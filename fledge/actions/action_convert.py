#!/usr/bin/env python
# -*- coding: utf-8 -*-

# convert
def action_convert(controller, parameters):
    """
  Converts the selected image files to the specified format.

    convert to jpg
    convert to png
    """

    from PIL import Image
    import os

    # convert to png
    # convert to jpg

    pred = parameters.split(' ')
    format = pred[1].lower()

    new_files = []

    for file in controller.files:
        # Open the image
        img = Image.open(file)

        # New filename
        new_filename = os.path.splitext(file)[0] + '.' + format

        # Save it to the new filename
        img.save(new_filename, quality=95)

        # Push the new filename to the new list
        new_files.append(new_filename)

    controller.files = new_files
