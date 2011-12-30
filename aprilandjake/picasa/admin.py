from django.contrib import admin
from picasa.models import Album, Photo

class AlbumAdmin(admin.ModelAdmin):
    model = Album
    list_display = ('title', 'url')

class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ('title', 'url', 'album', 'pub_date')

admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)