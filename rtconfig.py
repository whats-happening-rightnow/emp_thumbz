# add . to extension if not exists
def add_period_ifnot_exists(ext):
    return ext.lower() if str(ext).startswith('.') else "." + ext.lower()

# reorg config
# reorg_paths = [r'\\99.1.1.10\q$\__',r'\\99.1.1.10\q$\00\tg\_etc',r'\\99.1.1.10\q$\an',r'\\99.1.1.10\q$\ff',r'\\jfs\vid\mov_4k',r'\\jfs\vid\mov_3d',r'\\jfs\vid\race\Formula1',r'\\jfs\vid\race\MotoGP']
reorg_paths = [r'\\99.1.1.10\q$\ff',r'\\99.1.1.10\q$\__',r'\\99.1.1.10\q$\00\tg\_etc',r'\\99.1.1.10\q$\an',r'\\jfs\vid\mov_4k',r'\\jfs\vid\mov_3d',r'\\jfs\vid\race\Formula1',r'\\jfs\vid\race\MotoGP']
video_ext = [".mkv", ".flv", ".avi", ".mov", ".wmv", ".mp4", ".mpg", ".mpeg", ".m2v", "m4v", "ts", "webm"]
contact_ext = ".png"
exclude_postfix = "-zz"
reorg = True

# thumbs config
thumb_paths = [r'\\99.1.1.10\q$\__',r'\\99.1.1.10\q$\00\tg',r'\\99.1.1.10\q$\an',r'\\99.1.1.10\q$\zz-split\done',r'\\jfs\a\nzbg\pnew',r'\\99.1.1.10\q$\ff']
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
remove_lowres = True

# global
out_message = []
working_dir = ''

# test reorg and thumb create results
debug = False

# add . to extension if not exists
for ii in range(0, len(video_ext)):
    video_ext[ii] = add_period_ifnot_exists(video_ext[ii])

contact_ext = add_period_ifnot_exists(contact_ext)
