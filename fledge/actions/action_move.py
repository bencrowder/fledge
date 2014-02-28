#!/usr/bin/env python
# -*- coding: utf-8 -*-

# move
def action_move(controller, parameters):
    """
  Moves the selected files.

    move to ~
    move to /usr/share/foobar
    """

    # move to [path]

    # Get "to" out of predicate
    pred = parameters.split(' ')
    target = pred[1]
    target_dir = os.path.expanduser(target)

    new_files = []

    for file in controller.files:
        # Move the file
        shutil.copy2(file, target_dir)
        os.remove(file)

        # New filename
        new_filename = os.path.abspath(target_dir) + '/' + os.path.basename(file)

        # Push the new filename to the new list
        new_files.append(new_filename)

    controller.files = new_files
