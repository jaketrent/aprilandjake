import random
from django.core.paginator import Paginator, InvalidPage, EmptyPage
	
from friends.models import Friend
from content.models import Collection
	
def get_friend_list():
	return Friend.objects.filter(active=True).order_by("name")

def paginate(request, obj_list, num_per_page=10):
	paginator = Paginator(obj_list, num_per_page)
	try:
		page = int(request.GET.get('page', '1'))
	except ValueError:
		page = 1
	try:
		objects = paginator.page(page)
	except (EmptyPage, InvalidPage):
		objects = paginator.page(paginator.num_pages)
	return objects

