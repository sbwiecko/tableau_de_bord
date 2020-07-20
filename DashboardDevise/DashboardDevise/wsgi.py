"""
WSGI config for DashboardDevise project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DashboardDevise.settings')

application = get_wsgi_application()

"""
in pythonanywhere.com we have the following configuration
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
#
## assuming your django settings file is at '/home/tryptofan/mysite/mysite/settings.py'
## and your manage.py is is at '/home/tryptofan/mysite/manage.py'
path = '/home/tryptofan/DashboardDevise'
if path not in sys.path:
    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'DashboardDevise.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
"""
