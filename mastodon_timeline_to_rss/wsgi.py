"""
WSGI config for mastodon_timeline_to_rss project.

It exposes the WSGI callable as a module-level variable named ``application``.

# not really used, I need to edit
#  /var/www/juanman80_eu_pythonanywhere_com_wsgi.py


For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mastodon_timeline_to_rss.settings')


env_file = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), '..', '.env')
dotenv.read_dotenv(env_file)

application = get_wsgi_application()
