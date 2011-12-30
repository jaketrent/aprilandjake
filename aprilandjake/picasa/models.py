from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(verify_exists=True, unique=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url

    class Meta:
        ordering = ('title',)

class PhotoManager(models.Manager):
    def get_query_set(self):
        return super(PhotoManager, self).get_query_set().all()

    def random(self):
        return self.get_query_set().order_by('?')[:1][0]

class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=100)
    image = models.URLField(verify_exists=True)
    url = models.URLField(verify_exists=True, unique=True)
    pub_date = models.DateTimeField("Publication date", blank=True, null=True)

    objects = PhotoManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.url

    class Meta:
        ordering = ('title',)
        get_latest_by = 'pub_date'
