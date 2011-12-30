import re

from piston.handler import BaseHandler
from piston.utils import rc, throttle

from models import Gallery

class GalleryHandler(BaseHandler):
  allowed_methods = ('GET',)
  fields = ('title', 'cover',)
  exclude = ('id', re.compile(r'^_slug'))
  model = Gallery
#
#  @classmethod
#  def content_size(self, proj):
#    return len(proj.synopsis)

  def read(self, request):
    return Gallery.objects.all()
#
#  def read(self, request, slug):
#    return Gallery.objects.filter(title_slug=slug)
