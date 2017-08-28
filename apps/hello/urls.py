from django.conf.urls import patterns, include, url

from .views import IndexPage

urlpatterns = patterns(
    '',
    url(r'^$', IndexPage.as_view(), name=u'index'),

)
