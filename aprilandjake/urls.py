from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django import forms

from django.contrib import admin

admin.autodiscover()

from feeds import *
from sitemap import *

feeds = {
	'blog': AllBlog,
}

sitemaps = {
    'blog': BlogSitemap,
}

urlpatterns = patterns('',
  (r'^', include('content.urls')),
	(r'^photos/', include('gallery.urls')),
	(r'^friends/', include('friends.urls')),
	(r'^picasa/', include('picasa.urls')),

	(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

	(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

  url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
