from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('bookStore.views',
    url(r'^$', 'book_list'),
    url(r'^(\d+)$', 'book_detail'),
)
