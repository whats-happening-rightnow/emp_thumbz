import os

import rtconfig as cf
import rtprint as pr

def get_all_files(dir):
	walk = os.walk(dir)
	for folder in walk:
		for file in folder[2]:
			yield os.path.join(folder[0], file)

def get_all_subdir(dir):
	sub_dirs = [x[0] for x in os.walk(dir)]
	sub_dirs.sort(key=len, reverse=True)
	return sub_dirs[:-1]

def file_ext(file_path):
	filename, file_extension = os.path.splitext(file_path)
	return file_extension

def filename_only(file_path):
	filename, file_extension = os.path.splitext(file_path)
	return filename

def delete_file(file_path):
	if not cf.debug: 
		os.remove(file_path)
	pr.print_(file_path, 'del')

def move_file(src, dest):
    if not cf.debug: 
        os.rename(src, dest)

    pr.print_(src, 'move-frm')
    pr.print_(dest, 'move-to')
