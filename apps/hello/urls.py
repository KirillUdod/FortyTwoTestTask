from django.conf.urls import patterns, url

from .views import IndexPage, RequestsPage, NewRequestsView, EditView, LogOut, LoginView

urlpatterns = patterns(
    '',
    url(r'^$', IndexPage.as_view(), name=u'index'),
    url(r'^requests/$', RequestsPage.as_view(), name=u'requests'),
    url(r'^edit/$', EditView.as_view(), name=u'edit'),
    url(r'^get_new_requests/$', NewRequestsView.as_view(),
        name='new_requests'),
    url(r'^login/$', LoginView.as_view(), name=u'login'),
    url(r'^logout/$', LogOut.as_view(), name=u'logout'),

)
