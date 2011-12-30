from django.contrib import admin
from content.models import Content, Collection, Template

class ContentAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'date_published', 'date_created', 'date_updated', 'active']
	prepopulated_fields = {'title_slug': ('title',)}
	search_fields = ['title','summary','body']
	date_hierarchy = 'date_published'
	fieldsets = (
            (None, {
                'classes': ('',),
                'fields': ('title', 'title_slug', 'tagline', 'columns', 'summary', 'body')
            }),
            ('', {
                'classes': ('',),
                'fields': ('collection', 'user', 'date_published', 'tags')
            }),
            ('Small Sections', {
                'classes': ('collapse',),
                'fields': ('small_section_1', 'small_section_2', 'small_section_3', 'small_section_4', 'small_section_5')
            }),
            ('Links', {
                'classes': ('collapse',),
                'fields': ('web_link', 'doc_link', 'audio_link', 'video_link')
            }),
            ('Other', {
                'classes': ('collapse',),
                'fields': ('gallery', 'image_path', 'file')
            }),
            
        )


class CollectionAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'date_created', 'date_updated', 'active']
	prepopulated_fields = {'title_slug': ('title',)}

class TemplateAdmin(admin.ModelAdmin):
	list_display = ['title', 'id', 'date_created', 'date_updated', 'active']
	prepopulated_fields = {'title_slug': ('title',)}

admin.site.register(Content, ContentAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Template, TemplateAdmin)