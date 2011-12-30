import os
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.template import RequestContext

from picasa.models import Album
from gallery.models import Gallery
from gallery.downloader import downloadPicasaAlbum
from gallery.zipper import zip_photos
from gallery import util
from settings import PHOTOS_ZIP_URL

def gallery(request):
  section = "photos"
  return render_to_response('gallery/gallery.html', locals(),
                            context_instance=RequestContext(request, processors=[]))

def create_gallery_xml(request, gallery_id):
  gallery = get_object_or_404(Gallery, pk=gallery_id)
  util.create_gallery_xml(gallery)
  return HttpResponseRedirect("/admin/gallery/gallery/" + gallery_id)

def dwnld_picasa_album_zip(request, gallery_id):
  gallery = get_object_or_404(Gallery, pk=gallery_id)
  downloadPicasaAlbum(gallery.album)
  album_slug = slugify(gallery.album.title)
  zip_photos(album_slug)
  gallery.download_link = os.path.join(PHOTOS_ZIP_URL, album_slug + ".zip")
  gallery.save()
  return HttpResponseRedirect("/admin/gallery/gallery/" + gallery_id)
