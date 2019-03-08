import collections
import sys

import rtimaging as img
import rtprint as pr

def capture_thumbnails(vid_attr):

	# starting frame
	frame_counter = vid_attr.startframe

	thumbs_dict = {}
	success = True
	total_thumbs = vid_attr.totalthumbs + 1

	for ii in range(1, total_thumbs):

		# jump to frame, capture frame
		vid_attr.vid_cap.set(1, frame_counter)
		success, frame = vid_attr.vid_cap.read()

		if success:
			# overlay timecode
			thumbs_dict[frame_counter] = img.overlay_timecode_on_thumbnail(int(frame_counter / vid_attr.fps), frame)
			# move frame location forward
			frame_counter += vid_attr.frameinterval
			# print progress
			pr.print_progress(ii, vid_attr.totalthumbs)
		else:
			break

	# return dict in key ordered
	return collections.OrderedDict(sorted(thumbs_dict.items()))
