import uuid


class BlockBuilder:
    @staticmethod
    def context_block(value, text_type="plain_text", block_id=None):
        if not block_id:
            block_id = str(uuid.uuid4())
        return {
            "type": "context",
            "elements": [{"type": text_type, "text": value}],
            "block_id": block_id,
        }

    @staticmethod
    def text_block(value, text_type="plain_text"):
        return {"type": text_type, "text": value}

    @staticmethod
    def input_block(
        label,
        initial_value=None,
        placeholder=False,
        multiline=False,
        placeholder_type="plain_text",
        action_id="plain_input",
        block_id=None,
        label_type="plain_text",
        min_length=False,
        max_length=False,
        optional=True,
    ):
        """
        Creates a basic text input block

        Parameters:
        label - String of what the label text should be
        initial_value - Set an initial value for input using string passed in, otherwise None
        placeholder - Sets placeholder text for input using string passed in, defaults to no placeholder
        multiline - If True will set text input (in slack) to a Multiline text area
        placeholder_type - Only used if placeholder is passed in, sets placeholder type to plain_text
        action_id - Sets id of input to value passed in, otherwise defaults to 'plain_input'
        block_id - Set id of block to value passed in, if none is passed in will create one with uuid
        label_type - Sets the label type to plain_text. SHOULD NOT BE CHANGED.
        min_length - Set a minimum length for the input
        max_length - Set a maximum length for the input
        optional - indicated whether the input can be left blank

        If a placeholder, min_length, max_length is
        passed in it will be used otherwise False
        will not add a placeholder

        For a basic input only a string for the label has to be passed in.
        """

        if not block_id:
            block_id = str(uuid.uuid4())
        obj = {
            "type": "input",
            "block_id": block_id,
            "label": {"type": label_type, "text": label},
            "optional": optional,
            "element": {
                "type": "plain_text_input",
                "action_id": action_id,
                "multiline": multiline,
            },
        }
        if placeholder:
            # placeholder is a text_block
            obj["element"]["placeholder"] = BlockBuilder.text_block(placeholder, placeholder_type)

        if max_length:
            obj["element"]["max_length"] = max_length

        if min_length:
            obj["element"]["min_length"] = min_length

        if initial_value:
            initial_value = str(initial_value)
            obj["element"]["initial_value"] = initial_value

        return obj

    @staticmethod
    def simple_section_block(value, text_type="plain_text", block_id=None):
        if not block_id:
            block_id = str(uuid.uuid4())
        return {
            "type": "section",
            "text": {"type": text_type, "text": value},
            "block_id": block_id,
        }

    @staticmethod
    def simple_section_multiple_block(text_blocks, block_id=None):
        """sections can have multiple fields they are a collection of text_block

        Parameters
        -----------
        text_blocks: object
            contains plain text or markup
        block_id: str
            block i.d number. If not entered will generate random str
        """

        if not block_id:
            block_id = str(uuid.uuid4())
        return {"type": "section", "fields": text_blocks, "block_id": block_id}

    @staticmethod
    def option(text, value):
        """accepts a string and returns an object with 2 properties, type and text.

        The type property is set to plain_text. The text property is given the value of the
        string entered.

        Parameters
        ----------
        text: str
            plain text
        value: any
        """

        return {
            "text": {"type": "plain_text", "text": text},
            "value": value,
        }

    @staticmethod
    def divider_block():
        """returns an object that has one property, type:divider"""
        return {"type": "divider"}

    @staticmethod
    def header_block(text, block_id=None):
        """
        Creates a header block to be used inside other blocks

        Parameters:
        text - Set text as any String passed in.
        block_id - Optional Id can be passed in, otherwise creates one with uuid
        """
        if not block_id:
            block_id = str(uuid.uuid4())
        return {
            "type": "header",
            "text": {"type": "plain_text", "text": text},
            "block_id": block_id,
        }

    @staticmethod
    def external_select_block(
        label,
        action_id,
        initial_option=None,
        block_id=None,
        min_query_length=0,
        placeholder="Select",
    ):
        """returns a section block with markdown text and an external_select dropdown menu

        External menu's load their options from an external data source, allowing for a dynamic list of options.

        Parameters
        ----------
        label: mrkdwn
            markdown text for the section block.
        action_id: str
            An identifier for the action triggered when a menu option is selected.
        initial_option: obj
            The option selected when the menu initially loads.
        block_id: str
            Unique identifier for the block
        min_query_length: int
            Tell's Slack the fewest number of typed characters required before dispatch.
        placeholder: obj
            Defines the placeholder text shown on the menu. Maximum length for the text in this field is 150 characters.
        """

        block = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{label}"},
            "accessory": {
                "type": "external_select",
                "action_id": action_id,
                "placeholder": {"type": "plain_text", "text": placeholder},
                "min_query_length": min_query_length,
            },
        }
        if initial_option:
            block["accessory"]["initial_option"] = initial_option
        if block_id:
            block["block_id"] = block_id
        return block

    @staticmethod
    def static_select_block(
        label,
        options,
        action_id=None,
        initial_option=None,
        placeholder="Select",
        block_id=None,
    ):
        """ "
        Returns a select block where the select values are known and won't change.

        Parameters:
        label - A string for the select input label
        options - Options are an array of options (see above)
        action_id - Will be included if entered otherwise None
        initial_option - An option block has to be entered, this shows the entered option
        when first being displayed
        placeholder - Changed placeholder text, otherwise defautls to Select
        block_id - Sets block_id, otherwise will use uuid to set.

        Function returns an entire section with the select input.
        Only parameters that need to be entered are label and array of options.
        """

        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{label}"},
            "block_id": block_id,
            "accessory": {
                "type": "static_select",
                "placeholder": {"type": "plain_text", "text": placeholder},
                "options": options,
            },
        }
        if initial_option:
            block["accessory"]["initial_option"] = initial_option
        if action_id:
            block["accessory"]["action_id"] = action_id
        return block

    @staticmethod
    def multi_static_select_block(
        label,
        options,
        action_id=None,
        initial_options=None,
        placeholder="Select",
        block_id=None,
    ):
        """
        Creates a selection input for selecting multiple options

        Parameters:
        label - String of what the label text should be
        options  - must be an array of options (see above)
        action_id - set id to the value passed in, otherwise None
        initial_options - must be an array of options (see above) to show when initially loading
        placeholder - String for the placeholder text in the input, otherwise 'Select'
        block_id - set id of block to value passed in, otherwise created with uuid

        Should be used when the value of the selection are known
        and do not need to be gotten from and external source
        """

        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{label}"},
            "block_id": block_id,
            "accessory": {
                "type": "multi_static_select",
                "placeholder": {"type": "plain_text", "text": placeholder},
                "options": options,
            },
        }
        if initial_options:
            block["accessory"]["initial_options"] = initial_options
        if action_id:
            block["accessory"]["action_id"] = action_id
        return block

    @staticmethod
    def multi_external_select_block(
        label,
        action_id,
        initial_options=None,
        placeholder="Select",
        block_id=None,
        min_query_length=0,
    ):
        """A section block with markup text and a multi_external_select menu.

        Works the same as the external_select, but allows a user to select multiple items.

        If the section block has no id it will generate a random one. Returns the section block
        with the initial option if one was selected, and without the initial option if it was not
        selected.
        """

        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{label}"},
            "block_id": block_id,
            "accessory": {
                "type": "multi_external_select",
                "placeholder": {"type": "plain_text", "text": placeholder},
                "action_id": action_id,
                "min_query_length": min_query_length,
            },
        }
        if initial_options:
            block["accessory"]["initial_options"] = initial_options

        return block

    @staticmethod
    def datepicker_block(
        initial_date=None,
        action_id=None,
        block_id=None,
        label="Select Date",
        placeholder="Select a date",
    ):
        """
        Function returns a datepicker block object

        Parameters:
        initial_date - Sets the initial value to the date string passed in, must be 'YEAR-MONTH-DAY' format (ex '2020-04-21')
        action_id - Sets id to value passed in, otherwise None
        block_id - Sets id to value passed in, otherwise sets id with uuid
        label - Sets the label to the string passed in, otherwise default is 'Select Date'
        placeholder - Sets the placeholder text of the input to string passed in, otherwise default is 'Select a date'

        """
        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "text": {"type": "mrkdwn", "text": f"{label}"},
            "block_id": block_id,
            "accessory": {
                "type": "datepicker",
                "placeholder": {"type": "plain_text", "text": f"{placeholder}"},
            },
        }
        if initial_date:
            block["accessory"]["initial_date"] = initial_date
        if action_id:
            block["accessory"]["action_id"] = action_id
        return block

    @staticmethod
    def section_with_button_block(
        button_label,
        button_value,
        section_text,
        text_type="mrkdwn",
        block_id=None,
        url=None,
        style=None,
        confirm=False,
        action_id=None,
    ):
        """
        Function returns a section object with a button.

        Parameters:
        button_label - Sets the text of the button, needs to be included
        button_value - Sets the value to be passed along in the payload, needs to be included
        section_text - Sets the text of the section body, needs to be included
        text_type - Sets the type for the section block, generally doesn't need to be changed
        block_id - Sets the block_id to string passed in, otherwise is set with uuid
        url - If included the button will forward the user to the url, otherwise None
        style - If included changes the style of the button, options are default, primary, or danger.
        confirm - If True will have a popup confirmation window appear when button is pressed.
        action_id - Sets the action_id to string passed in, otherwise is set with uuid.

        Used for linking to another site/page or confirming information.
        """
        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "text": {"type": text_type, "text": section_text},
            "block_id": block_id,
            "accessory": {
                "type": "button",
                "text": {"type": "plain_text", "text": button_label},
                "value": button_value,
                # "confirm": confirm,
                "action_id": action_id if action_id else str(uuid.uuid4()),
            },
        }
        if style:
            block["accessory"]["style"] = style
        if url:
            block["accessory"]["url"] = url
        return block

    @staticmethod
    def simple_button_block(label, value, url=None, style=None, confirm=False, action_id=None):
        """
        Function returns an object for a button block.

        label - Sets text of the button
        value - Sets value of the button to be passed in the payload
        url - If included button will forward user to the url, otherwise None
        style - If included will change the appearance of the button.
                Choices are default, primary, or danger
        confirm - If included will add a popup window confirming button press
        action_id - Sets the action_id to string passed in, otherwise set with uuid, must be unique

        This block can only be used in action_block function and action_id must be unique
        """

        block = {
            "type": "button",
            "text": {"type": "plain_text", "text": label},
            "value": value,
            # "confirm": confirm,
            "action_id": action_id if action_id else str(uuid.uuid4()),
        }
        if style:
            block["style"] = style
        if url:
            block["url"] = url
        return block

    @staticmethod
    def actions_block(blocks=[], block_id=None):
        """
        Array of interactive element objects - buttons, select menus, overflow menus, or date pickers.
        max of 5

        parameters
        ----------
        blocks: array
            Element objects
        block_id: str
            A unique identifier for the block
        """

        if not len(blocks):
            return
        if len(blocks) > 4:
            return
        if not block_id:
            block_id = str(uuid.uuid4())
        return {"type": "actions", "block_id": block_id, "elements": [*blocks]}

    @staticmethod
    def checkbox_block(label, options, action_id=None, initial_options=None, block_id=None):
        """
        Function returns a section with checkbox inputs.

        Parameters:
        label - String to set the text of the section, must be included
        options - array of options (see above), must be included
        action_id - sets action_id to value passed in, otherwise sets id from uuid
        initial_options - Array of options (see above), if included will pre-check those options
        block_id - sets block_is as value entered, otherwise sets if from uuid

        """
        if not action_id:
            action_id = str(uuid.uuid4())
        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "block_id": block_id,
            "text": {"type": "mrkdwn", "text": f"{label}"},
            "accessory": {
                "type": "checkboxes",
                "action_id": action_id,
                "options": options,
            },
        }
        if initial_options:
            block["accessory"]["initial_options"] = initial_options
        return block

    @staticmethod
    def section_with_accessory_block(
        section_text,
        accessory,
        text_type="mrkdwn",
        block_id=None,
    ):
        """ " Builds a section with an accessory (image/button)

        parameters
        ----------
        section_text: str
            text for the section block
        accessory: obj
            element object
        text_type: str
            markdown
        block_id: str
            unique identifier
        """
        if not block_id:
            block_id = str(uuid.uuid4())
        block = {
            "type": "section",
            "text": {"type": text_type, "text": section_text},
            "block_id": block_id,
            "accessory": accessory,
        }

        return block

    @staticmethod
    def simple_image_block(url, alt_text):
        """An image block object with the image's url and alt text.

        parameters
        ----------
        url: str
            The URL of the image to be displayed. Maximum length for this field is 3000 characters.
        alt_text: str
            A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.
        """
        return {
            "type": "image",
            "image_url": url,
            "alt_text": alt_text,
        }

    @staticmethod
    def multi_channels_select_block(
        section_text,
        placeholder_text="Select Channels",
        section_text_type="mrkdwn",
        block_id=None,
        action_id=None,
        initial_channels=[],
        max_selected_items=None,
    ):
        if not block_id:
            block_id = str(uuid.uuid4())
        accessory_block = {
            "type": "multi_channels_select",
            "placeholder": BlockBuilder.text_block(placeholder_text),
        }
        if action_id:
            accessory_block["action_id"] = action_id
        if initial_channels and len(initial_channels):
            accessory_block["initial_channels"] = initial_channels
        if max_selected_items not in ["", None]:
            accessory_block["max_selected_items"] = max_selected_items

        block = BlockBuilder.section_with_accessory_block(
            section_text,
            accessory_block,
            text_type=section_text_type,
            block_id=block_id,
        )
        return block

    @staticmethod
    def multi_conversations_select_block(
        section_text,
        placeholder_text="Select Channels",
        section_text_type="mrkdwn",
        block_id=None,
        action_id=None,
        initial_conversations=[],
        max_selected_items=None,
        default_to_current_conversation=False,
        filter_opts=None,  # see https://api.slack.com/reference/block-kit/composition-objects#filter_conversations
    ):
        if not block_id:
            block_id = str(uuid.uuid4())
        accessory_block = {
            "type": "multi_conversations_select",
            "placeholder": BlockBuilder.text_block(placeholder_text),
        }
        if action_id:
            accessory_block["action_id"] = action_id
        if initial_conversations and len(initial_conversations):
            accessory_block["initial_conversations"] = initial_conversations
        if max_selected_items not in ["", None]:
            accessory_block["max_selected_items"] = max_selected_items
        if filter_opts:
            accessory_block["filter"] = filter_opts

        block = BlockBuilder.section_with_accessory_block(
            section_text,
            accessory_block,
            text_type=section_text_type,
            block_id=block_id,
        )
        return block
