from django.contrib.syndication.feeds import Feed
from django.contrib.sites.models import Site

from content.models import Content

class AllBlog(Feed):
  title = "AprilandJake.com Blog"
  link = 	"http://%s/blog/" % (Site.objects.get_current().domain)
  description = "April and Jake's blog entries."
  def items(self):
    return Content.objects.filter(active=True, collection__title_slug="blog").exclude(collection__title_slug="tech").order_by("-date_published")

  def item_title(self, item):
    return item.title

  def item_description(self, item):
    return item.summary

  def item_pubdate(self, item):
    return item.date_published


