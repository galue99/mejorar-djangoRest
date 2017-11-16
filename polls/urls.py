__author__ = 'edgar'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^polls/$', views.PollsViews.as_view()),
    url(r'^polls/(?P<pk>[0-9]+)/$', views.PollDetail.as_view()),
    url(r'^pollusers/$', views.PollUserViews.as_view()),
    url(r'^pollusers/(?P<pk>[0-9]+)/$', views.PollUserDetail.as_view()),
    url(r'^levels/$', views.LevelViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)