from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        )

if settings.DEBUG:
    urlpatterns += patterns('',
            url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
                'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT,
                 }
                ),
            url(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
                'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT,
                 }
                ),
            )
