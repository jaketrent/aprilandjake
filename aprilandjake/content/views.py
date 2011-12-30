import os
from tagging.managers import ModelTaggedItemManager
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from tagging.models import Tag, TaggedItem
from django.contrib.comments.models import Comment
import context_processors as cp
import util
from settings import PHOTOS_ZIP_PATH, PHOTOS_ZIP_URL
from content.models import Content
from django.http import HttpResponsePermanentRedirect

def search_results(request):
	return render_to_response('content/search_results.html', locals(),
		context_instance=RequestContext(request, processors=[]))

def content_list(request):
	content = util.paginate(request, Content.objects.filter(active=True).exclude(collection__title_slug="tech").order_by("-date_published"))
	section = "blog"
	return render_to_response('base.html', locals(),
		context_instance=RequestContext(request, processors=[]))

def home(request):
  section = "blog"
  content = util.paginate(request, Content.objects.filter(active=True).exclude(collection__title_slug="tech").order_by("-date_published"))
  return render_to_response('base.html', locals(),
		context_instance=RequestContext(request, processors=[]))
	
def content_list_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)    
    content = util.paginate(request, TaggedItem.objects.get_by_model(Content, tag).order_by("-date_published"))
    return render_to_response('content/content_list_tag.html', locals(),
		context_instance=RequestContext(request, processors=[]))

def tag_list(request):
	section = "tags"
	return render_to_response('content/tag_list.html', locals(),
		context_instance=RequestContext(request, processors=[]))

def friend_list(request):
	section = "friends"
	return render_to_response("friends/friend_list.html", locals(),
		context_instance=RequestContext(request, processors=[]))

def content_detail(request, slug):
  section="blog"
  content = get_object_or_404(Content, active=True, title_slug=slug)
  if (content and content.collection.title_slug == "tech"):
    return HttpResponsePermanentRedirect('http://rockycode.com/blog/' + slug)
  else:
    return render_to_response('content/content_detail.html', locals(),
      context_instance=RequestContext(request, processors=[]))

def content_collection(request, slug, section):
  content = util.paginate(request, Content.objects.filter(active=True, collection__title_slug=slug).order_by("-date_published"))
  return render_to_response('base.html', locals(),
    context_instance=RequestContext(request, processors=[]))

def content_podcast(request):
  return content_collection(request, "podcast", "blog")

def content_blog(request):
  return content_collection(request, "blog", "blog")

def content_quotes(request):
  return content_collection(request, "quotes", "blog")

def content_photos(request):
  return content_collection(request, "photos", "blog")

def content_comments(request, slug):
  content = get_object_or_404(Content, active=True, title_slug=slug)
  comments = Comment.objects.filter(object = content)
  return

def all_comments(request):
  all_comments = Comment.objects.order_by("-submit_date")
  #most_commented = Content().get_most_commented()
  return render_to_response('content/comments.html', locals(),
  context_instance=RequestContext(request, processors=[cp.content_common]))

def comment_posted(request):
  if request.GET['c']:
    comment_id = request.GET['c']
    content_id = Comment.objects.get(pk=comment_id).object_pk
    post = Content.objects.get(pk=content_id)
    if post:
      return HttpResponseRedirect(post.get_absolute_url())
  return HttpResponseRedirect("/")