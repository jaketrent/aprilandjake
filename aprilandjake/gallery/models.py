from django.db import models

try:
    from picasa.models import Album
except:
    raise ValueError('This app is dependent on django-picasa being installed for project/django')

class Gallery(models.Model):
	title = models.CharField(max_length=100)
	title_slug = models.SlugField(unique=True)
	cover = models.URLField(null=True, blank=True)
	download_link = models.CharField(max_length=255, null=True, blank=True)
	xml_link = models.CharField(max_length=255, null=True, blank=True)
	album = models.ForeignKey(Album)
	date_created = models.DateTimeField(editable=False, auto_now_add=True)
	date_updated = models.DateTimeField(editable=False, auto_now=True)
	active = models.BooleanField(default=True)
	def __unicode__(self):
		return u"%s" % (self.title)
	def get_absolute_url(self):
		return self.url
	class Meta:
		ordering = ['title']
