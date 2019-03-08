# add . to extension if not exists
def add_period_ifnot_exists(ext):
    return ext.lower() if str(ext).startswith('.') else "." + ext.lower()

# thumbs config
thumb_paths = [r'C:\emp_thumbz\vids', r'C:\emp_thumbz\vids_another_folder']
video_ext = [".mkv", ".flv", ".avi", ".mov", ".wmv", ".mp4", ".mpg", ".mpeg", ".m2v", "m4v", "ts"]
contact_ext = ".png"
width = 2500
thumbs_horizontal = 7
thumbs_vertical = 6
video_pad = 0.05
background_color = (244, 66, 232)
text_font = "courbd.ttf"
text_font_size = 25
thumb_spacing = 3
thumb_width = int(round((width * 1.0 - ((thumbs_horizontal * thumb_spacing) + thumb_spacing)) / thumbs_horizontal))
thumb_height = 0
exclude_postfix = "-zz"

# global
out_message = []
working_dir = ''

# test reorg and thumb create results
debug = False

# reorg config
# reorg_paths = [r'']
# reorg = True

# add . to extension if not exists
for ii in range(0, len(video_ext)):
    video_ext[ii] = add_period_ifnot_exists(video_ext[ii])

contact_ext = add_period_ifnot_exists(contact_ext)
