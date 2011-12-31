import os
from tagging.managers import ModelTaggedItemManager
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.defaultfilters import slugify
from tagging.models import Tag, TaggedItem
import context_processors as cp
import util
from settings import PHOTOS_ZIP_PATH, PHOTOS_ZIP_URL
from friends.models import Friend

def friend_list(request):
  friends = Friend.objects.filter(active=True).order_by("name")
  print "Friends..."
  print friends
  print "End friends"
  section = "friends"
  return render_to_response('friends/friend_list.html', locals(),
    context_instance=RequestContext(request, processors=[]))

def runner(request):
  return render_to_response('friends/runner.html', locals(),
          context_instance=RequestContext(request, processors=[]))
