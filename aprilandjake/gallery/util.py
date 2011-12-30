from django.conf import settings
import os
from django.template.defaultfilters import slugify

from gallery.models import Gallery

def create_gallery_xml(gallery):
	file = open(os.path.join(settings.MEDIA_ROOT, settings.PHOTOS_XML_PATH, slugify(gallery.album.title) + ".xml"),"w")
	file.write("""<gallery 
				   rows="3" 
				   cols="4" 
				   stage_width="975" 
				   stage_height="650" 
				   galleryMargin="10" 
				   thumb_width="130" 
				   thumb_height="130" 
				   thumb_space="20" 
				   thumbs_x="auto" 
				   thumbs_y="auto" 
				   large_x="auto" 
				   large_y="auto" 
				   nav_x="0" 
				   nav_y="15" 
				   nav_slider_alpha="50" 
				   nav_padding="7" 
				   use_flash_fonts="false" 
				   nav_text_size="21" 
				   nav_text_bold="false" 
				   nav_font="Verdana" 
				   bg_alpha="0" 
				   text_bg_alpha="50" 
				   text_xoffset="20" 
				   text_yoffset="10" 
				   text_size="11" 
				   text_bold="false" 
				   text_font="Verdana" 
				   link_xoffset="-2" 
				   link_yoffset="5" 
				   link_text_size="11" 
				   link_text_bold="false" 
				   link_font="Verdana" 
				   border="5" 
				   corner_radius="5" 
				   shadow_alpha="40" 
				   shadow_offset="2" 
				   shadow_size="5" 
				   shadow_spread="0" 
				   friction=".3" 
				   bg_color="ffffff" 
				   border_color="000000" 
				   thumb_bg_color="FFFFFF" 
				   nav_color="000000"
				   nav_slider_color="999999" 
				   txt_color="000000" 
				   text_bg_color="ffffff" 
				   link_text_color="000000"
				   link_text_over_color="475B8F" 
				   auto_size="true" 
				   showHideCaption="true" 
				   autoShowFirst="false" 
				   disableThumbOnOpen="false">
	    """)
	for photo in gallery.album.photo_set.all():
		pic = '<pic image="%s" title="%s" link="%s" link_title="%s"/>\n' % (photo.image.replace("s288", "s800"), photo.title, photo.url, photo.title)
		file.write(pic)
	file.write('</gallery>')
	file.close()
	gallery.xml_link = os.path.join(settings.PHOTOS_XML_URL, slugify(gallery.album.title) + ".xml")
	gallery.save()
