from django.contrib import admin
from gallery.models import Gallery

class GalleryAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'date_created', 'date_updated', 'active']
	prepopulated_fields = {'title_slug': ('title',)}

admin.site.register(Gallery, GalleryAdmin)