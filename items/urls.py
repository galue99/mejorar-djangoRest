__author__ = 'edgar'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from items import views
from rest_framework import routers

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.


urlpatterns = [
    url(r'^items/$', views.ItemViews.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetailsViews.as_view()),
    url(r'^phrases/$', views.PhraseViews.as_view()),
    url(r'^phrases/(?P<pk>[0-9]+)/$', views.PhraseDetailsViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)