## Fledge

Fledge is a language/shell for processing files (mainly text and image files). A few examples will hopefully explain it better:

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

The `fl` script will get installed to `/usr/local/bin`. The installer will automatically create a `~/.fledge` directory, which you can delete if you don't want it.

1. Download the package.
2. `sudo python setup.py install`
3. `sudo pip install cmd2`
4. Install libjpeg if you don't already have it installed:
	1. `curl -O http://www.ijg.org/files/jpegsrc.v8c.tar.gz`
	2. `tar -xvzf jpegsrc.v8c.tar.gz`
	3. `cd jpeg-8c`
	4. `./configure`
	5. `make`
	6. `sudo make install`
5. OS X: Install [XQuartz](http://xquartz.macosforge.org/landing/) (for PIL).
6. Install [PIL](http://www.pythonware.com/products/pil/).
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

	$ fl
	fl> with *.text
	fl> print name
	fl> help

Or:

	$ fl myscript.fledge


### Help

More help is coming, but within the Fledge shell you can type `help` to get an overview. You can also type `help [action]` for help about a specific action.


### Built-in actions

- `alias`: Set an alias for an action or a path
- `aliases`: List aliases
- `append`: Append text to the selected text files
- `convert`: Convert the selected files to another format
- `copy`: Copy the selected files to a new directory
- `deselect`: Deselect files from the current selection
- `flip`: Flip the selected image files
- `move`: Move the selected files to a new directory
- `prepend`: Prepend text to the selected text files
- `print`: Print attributes (name, size, etc.) about the selected files
- `rename`: Rename the selected files sequentially
- `replace`: Find-and-replace on the selected text files using regular expressions
- `resize`: Resize the selected image files
- `rotate`: Rotate the selected image files
- `select`: Add files to the current selection
- `split`: Split the selected text files into multiple files based on a regular expression
- `trim`: Trim whitespace off the beginning and end of the selected text files
- `with`: Start a new selection


### Customization

User customizations live in the `~/.fledge` directory. If you have put Fledge commands in `~/.fledge/fledgerc`, they will be run before anything else (mostly useful for setting up commonly used aliases).

Custom actions can be added to the `~/.fledge/actions` directory, and you can look at the [built-in actions](https://github.com/bencrowder/fledge/tree/master/fledge/actions) to see how they're constructed. (Custom action files look exactly the same.)
