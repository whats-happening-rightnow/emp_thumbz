
import os
import math
import sys

import numpy as np
import cv2

import rtconfig as cf
import rtfilesys as fs
import rtfunctions as fn

class file_info:

	def __init__(self, fullpath, workingfolder):

		filename_arr = fullpath.split(os.sep)
				 
		self.rootfolder = workingfolder
		self.fullfilename = fullpath
		self.filename = filename_arr[-1]
		self.extension = fs.file_ext(fullpath); 
		self.folder = os.sep.join(filename_arr[:-1])
		self.excludefilereorg = fn.exclude_in_file_reorg(self.fullfilename)

		self.isatroot = self.rootfolder == self.folder;

		if self.isatroot: 
			return
		
		parent_arr = fullpath.replace(workingfolder, "").split(os.sep)
		
		if len(parent_arr) < 2: return

		self.parentfoldername = [s for s in parent_arr if len(s) > 0][0]
		
		workingfolderArr = [s for s in workingfolder.split(os.sep) if len(s) > 0]
		workingfolderArr.append(self.parentfoldername)

		self.parentfolderpath = os.sep.join(workingfolderArr)

class vid_attribute:

	def __init__(self, file_nfo):

		self.file_nfo = file_nfo
		self.vid_cap = cv2.VideoCapture(self.file_nfo.fullfilename)
		
		self.filename = self.file_nfo.fullfilename.split(os.sep)[-1]
		self.fps = self.vid_cap.get(cv2.CAP_PROP_FPS)
		self.fps_string = \
			str(math.floor(self.fps * 10 ** 1) / 10 ** 1) \
			if "." in str(self.fps) and ".0" not in str(self.fps) \
			else str(int(self.fps))
		self.frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.totalthumbs = cf.thumbs_horizontal * cf.thumbs_vertical
		self.frameinterval = int((self.frames * (1 - (cf.video_pad * 2))) / self.totalthumbs)
		self.height = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.length = int(self.frames / self.vid_cap.get(cv2.CAP_PROP_FPS))
		self.length_string = ""
		self.size = os.path.getsize(self.file_nfo.fullfilename)
		self.size_string = ""
		self.startframe = int(self.frames * cf.video_pad)
		self.width = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))

		# self.length_string
		m, s = divmod(self.length, 60)
		h, m = divmod(m, 60)

		if h > 0:
			self.length_string = "%02d:%02d:%02d" % (h, m, s)
		else:
			self.length_string = "%02d:%02d" % (m, s)

		# self.size_string
		# gt MB
		if self.size > 1073741824:
			self.size_string = "%.1fGB" % (self.size / 1073741824.0)
		# gt MB
		elif self.size > 1048576:
			self.size_string = "%dMB" % int(self.size / 1048576.0)
		else:
			self.size_string = "%dKB" % int(self.size / 1024.0)

