#!/usr/bin/env python
# -*- coding: utf-8 -*-

# resize
def action_resize(controller, parameters):
    """
  Resizes the selected image files.

    resize 640x480
    resize 1000w
    resize 1000
    resize 75h
    """

    if parameters.strip() == '':
        print 'Missing parameters. Usage:'
        print '  resize [size]'
        return

    from PIL import Image

    # resize 640x480
    # resize 1000w
    # resize 500h

    w = 0
    h = 0

    # Parse the size into width/height
    if 'x' in parameters:
        w = int(parameters.split('x')[0])
        h = int(parameters.split('x')[1])
    else:
        if parameters[-1] == 'h':
            h = int(parameters[:-1])
        else:
            if parameters[-1] == 'w':
                # If it ends with 'w'
                w = int(parameters[:-1])
            else:
                # If it's just a number, it's a width
                w = int(parameters)

    for file in controller.files:
        # Open the image
        img = Image.open(file)

        file_w, file_h = img.size

        if w == 0:
            # Proportional to height
            width = int(round((float(h) / file_h) * file_w))
        else:
            width = w

        if h == 0:
            # Proportional to width
            height = int(round((float(w) / file_w) * file_h))
        else:
            height = h

        # Resize it
        img = img.resize((width, height), Image.ANTIALIAS)

        # Save it
        img.save(file, quality=95)
