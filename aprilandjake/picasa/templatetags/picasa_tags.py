from django import template
from picasa.models import *

register = template.Library()

def random_picasa_photo():
    try:
        return {'photo': Photo.objects.random()}
    except:
        return {'photo': None}
register.inclusion_tag('picasa/_random_picasa_photo.html')(random_picasa_photo)

