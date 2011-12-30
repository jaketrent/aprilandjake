from django.conf.urls.defaults import *

urlpatterns = patterns('picasa.views',
    url(r'^next/$', 'get_random_photo_ajax', name='picasa-random-photo'),
    url(r'^update/$', 'refresh_photos', name='picasa-refresh-photos'),
)