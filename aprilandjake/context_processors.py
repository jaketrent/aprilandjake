
import util

def content_common(request):
    return {
		'friends': util.get_friend_list()
    }
