#!/usr/bin/env python
# -*- coding: utf-8 -*-

# flip
def action_flip(controller, parameters):
    """
  Flips the selected image files.

    flip h
    flip v
    """

    # flip h
    # flip v

    if parameters == 'h':
        method = Image.FLIP_LEFT_RIGHT
    elif parameters == 'v':
        method = Image.FLIP_TOP_BOTTOM

    for file in controller.files:
        # Open the image
        img = Image.open(file)

        # Flip it
        img = img.transpose(method)

        # Save it
        img.save(file, quality=95)
