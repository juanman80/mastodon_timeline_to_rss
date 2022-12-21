from django.urls import path

from mastodon_timeline_to_rss.api import views

urlpatterns = [
    path('', views.index, name='index'),
]
