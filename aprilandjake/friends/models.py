from django.db import models
	
class Friend(models.Model):
	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return u"%s" % (self.name)
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100, blank=True)
	date_created = models.DateTimeField(editable=False, auto_now_add=True)
	date_updated = models.DateTimeField(editable=False, auto_now=True)
	active = models.BooleanField(default=True)
	
class FriendProjectManager(models.Manager):
	def get_query_set(self):
		return super(FriendProjectManager, self).get_query_set().filter(active=True).order_by('-date_updated')		
	
class FriendProject(models.Model):
	class Meta:
		ordering = ['name']
	def __unicode__(self):
		return u"%s's %s" % (self.friend.name, self.name)
	name = models.CharField(max_length=100)
	url = models.URLField(max_length=200, verify_exists=False)
	date_created = models.DateTimeField(editable=False, auto_now_add=True)
	date_updated = models.DateTimeField(editable=False, auto_now=True)
	active = models.BooleanField(default=True)
	friend = models.ForeignKey(Friend)
	objects = FriendProjectManager()

