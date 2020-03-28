import os
import sys
import cv2
import collections

import numpy as np
from PIL import Image, ImageDraw, ImageFont

from rtclasses import *

import rtfilesys as fs
import rtimaging as img
import rtconfig as cf
import rtprint as pr
import rtvidcap as cap

def create_contact_sheet(file_info):

	pr.print_(file_info.fullfilename, "start")

	cs_filename = file_info.fullfilename[:-len(file_info.extension)] + cf.contact_ext

	if cf.debug:
		pr.print_(cs_filename, "done", True)
		pr.print_("")
		return

	vid_attr = vid_attribute(file_info)
	
	# DO 360P DELETE HERE

	if (vid_attr.height < 400 and cf.remove_lowres):

	    vid_attr.vid_cap.release()
	    cv2.destroyAllWindows()

	    fs.delete_file(vid_attr.file_nfo.fullfilename)
	    pr.print_(cs_filename, f" del {vid_attr.height}p", True)
	    pr.print_("")
	    return

	header_height, thumb_height, template_image = img.create_image_template(file_info)
	thumbs = cap.capture_thumbnails(vid_attr)

	cf.thumb_height = thumb_height

	counter = 0
	thumbs_keys = list(thumbs.keys())
	# thumbnail_scale = (cf.thumb_height * 1.0) / thumbs[thumbs_keys[0]].shape[0]
	x_offset = cf.thumb_spacing
	y_offset = header_height

	for y in range (1, cf.thumbs_vertical_new + 1):

		for x in range(1, cf.thumbs_horizontal + 1):

			thumbnail = thumbs[thumbs_keys[counter]]
			thumbnail_scaled = cv2.resize(thumbnail, (cf.thumb_width, cf.thumb_height), interpolation = cv2.INTER_AREA)
			template_image[y_offset: y_offset + thumbnail_scaled.shape[0], x_offset: x_offset + thumbnail_scaled.shape[1]] = thumbnail_scaled		

			x_offset += cf.thumb_spacing + cf.thumb_width
			counter += 1

		x_offset = cf.thumb_spacing
		y_offset += (cf.thumb_height + cf.thumb_spacing)

	newdim = (
		int(template_image.shape[1] * 0.6),
		int(template_image.shape[0] * 0.6),
	)
	template_image = cv2.resize(template_image, newdim, interpolation = cv2.INTER_AREA)
	cv2.imwrite(cs_filename, template_image, [cv2.IMWRITE_PNG_COMPRESSION, 9])

	pr.print_(cs_filename, "done", True)
	pr.print_("")

def create_image_template(file_nfo):

	vid_attr = vid_attribute(file_nfo)

	thumb_height = int(round((vid_attr.height / (vid_attr.width * 1.0)) * cf.thumb_width))
	im_header = im_height = 0

	im_header += cf.thumb_spacing				# pad
	im_header += int(cf.text_font_size * 1.5)	# first line
	im_header += int(cf.text_font_size)			# second line
	im_header += int(cf.thumb_spacing / 2)		# pad
	im_height += ((thumb_height + cf.thumb_spacing) * cf.thumbs_vertical_new) + int(cf.thumb_spacing)	# all the thumbs

	im = Image.new('RGBA', (cf.width, im_header + im_height), cf.background_color)
	draw = ImageDraw.Draw(im)
	courier_font = ImageFont.truetype(os.path.join(cf.text_font), cf.text_font_size)

	draw_text = vid_attr.filename
	pos_x = pos_y = cf.thumb_spacing
	draw.text((pos_x, pos_y), draw_text, fill='black', font=courier_font)

	draw_text = "{0}, {1}x{2}, {3}fps, {4}".format(\
		vid_attr.size_string, \
		vid_attr.width, \
		vid_attr.height, \
		vid_attr.fps_string, \
		vid_attr.length_string)

	pos_y += int(cf.text_font_size * 1.5)
	draw.text((pos_x, pos_y), draw_text, fill='black', font=courier_font)

	return im_header, thumb_height, cv2.cvtColor(np.array(im), cv2.COLOR_BGRA2BGR)

def overlay_timecode_on_thumbnail(time_in_seconds, thumbnail):
	
	# get timecode image
	tc_img = timecode_image(time_in_seconds)

	# calculate timecode image size ratio to thumbnail
	resize_ratio = (thumbnail.shape[1] * 0.35) / tc_img.shape[1]

	# resize timecode image
	tc_img_sized = cv2.resize(tc_img, (0,0), fx=resize_ratio, fy=resize_ratio) 

	# flip both thumbnail and timecode image on x,y axis
	# no need to calculate timecode image offset to place on bottom right corner
	l_img = cv2.flip(thumbnail, -1)
	s_img = cv2.flip(tc_img_sized, -1)

	# overlay timecode image on thumbnail
	x_offset = y_offset = 0
	l_img[y_offset: s_img.shape[0], x_offset: s_img.shape[1]] = s_img

	# flip thumbnail again
	return cv2.flip(l_img, -1)

def timecode_image(seconds):

	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)

	timecode = "%02d:%02d:%02d" % (h, m, s)

	time_code_background_image = np.zeros((107, 500, 3), np.uint8)
	cv2.putText(time_code_background_image, timecode, (3, 90), cv2.FONT_HERSHEY_DUPLEX, 3.45, (255,255,255), 6, cv2.LINE_AA)
	return time_code_background_image 