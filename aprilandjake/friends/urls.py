from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from content.models import Content
from friends.views import *
from settings import PAGINATION_SIZE

urlpatterns = patterns('',
    url(r'^$', friend_list, name='aj2-friends'),
    url(r'^favs/$', runner, name='aj2-blog-runner'),
)
