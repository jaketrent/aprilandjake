from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from content.models import Content
from friends.views import *

urlpatterns = patterns('',
    url(r'^$', friend_list, name='aj2-friends'),
    url(r'^favs/$', runner, name='aj2-blog-runner'),
)
