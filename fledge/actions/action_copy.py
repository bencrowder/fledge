#!/usr/bin/env python
# -*- coding: utf-8 -*-

# copy
def action_copy(controller, parameters):
    """
  Copies the selected files.

    copy to ~
    copy to /usr/share/foobar
    """

    # copy to [path]

    # Get "to" out of predicate
    pred = parameters.split(' ')
    target = pred[1]
    target_dir = os.path.expanduser(target)

    new_files = []

    for file in controller.files:
        # Copy the file
        shutil.copy(file, target_dir)

        # New filename
        new_filename = os.path.abspath(target_dir) + '/' + os.path.basename(file)

        # Push the new filename to the new list
        new_files.append(new_filename)

    controller.files = new_files

