#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rename
def action_rename(controller, parameters):
    """
  Renames the selected files.

    rename .jpg
    rename part-%%%.text starting with 5
    """

    if parameters.strip() == '':
        print 'Missing parameters. Usage:'
        print '  rename [spec]'
        return

    import re
    import os

    # rename .jpg
    # rename file-####.jpg
    # rename file-####.jpg starting with 5

    # First parse the parameters
    # TODO: allow spaces in filename
    pred = parameters.split(' ')
    target = pred[0]
    if len(pred) == 4:
        # starting with X
        start_with = int(pred[3])
    else:
        start_with = 1

    counter = start_with

    # Parse target into counter template
    if target.count('%') > 0:
        template = "%0" + str(target.count('%')) + "d"
    else:
        template = ''

    new_files = []

    for file in controller.files:
        # If we just have an extension (starts with period), rename
        if target[0] == '.':
            # TODO: What about dotfiles?
            new_filename = os.path.splitext(os.path.basename(file))[0] + target
        else:
            # Otherwise rename to new filename pattern
            new_filename = re.sub(r"%+", template, target) % counter
            counter += 1

        # Do the rename
        dest = os.path.split(file)[0] + '/' + new_filename
        os.rename(file, dest)

        # Push the new filename to the new list
        new_files.append(dest)

    controller.files = new_files
