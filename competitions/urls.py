__author__ = 'edgar'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from competitions import views
from rest_framework import routers

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.


urlpatterns = [
    url(r'^competition/$', views.CompetitionViews.as_view()),
    url(r'^competition/(?P<pk>[0-9]+)/$', views.CompetitionDetailsViews.as_view()),
    url(r'^competition-type/$', views.CompetitionTypeViews.as_view()),
    url(r'^behaviors/$', views.BehaviorViews.as_view()),
    url(r'^behaviors/(?P<pk>[0-9]+)/$', views.BehaviorDetailsViews.as_view()),
    url(r'^competition-behavior/(?P<pk>[0-9]+)/$', views.CompetitionBehaviorViews.as_view()),
    url(r'^competition-behavior-mejorar/$', views.CompetitionBehaviorMejorarViews.as_view()),
    url(r'^competition-mejorar/$', views.CompetitionMejorarViews.as_view()),
    url(r'^competitions-save-mejorar/$', views.CompetitionSaveMejorarViews.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)