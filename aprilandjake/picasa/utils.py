try:
    from xml.etree.ElementTree import fromstring, tostring
except ImportError:
    from elementtree.ElementTree import fromstring, tostring
from django.conf import settings
from picasa.models import *
import urllib2, re, random
import datetime, time

try:
    PICASA_USERS = settings.PICASA_USERS
except:
    raise ValueError('Please define PICASA_USERS in settings.py')

PICASA_THUMBSIZE = getattr(settings, 'PICASA_THUMBSIZE', None)

def parse_feeds():
    """
    Returns a dictionary of photos from Picasa Web.  This dictionary is formatted
    with the URL to the photo (on Picasa Web) as the key, and the URL to the
    photo's thumbnail as the value associated with the key.
    """

    count = 0

    for user in PICASA_USERS:
        print 'Pulling in photos for %s...' % user

        album_url = 'http://picasaweb.google.com/data/feed/base/user/%s?kind=album&alt=rss&hl=en_US&access=public' % user

        raw_data = urllib2.urlopen(urllib2.Request(url=album_url)).read()
        media_ns = re.findall("xmlns:media='(.*?)'", raw_data)[0]
        tree = fromstring(raw_data)

        print 'Album:',

        for album in tree.getiterator('item'):
            title = album.find('.//title/').text
            url = re.findall('href="(.*?)"', album.find('.//description/').text)[0]

            print '%s,' % title,

            try:
                a = Album.objects.create(title=title, url=url)
            except:
                # do not duplicate albums
                pass
            else:
                album_feed = album.find('.//guid/').text.replace('data/entry/base', 'data/feed/base') + '&kind=photo'
                if PICASA_THUMBSIZE: album_feed += '&thumbsize=' + PICASA_THUMBSIZE

                try:
                    all_photos = fromstring(urllib2.urlopen(urllib2.Request(url=album_feed)).read())
                except urllib2.URLError:
                    pass
                else:
                    for photo in all_photos.getiterator('item'):
                        title = photo.find('.//title/').text
                        description = photo.find('.//description/').text

                        if PICASA_THUMBSIZE:
                            url, extra = re.findall('href="(.*?)"><img(.*?)src=', description)[0]
                            img = photo.find('.//{%s}thumbnail' % media_ns).attrib["url"]
                        else:
                            url, extra, img = re.findall('href="(.*?)"><img(.*?)src="(.*?)"', description)[0]
                        pubtime = time.strptime(photo.find('.//pubDate/').text,
                                                "%a, %d %b %Y %H:%M:%S +0000")
                        pubdate = datetime.datetime.fromtimestamp(time.mktime(pubtime))

                        try:
                            Photo.objects.create(album=a, title=title, image=img, url=url, pub_date=pubdate)
                            count += 1
                        except:
                            # do not duplicate photos
                            pass
        print

    return count