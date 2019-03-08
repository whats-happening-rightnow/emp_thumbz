import os
import sys

import rtconfig as cf
import rtfunctions as fn
import rtprint as pr

if cf.debug: pr.print_("Debug mode is on\n\n")

# handle if folder path is passed in
if (len(sys.argv) > 1):
	in_path = str(sys.argv[1]).strip().replace('"', '')
	if os.path.isdir(sys.argv[1]):
		cf.reorg_paths = [in_path]
		pr.print_("Folder: " + in_path)
		resp = raw_input("Reorganize folder? (y/n): ")
		pr.print_("")
		cf.reorg = resp.strip().lower() == "y"
	else:
		pr.print_("Parameter not recognized as folder, exiting")
		sys.exit()

# delete unwanted files
for dir in cf.reorg_paths:

	pr.print_(dir)
	cf.working_dir = dir
	
	fn.delete_unwanted_files()

	if cf.reorg:
		fn.rename_move()
