#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rotate
def action_rotate(controller, parameters):
    """
  Rotates the selected image files.

    rotate 90
    rotate -45
    """

    if parameters.strip() == '':
        print 'Missing parameters. Usage:'
        print '  rotate [degrees]'
        return

    from PIL import Image

    # rotate 90
    # rotate -45

    for file in controller.files:
        # Open the image
        img = Image.open(file)

        # Rotate it
        img = img.rotate(float(parameters))

        # Save it
        img.save(file, quality=95)
