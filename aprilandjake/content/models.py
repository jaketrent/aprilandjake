from datetime import datetime
import os
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from tagging.fields import TagField
from settings import PROJ_PATH
from gallery.models import Gallery

class Template(models.Model):
	title = models.CharField(max_length=250)
	title_slug = models.SlugField(unique=True)
	list_path = models.FilePathField(path=os.path.join(PROJ_PATH, "templates/collections/"), match=".*\.html$", recursive=True)
	detail_path = models.FilePathField(path=os.path.join(PROJ_PATH, "templates/collections/"), match=".*\.html$", recursive=True)
	date_created = models.DateTimeField(editable=False, auto_now_add=True)
	date_updated = models.DateTimeField(editable=False, auto_now=True)
	active = models.BooleanField(default=True)
	class Meta:
		ordering = ["title"]
	def __unicode__(self):
		return u'%s' % (self.title)

class Collection(models.Model):
	title = models.CharField(max_length=250)
	title_slug = models.SlugField(unique=True)
	description = models.TextField(max_length=10000, blank=True, null=True)
	template = models.ForeignKey(Template)
	date_created = models.DateTimeField(editable=False, auto_now_add=True)
	date_updated = models.DateTimeField(editable=False, auto_now=True)
	active = models.BooleanField(default=True)
	fake_sort = models.IntegerField(blank=True, null=True, default=100)
	class Meta:
		ordering = ["title"]
	def __unicode__(self):
		return u'%s' % (self.title)

class Content(models.Model):
  title = models.CharField(max_length=250)
  title_slug = models.SlugField(unique=True)
  tagline = models.CharField(max_length=250, blank=True, null=True)
  columns = models.IntegerField(blank=True, null=True, default=3)
  summary = models.TextField(max_length=1000, blank=True, null=True)
  body = models.TextField(blank=True, null=True)
  small_section_1 = models.CharField(max_length=255, blank=True, null=True)
  small_section_2 = models.CharField(max_length=255, blank=True, null=True)
  small_section_3 = models.CharField(max_length=255, blank=True, null=True)
  small_section_4 = models.CharField(max_length=255, blank=True, null=True)
  small_section_5 = models.CharField(max_length=255, blank=True, null=True)
  web_link = models.URLField(null=True, blank=True)
  doc_link = models.URLField(null=True, blank=True)
  audio_link = models.URLField(null=True, blank=True)
  video_link = models.URLField(null=True, blank=True)
  collection = models.ForeignKey(Collection)
  gallery = models.ForeignKey(Gallery, blank=True, null=True)
  image_path = models.CharField(max_length=500, blank=True, null=True)
  file = models.FileField(upload_to='files/', null=True, blank=True)
  user = models.ForeignKey(User, help_text='This should be you.')
  tags = TagField(help_text='Separate tags with spaces, put quotes around multiple-word tags.', blank=True, null=True)
  date_published = models.DateTimeField(default=datetime.now)
  date_created = models.DateTimeField(editable=False, auto_now_add=True)
  date_updated = models.DateTimeField(editable=False, auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    ordering = ["title"]

  def __unicode__(self):
    return u'%s' % (self.title)

  def get_absolute_url(self):
    return "http://%s/content/%s/" % (Site.objects.get_current().domain, str(self.title_slug))

  def intro_img(self):
    if self.image_path:
      return self.image_path

