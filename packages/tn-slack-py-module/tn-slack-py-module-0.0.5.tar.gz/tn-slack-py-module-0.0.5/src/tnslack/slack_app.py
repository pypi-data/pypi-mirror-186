import hashlib
import hmac
import json
import logging
import math
from datetime import datetime
from urllib.parse import urlencode

import requests
from requests.exceptions import HTTPError

from . import constants as slack_consts
from .block_builder import BlockBuilder
from .exceptions import SlackAppException
from .utils import SlackUtils

logger = logging.getLogger(__name__)


class SlackApp:
    SLACK_API_ROOT = "https://slack.com/api/"
    SLACK_OAUTH_AUTHORIZE_ROOT = "https://slack.com/oauth/v2/authorize"
    # https://api.slack.com/methods/oauth.v2.access
    OAUTH_V2_ACCESS = "oauth.v2.access"

    # https://api.slack.com/methods/conversations.open
    CONVERSATIONS_OPEN = "conversations.open"

    # https://api.slack.com/methods/chat.postMessage
    POST_MESSAGE = "chat.postMessage"

    POST_EPHEMERAL = "chat.postEphemeral"

    # https://api.slack.com/methods/views.open

    VIEWS_OPEN = "views.open"

    VIEWS_UPDATE = "views.update"

    VIEWS_PUSH = "views.push"

    VIEWS_PUBLISH = "views.publish"

    #  https://api.slack.com/methods/chat.getPermalink
    CHAT_GET_PERMALINK = "chat.getPermalink"

    # https://api.slack.com/methods/chat.update
    CHAT_UPDATE = "chat.update"

    APP_VERSION = "v0"

    TOKEN_TYPE_BOT = "bot"

    TOKEN_TYPE_USER = "user"

    JSON_HEADERS = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
    }
    URL_ENCODED_HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    }
    ROUTES = {
        slack_consts.BLOCK_ACTIONS: {},
        slack_consts.BLOCK_SUGGESTION: {},
        slack_consts.VIEW_SUBMISSION: {},
        slack_consts.VIEW_CLOSED: {},
    }

    _ROUTE_TYPES = [
        slack_consts.BLOCK_ACTIONS,
        slack_consts.BLOCK_SUGGESTION,
        slack_consts.VIEW_CLOSED,
        slack_consts.VIEW_SUBMISSION,
    ]
    BLOCK_SETS = dict()

    def __init__(
        self,
        client_id,
        client_secret,
        signing_secret,
        redirect_url,
        bot_scopes=[],
        user_scopes=[],
        error_webhook=None,
    ):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
        self.SIGNING_SECRET = signing_secret
        self.BOT_SCOPES = bot_scopes
        self.USER_SCOPES = user_scopes
        self.REDIRECT_URL = redirect_url
        self.ERROR_WEBHOOK = error_webhook

    @classmethod
    def configure(
        cls,
        client_id,
        client_secret,
        signing_secret,
        redirect_url,
        bot_scopes=[],
        user_scopes=[],
        error_webhook=None,
    ):
        return cls(
            client_id,
            client_secret,
            signing_secret,
            redirect_url,
            bot_scopes,
            user_scopes,
            error_webhook,
        )

    def _handle_response(self, response, fn_name=None, blocks=[]):
        if not hasattr(response, "status_code"):
            raise ValueError

        else:
            status_code = response.status_code
            try:
                res_data = response.json()
            except json.decoder.JSONDecodeError:
                # one slack request (see generic requests) does not return json
                return response.text

            if not res_data.get("ok"):
                error_code = response.status_code
                error_param = res_data.get("error")
                if res_data.get("response_metadata", None):
                    error_message = res_data.get("response_metadata", {}).get("messages")
                elif res_data.get("error", None):
                    error_message = res_data.get("error")
                else:
                    error_message = response.text

                kwargs = {
                    "status_code": status_code,
                    "error_code": error_code,
                    "error_param": error_param,
                    "error_message": error_message,
                }
                try:
                    SlackAppException(HTTPError(kwargs), blocks=blocks)
                except Exception as e:
                    if self.ERROR_WEBHOOK:
                        try:
                            self.generic_request(
                                self.ERROR_WEBHOOK,
                                {"text": f"An error occured {e}"},
                            )
                        except Exception as fail_safe_error:
                            logger.info(fail_safe_error)
                            pass
                    raise e

            return res_data

    def _check_request_time_stamp(self, request):
        time_stamp = request.headers.get("X-Slack-Request-Timestamp", None)
        if not time_stamp:
            raise ValueError
        is_expired = int(time_stamp) <= math.floor(datetime.timestamp(datetime.now() - datetime.timedelta(minutes=5)))
        if is_expired:
            raise ValueError

        return time_stamp

    def authenticate_incoming_request(self, request):

        time_stamp = self._check_time_stamp(request)
        slack_signature = request.headers.get("X-Slack-Signature", None)
        if not slack_signature:
            raise ValueError
        data = request.body.decode("utf-8")
        sig_basedstring = (f"{self.APP_VERSION}:{time_stamp}:{data}").encode("utf-8")
        my_sig = (
            self.APP_VERSION
            + "="
            + hmac.new(
                self.SIGNING_SECRET.encode("utf-8"),
                sig_basedstring,
                hashlib.sha256,
            ).hexdigest()
        )
        if hmac.compare_digest(my_sig, slack_signature):
            return True
        return False

        raise ValueError

    def retrieve_data_with_code(self, code):
        url = self.SLACK_API_ROOT + self.OAUTH_V2_ACCESS
        data = {
            "code": code,
            "redirect_uri": self.REDIRECT_URL,
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET,
        }

        return self._handle_response(
            requests.post(
                url,
                data=data,
                headers=self.URL_ENCODED_HEADERS,
            )
        )

    def revoke_access_token(self, token):
        query = urlencode({"token": token})
        url = self.SLACK_API_ROOT + "auth.revoke?" + query

        return requests.post(
            url,
            headers=self.URL_ENCODED_HEADERS,
        )

    def block_finder(self, block_id, blocks=[]):
        item = list(
            filter(
                lambda x: x[1]["block_id"] == block_id,
                enumerate(blocks),
            )
        )
        if len(item):
            return item[0]
        return item

    def auth_headers(self, access_token):
        return {"Authorization": "Bearer " + access_token, **self.JSON_HEADERS}

    def _block_action_consumer(self, payload):
        action_query_string = payload["actions"][0]["action_id"]
        processed_string = self.utils.process_action_id(action_query_string)
        action_id = processed_string.get("true_id")
        action_params = processed_string.get("params")
        # special override for block_actions
        if action_params.get("__block_action", None):
            action_id = action_params.get("__block_action")
        switcher = self._action_routes
        return switcher.get(action_id, self.utils.NO_OP)(payload, action_params)

    def _block_suggestion_consumer(self, payload):
        action_query_string = payload["action_id"]
        processed_string = self.utils.process_action_id(action_query_string)
        action_id = processed_string.get("true_id")
        action_params = processed_string.get("params")
        switcher = self._suggestion_routes
        return switcher.get(action_id, self.utils.NO_OP)(payload, action_params)

    def _view_submission_consumer(self, payload):
        callback_id = payload["view"]["callback_id"]
        view_context = json.loads(payload["view"]["private_metadata"])
        switcher = self._view_submission_routes
        return switcher.get(callback_id, self.utils.NO_OP)(payload, view_context)

    def _view_closed_consumer(self, payload):
        view = payload["view"]
        callback_id = payload["view"]["callback_id"]
        switcher = self._view_closed_routes
        return switcher.get(callback_id, self.utils.NO_OP)(payload, view)

    def register_route(self, route_type, route_fn, name=None):
        """Register's interaction routes"""
        if route_type not in self._ROUTE_TYPES:
            raise ValueError(f"Invalid Route Type, only {', '.join(self._ROUTE_TYPES)} available")
        name = name if name else route_fn.__name__
        self.ROUTES.get(route_type).update({name: route_fn})
        return

    def register_block_set(self, block_set_fn, name=None):
        name = name if name else block_set_fn.__name__
        self.BLOCK_SETS.update({name: block_set_fn})
        return

    def slack_interaction_consumer(self, payload):
        """
        expects a payload to be sent
        example usage in django view
        payload = json.loads(request.data.get("payload"))
        process_output = slack_app.slack_interaction_consumer(payload)
        return Response(data=json.dumps(process_output))
        """
        switcher = {
            slack_consts.BLOCK_ACTIONS: self._block_action_consumer,
            slack_consts.BLOCK_SUGGESTION: self._block_suggestion_consumer,
            slack_consts.VIEW_SUBMISSION: self._view_submission_consumer,
            slack_consts.VIEW_CLOSED: self._view_closed_consumer,
        }

        return switcher.get(payload["type"], self.utils.NO_OP)(payload)

    def slack_event_request_consumer(self, request):
        if request.data.get("type") == slack_consts.EVENT_URL_VERIFICATION:
            event_type = "challenge"
            event_tab = None
            event_data = request.data.get("challenge")
        else:
            event_data = request.data.get("event", {})
            event_type = event_data.get("type")
            event_tab = event_data.get("tab")

        return dict(event_type=event_type, event_tab=event_tab, event_data=event_data)

    def get_block_set(self, set_name, context={}, *args, **kwargs):
        try:
            return self.BLOCK_SETS.get(set_name)(context, *args, **kwargs)
        except TypeError:
            raise TypeError("Block Set not found or not registered")

    def workspace_install_link(self, team_id=None, state=None):
        params = dict(
            redirect_uri=self.REDIRECT_URL,
            client_id=self.CLIENT_ID,
            scope=",".join(self.BOT_SCOPES),
        )
        if state:
            params["state"] = state
        if team_id:
            params["team_id"] = team_id
        return self.SLACK_OAUTH_AUTHORIZE_ROOT + "?" + urlencode(params)

    def user_install_link(self, team_id=None, state=None):
        params = dict(
            redirect_uri=self.REDIRECT_URL,
            client_id=self.CLIENT_ID,
            user_scope=",".join(self.USER_SCOPES),
        )
        if state:
            params["state"] = state
        if team_id:
            params["team_id"] = team_id
        return self.SLACK_OAUTH_AUTHORIZE_ROOT + "?" + urlencode(params)

    def generic_request(self, url, data, access_token=None):
        original_data = data
        res = requests.post(
            url,
            data=json.dumps(data),
            headers=self.auth_headers(access_token) if access_token else self.JSON_HEADERS,
        )
        return self._handle_response(res, blocks=original_data.get("blocks"))

    def open_user_conversation_channel(self, user_slack_id, access_token):
        """
        Request the Slack Channel ID for a 1:1 conversation
        between the user and bot
        """
        url = self.SLACK_API_ROOT + self.CONVERSATIONS_OPEN
        data = {"users": user_slack_id}
        res = requests.post(
            url,
            data=json.dumps(data),
            headers=self.auth_headers(access_token),
        )
        return self._handle_response(res, blocks=[])

    def send_channel_message(self, channel, access_token, text="Slack Message", block_set=[]):
        """
        Posts a message to a channel
        """
        url = self.SLACK_API_ROOT + self.POST_MESSAGE
        data = {}
        data["channel"] = channel
        data["text"] = text
        data["blocks"] = block_set

        res = requests.post(
            url,
            data=json.dumps(data),
            headers=self.auth_headers(access_token),
        )
        return self._handle_response(res, blocks=block_set)

    def publish_view(self, slack_id, access_token, view):
        """
        Publishes a view to the user's home tab
        slack_id: user slack id
        """
        url = self.SLACK_API_ROOT + self.VIEWS_PUBLISH
        data = {}
        data["user_id"] = slack_id
        data["view"] = view

        res = requests.post(
            url,
            data=json.dumps(data),
            headers=self.auth_headers(access_token),
        )
        return self._handle_response(res, data)

    def send_ephemeral_message(self, channel, access_token, slack_id, text="Slack Message", block_set=[]):
        """
        Posts a message to DM channel.
        *Channel and User are required for ephemeral messages
        """
        url = self.SLACK_API_ROOT + self.POST_EPHEMERAL
        data = {}
        data["channel"] = channel
        data["text"] = text
        data["blocks"] = block_set
        data["user"] = slack_id

        res = requests.post(
            url,
            data=json.dumps(data),
            headers=self.auth_headers(access_token),
        )
        return self._handle_response(res, blocks=block_set)

    def update_channel_message(self, channel, message_timestamp, access_token, text="Managr", block_set=[]):
        """
        Updates a message in DM.
        """
        url = self.SLACK_API_ROOT + self.CHAT_UPDATE
        data = {}
        data["channel"] = channel
        data["ts"] = message_timestamp

        data["text"] = text
        data["blocks"] = block_set
        res = requests.post(
            url,
            data=json.dumps(data),
            headers=self.auth_headers(access_token),
        )
        return self._handle_response(res, blocks=block_set if block_set else [])

    @property
    def utils(self):
        return SlackUtils()

    @property
    def block_builder(self):
        return BlockBuilder()

    @property
    def constants(self):
        return

    @property
    def _action_routes(self):
        return self.ROUTES.get(slack_consts.BLOCK_ACTIONS)

    @property
    def _suggestion_routes(self):
        return self.ROUTES.get(slack_consts.BLOCK_SUGGESTION)

    @property
    def _view_submission_routes(self):
        return self.ROUTES.get(slack_consts.VIEW_SUBMISSION)

    @property
    def _view_closed_routes(self):
        return self.ROUTES.get(slack_consts.VIEW_CLOSED)
