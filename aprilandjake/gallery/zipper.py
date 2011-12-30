import os, zipfile, unicodedata
from settings import PHOTOS_DWNLD_URL, PHOTOS_ZIP_PATH

def zip_photos(album_slug):
	album_dir = unicodedata.normalize('NFKD',os.path.join(PHOTOS_DWNLD_URL, album_slug)).encode('ascii','ignore')
	photonames = []
	try:
		os.system('mkdir ' + album_slug)
		os.system('cp ' + album_dir + '/* ./' + album_slug + '/')
		for photo in os.listdir(album_dir):
			#photonames.append(unicodedata.normalize('NFKD',os.path.join(PHOTOS_DWNLD_URL,album_slug,photo)).encode('ascii','ignore'))
			photonames.append(unicodedata.normalize('NFKD','./' + album_slug + '/' + photo).encode('ascii','ignore'))
		zout = zipfile.ZipFile(unicodedata.normalize('NFKD',os.path.join(PHOTOS_ZIP_PATH, album_slug + ".zip")).encode('ascii','ignore'), "w")
		for p in photonames:
			zout.write(p)
		zout.close()
		os.system('rm -rf ./' + album_slug)
	except IOError:
		os.exit()


