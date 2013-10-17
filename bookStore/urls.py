from django.conf.urls import patterns, url


urlpatterns = patterns('bookStore.views',
    url(r'^$', 'book_list'),
    url(r'^(\d+)$', 'book_detail'),
)
