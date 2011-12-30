from django.contrib.sitemaps import Sitemap
from content.models import Content

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
    # todo: location() uses /absolute/path w/o http:// protocol -- adj get_absolute_url()?

    def items(self):
        return Content.objects.filter(active=True).exclude(collection__title_slug="tech")

    def lastmod(self, obj):
        return obj.date_updated

