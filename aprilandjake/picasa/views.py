from django.shortcuts import render_to_response
from django.utils.simplejson.encoder import JSONEncoder
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from picasa.models import Photo
from picasa.utils import parse_feeds

def get_random_photo_ajax(request):
    photo = Photo.objects.random()
    data = {'title': photo.title,
            'image': photo.image,
            'url': photo.url}

    return render_to_response('json.html',
                              {'json': JSONEncoder().encode(data)})

def refresh_photos(request):
    added = parse_feeds()
    request.user.message_set.create(message='%i Picasa photos have been added to your database' % added)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))
refresh_photos = staff_member_required(refresh_photos)