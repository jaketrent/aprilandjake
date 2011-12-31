from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
from content.models import Content
from content.views import *

urlpatterns = patterns('',
  url(r'^$', home, name='aj2-home'),

  url(r'^searchresults$', search_results, name='aj2-searchresults'),
  url(r'^content/(?P<slug>[\-\d\w]+)/$', content_detail, name='aj2-content-detail'),
  url(r'^content/collection/(?P<slug>[\-\d\w]+)/$', content_collection, name='aj2-content-collection'),

  url(r'^tags/$', tag_list, name='aj2-tags'),
  url(r'^tag/(?P<tag_name>[^/]+)/$', content_list_tag, name='aj2-content-tag'),

  url(r'^friends/$', friend_list, name='aj2-friends'),  

	# content shortcuts - also used in feed urls
	url(r'^podcast/$', content_podcast, name='aj2-podcast'),
	url(r'^blog/$', content_blog, name='aj2-blog'),
	url(r'^quotes/$', content_quotes, name='aj2-quotes'),

)
