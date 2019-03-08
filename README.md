
# emp_thumbz
### What is it?
It makes a contact sheet for all video files in a given folder if one doesn't exist.

It's written in Python so it should run in all OS (Windows, Mac, Linux).

### How's it work?

You set a bunch of settings in a configuration file, then it runs like this:

![](https://i.imgur.com/xdwklzx.jpg)

Then you get this:

![](https://i.imgur.com/clzZE5D.jpg)

It'll find video files in subfolders, so a contact sheet will be made for all videos files in an folder tree.

But due to my lack of know-how in python packaging, there is a good amount of setting up first, a lot of it in command prompt (cmd) / terminal.

Still up for it?  Detailed setup instructions are below...

### Setup for Windows
**Step 1 - Install Python**

Assuming python is not installed, go and install python 2.7.

Current version is 3.7, but this app was written in 2.7.  I have not tested this app in 3.7.

https://www.python.org/downloads/release/python-2716/

Select the appropriate installer, you'll mostly likely use [64bit msi](https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi).

Just use the default installation options, but be sure to include PIP and make sure python in added to Windows PATH.

Verify python is installed by opening command prompt, and type `python --version`: 

![](https://i.imgur.com/tgQH4vT.png)

And verify that PIP is installed for python by typing `python -m pip --version`:

![](https://i.imgur.com/17yxBcR.png)

PIP will be needed to install all of the packages required for this app.

**Step 2 - Get emp_thumbz source code**

Grab source code from github page: https://github.com/whats-happening-rightnow/emp_thumbz

Download zip and unpack to a folder of your choice (or `git clone` if you're able):

![](https://i.imgur.com/oLiIDQC.png)

**Step 2 - Set emp_thumbz settings**

Open config file `rtconfig.py` in your favorite text editor (recommend notepad++ with python syntax highlighting).

The only setting you'll need to update is `thumb_paths`.  Get everything working before messing around with the other settings.

![](https://i.imgur.com/Prnioyb.png)

`thumb_paths` : 
folder where your video files are located; specify multiple folders by separating with a comma

`video_ext` :
video file extension, comma separated, all formats should be already be covered

`contact_ext` :
contact sheet image format

`width` : 
contact sheet width

`thumbs_horizontal` : 
number of columns in contact sheet

`thumbs_vertical` : 
number of rows in contact sheet

`video_pad` :
percentage of video taken off the beginning and end of the video

`background_color` :
rgb value of the contact sheet background color

`text_font` :
header text font, set to courier new

`text_font_size` : 
header text font size in pixels

`thumb_spacing` :
gap in between each thumbnail image in pixels

`thumb_width` :
leave this one alone, it dynamically calculates each thumbnail image size

`thumb_height` :
don't remember what this is used for, leave it alone

`exclude_postfix` :
this is an unused setting but dependent anyway, leave it alone

**Step 3 - Install app dependencies**

Ignore the warning as modules are installed.  Definitely do not update PIP as it's recommended, it'll cause some problems since this is on python 2.7:

![](https://i.imgur.com/ATpfqaT.png)

In command prompt (cmd), navigate to where you unzipped the app files, and type in these commands (one at a time):

`python -m pip install numpy`

`python -m pip install opencv-python`

`python -m pip install Pillow`

**Step 4 - Run it!**

In command prompt (cmd), navigate to where you unzipped the app files, and type in this command to run the app:

`python thumbs.py`

It should looks like this:

![](https://i.imgur.com/Gcjn23J.png)

And contact sheets should be in the same location as the video files.
