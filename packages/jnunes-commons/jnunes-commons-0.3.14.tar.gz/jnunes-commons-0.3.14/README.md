# Commons Django Application

Commons Application to Django projects

## Project Architecture

python (Contains a collections of reusable function)
static files templates templatetags

## Package usage

To use this project, install the last version available on
pypi [jnunes-commons](https://pypi.org/project/jnunes-commons/)
For package install, run ``pip install jnunes-commons``. After install, change your settings.py and add the dependency
to INSTALLED_APP list, like this:

```python
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'commons',
]
```

## Custom tags usage

To use the custom tags, on your template file, include: ``{% load static %}``

## Override default files

If you need to display your own favicon.ico file, you can do that by creating the same directory structure in your
project. For example:
In your static files directory, create: commons/img/favicon.ico. The favicon.ico it's your own image. When you run the
collectstatic command, the default files will be overwritten.