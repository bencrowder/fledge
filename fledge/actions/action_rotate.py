#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rotate
def action_rotate(controller, parameters):
    """
  Rotates the selected image files.

    rotate 90
    rotate -45
    """

    # rotate 90
    # rotate -45

    for file in controller.files:
        # Open the image
        img = Image.open(file)

        # Rotate it
        img = img.rotate(float(predicate))

        # Save it
        img.save(file, quality=95)
