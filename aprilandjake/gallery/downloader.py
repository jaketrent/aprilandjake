from urllib import urlopen
import os, sys
from getopt import getopt
from django.template.defaultfilters import slugify
from settings import PHOTOS_DWNLD_URL

def downloadPicasaAlbum(album):
	urls = []
	album_slug = slugify(album.title)
	for p in album.photo_set.all():
		#p.image[0:p.image.find('s288')] + p.image[p.image.find('s288')+5:]
		#urls.append(p.image[0:p.image.find('s288')] + p.image[p.image.find('s288')+5:])
		urls.append(p.image.replace('s288/',''))
	downloadUrls(album_slug, urls)	

def getURLName(url):
	directory=os.curdir

	name="%s%s%s" % (
		directory,
		os.sep,
		url.split("/")[-1]
	)

	return name

def createDownload(url, proxy=None):
	instream=urlopen(url, None, proxy)

	filename=instream.info().getheader("Content-Length")
	if filename==None:
		filename="temp"

	return (instream, filename)

def download(instream, outstream):
	outstream.write(instream.read())

	outstream.close()

def downloadUrls(album_slug, urls, downloaddir = PHOTOS_DWNLD_URL):
	systemArgs=sys.argv[1:] # ignore program name

	proxies={}

	optlist=[]
	args=[]

	# make album dir if not exist
	if not os.path.isdir(os.path.join(downloaddir, album_slug)):
		os.mkdir(os.path.join(downloaddir, album_slug))

	for url in urls:
		try:
			outfile=open(os.path.join(downloaddir, album_slug, getURLName(url)), "wb")
			#path of where file will be saved
			#outfile=open(getURLName(url), "wb")
			fileName=os.path.join(downloaddir, album_slug, getURLName(url))#outfile.name.split(os.sep)[-1]

			url, length=createDownload(url, proxies)
			if not length:
				length="?"

			# TODO: remove print's
			#print "Downloading %s (%s bytes) ..." % (url.url, length)
			#if length!="?":
			#		length=float(length)
			#bytesRead=0.0

			for line in url:
				#bytesRead+=len(line)

				#if length!="?":
					#print "%s: %.02f/%.02f kb (%d%%)" % (
						#fileName,
						#bytesRead/1024.0,
						#length/1024.0,
						#100*bytesRead/length
					#)

				outfile.write(line)

			url.close()
			outfile.close()
			#print "Done"

		except Exception, e:
			print "Error downloading %s: %s" % (url, e)
"""
if __name__=="__main__":
	main()
"""