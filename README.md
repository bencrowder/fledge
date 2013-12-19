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

- Coming soon.
