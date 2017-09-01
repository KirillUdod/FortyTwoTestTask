from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^', include(u'hello.urls')),
    url(r'^admin/', include(admin.site.urls), name=u'admin'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

