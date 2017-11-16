__author__ = 'edgar'

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from answers import views
from rest_framework import routers
from accounts.views import AccountsViews, AccountsDetailsViews


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.


urlpatterns = [
    url(r'^answers/$', views.AnswersViews.as_view()),
    url(r'^answers/(?P<pk>[0-9]+)/$', views.AnswerViewsDetail.as_view()),
    url(r'^user-answers/$', views.UserAnswerViews.as_view()),
    url(r'^user-answers/(?P<pk>[0-9]+)/$', views.UserAnswerDetailViews.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)