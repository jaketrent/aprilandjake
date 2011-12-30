from django.conf.urls.defaults import *
from piston.resource import Resource

from views import *
from handlers import GalleryHandler

gallery_resource = Resource(handler=GalleryHandler)

urlpatterns = patterns('',
	url(r'^$', gallery, name='aj2-gallery'),
	url(r'^load/$', gallery_resource, name='aj2-gallery-load'),
	url(r'^generate/xml/(?P<gallery_id>\d+)$', create_gallery_xml, name='aj2-gallery-gen-xml'),
	url(r'^download/zip/(?P<gallery_id>\d+)$', dwnld_picasa_album_zip, name='aj2-gallery-dwnld-zip'),
)
