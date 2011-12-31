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
  url(r'^', include('content.urls')),
	url(r'^photos/', include('gallery.urls')),
	url(r'^friends/', include('friends.urls')),
	url(r'^picasa/', include('picasa.urls')),

	url(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

	url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

  url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG is False:
  urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
  )
elif settings.DEBUG is True:
  urlpatterns += staticfiles_urlpatterns()


