
import util
from django.contrib.comments.models import Comment

def content_common(request):
    return {
		'friends': util.get_friend_list(),
		'recent_comments' : Comment.objects.order_by("-submit_date")[:5]
    }
