# Readme #



## Update ##

When updating this module remember to change the version in setup.cfg 
when updating setup.cfg use an editor that does not autoformat due to a format requirement for this file 
e.g use vim (the bug is caused on the line under package_src it needs the tab indent on the '= src' )

This is a repo for a slack builder plugin

## Build ##

currently this is built only on pypi test 

python -m build    
python -m twine upload --repository testpypi dist/*