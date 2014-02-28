## Fledge

Fledge is a utility for processing files (mainly text and image files). A few examples will hopefully explain it better:

	with *.text
	split on /==%==/ to page-%%%.text starting with 1
	replace /==%==//
	trim

Or:

	with image*.jpg where width < 600
	print name, imagesize
	rotate 90
	resize 150w

Or:

	with **/*.png
	convert to jpg

And so on. Select files, then run one or more actions on that selection.


### Installation

1. Download the package.
2. `sudo python setup.py install`
3. Copy the `fl` script somewhere in your PATH (or add its location to your PATH).
4. `sudo pip install cmd2`
5. Install libjpeg if you don't already have it installed:
	1. `curl -O http://www.ijg.org/files/jpegsrc.v8c.tar.gz`
	2. `tar -xvzf jpegsrc.v8c.tar.gz`
	3. `cd jpeg-8c`
	4. `./configure`
	5. `make`
	6. `sudo make install`
6. OS X: Install [XQuartz](http://xquartz.macosforge.org/landing/) (for PIL).
7. Install [PIL](http://www.pythonware.com/products/pil/).
	1. Download the [source kit](http://effbot.org/downloads/Imaging-1.1.7.tar.gz)
	2. `tar -xvzf Imaging-1.1.7.tar.gz`
	3. `cd Imaging-1.1.7`
	4. OS X: Edit `setup.py` and at line 151 (after `add_directory(library_dirs, "/usr/local/lib")`) add the following two lines:
		1. `add_directory(library_dirs, "/opt/X11/lib")`
		2. `add_directory(include_dirs, "/opt/X11/include")`
	5. `python setup.py build`
	6. `sudo python setup.py install`


### Usage

You can use Fledge as an interactive shell or to execute `.fledge` scripts.

	$ fledge
	fledge> with *.text
	fledge> print name
	fledge> help

Or:

	$ fledge myscript.fledge


### Help

More help is coming, but within the Fledge shell you can type `help` to get an overview. You can also type `help [command]` for help about a specific command.
