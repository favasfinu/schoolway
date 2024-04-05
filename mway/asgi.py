"""
ASGI config for mway project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import django
from channels.routing import get_default_applicatin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mway.settings')

application = get_asgi_application()

if django. VERSION >= (4,0):
    application = get_asgi_application()