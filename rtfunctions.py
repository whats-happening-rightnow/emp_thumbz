import os
import shutil
import sys

import rtconfig as cf
import rtfilesys as fs
import rtfunctions as fn
import rtprint as pr
from rtclasses import *

def rename_move():

	# rename video file name and move to parent
	allfiles = list(fs.get_all_files(cf.working_dir))

	# move video files to working folder root
	for file in allfiles:

		# object to parse out file path parts
		fileinfo = file_info(file, cf.working_dir)

		# skip file is not video or marked for omit reorg
		if (fileinfo.extension not in cf.video_ext) \
			or fileinfo.isatroot \
			or fileinfo.excludefilereorg: continue

		# unique counter 
		iterator = 0
		newfilename = os.path.join(fileinfo.rootfolder, fileinfo.parentfoldername) \
			+ fileinfo.extension

		# make filename unique if exists in destination
		while os.path.isfile(newfilename):
			newfilename = os.path.join(fileinfo.rootfolder, fileinfo.parentfoldername) + "-" + \
				("%02d" % (iterator,)) + fileinfo.extension
			iterator += 1

		# move / rename file to parent root dir
		pr.print_(fileinfo.fullfilename)
		pr.print_(newfilename)
		fs.move_file(fileinfo.fullfilename, newfilename)
	
	# delete subdirs
	all_sub_dirs = fs.get_all_subdir(cf.working_dir)
	for dir in all_sub_dirs: 
		if len(list(fs.get_all_files(dir))) == 0:
			delete_folder(dir)
		#else:
		#	pr.print_(dir, "skip")

	## get first level subdirs
	#subdirs_first_level = next(os.walk(cf.working_dir))[1]

	## delete dir is not omit reorg
	#for dir in subdirs_first_level: 
	#	all_sub_dirs = fs.get_all_subdir(dir)
	#	if len(all_sub_dirs) == 0:
	#		delete_folder(dir)
	#	else:
	#		pr.print_(dir, "delskip")

def delete_folder(dir):
	if not exclude_in_file_reorg(dir):
		pr.print_(dir, "deltree")
		if not cf.debug:
			shutil.rmtree(dir)
	#else:
	#	pr.print_(dir, "delskip")

def delete_unwanted_files():

	allfiles = list(fs.get_all_files(cf.working_dir))

	# delete unwanted files
	for file in allfiles:
	
		fileinfo = file_info(file, cf.working_dir)
		
		# skip is exclude pattern found
		if fileinfo.excludefilereorg: 
			#pr.print_(fileinfo.fullfilename, "delskip")
			continue

		# if contact sheet
		if (fileinfo.extension == cf.contact_ext):
			# make sure matching video file exists
			if not corresponding_video_file_exists(fs.filename_only(file), allfiles):
				# if no matching video file, delete
				fs.delete_file(file)
		# if is not contact sheet or video file, delete
		elif (fileinfo.extension not in cf.video_ext) or ('sample' in fileinfo.filename.lower()):
			fs.delete_file(file)

def corresponding_video_file_exists(cs_fn, all_files):

	for ext in cf.video_ext:
		if (cs_fn + ext) in all_files:
			return True

	return False

def corresponding_contact_sheet_exists(video_fullfilename, all_files):

	video_cs_filename = fs.filename_only(video_fullfilename) + cf.contact_ext

	if video_cs_filename in all_files:
		return True

	return False

def exclude_in_file_reorg(vid_fn):

	trunc_path = str(vid_fn).replace(cf.working_dir, "")

	fullpath = trunc_path.split(os.sep)

	for item in fullpath:
		if item.endswith(cf.exclude_postfix):
			return True

	return False
