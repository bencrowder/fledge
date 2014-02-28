#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# print
def action_print(controller, parameters):
    """
  Prints out information for each file in the current selection.

    print name
    print name, size, width, height
    print fullpath
    """

    # Break up the predicate
    attributes = [p.strip() for p in parameters.split(',')]

    # Loop through everything we want
    for f in controller.files:
        line = []

        for attribute in attributes:
            # Print attributes
            if attribute == 'name' or attribute == 'filename' or attribute == '':
                line.append(os.path.relpath(f, os.getcwd()))
            elif attribute == 'fullpath':
                line.append(f)
            elif attribute == 'size':
                # File size
                size = os.path.getsize(f)
                line.append(str(size))
            elif attribute == 'width':
                # Image width
                img = Image.open(f)
                line.append(str(img.size[0]))
            elif attribute == 'height':
                # Image height
                img = Image.open(f)
                line.append(str(img.size[1]))
            elif attribute == 'imagesize':
                # Image width x height
                img = Image.open(f)
                line.append('%sx%s' % (img.size[0], img.size[1]))

        print ' | '.join(line)
