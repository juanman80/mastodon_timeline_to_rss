import logging

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from mastodon import Mastodon

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    mastodon = Mastodon(access_token=settings.MASTODON_BEARER, api_base_url=settings.MASTODON_HOST)
    timeline = mastodon.timeline_home()
    return render(request, 'index.xml', {'timeline': timeline})
