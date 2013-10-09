from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'bookStore.views.book_list'),
    url(r'^(\d+)$', 'bookStore.views.book_detail'),
)
