#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

# copy
def action_copy(controller, parameters):
    """
  Copies the selected files.

    copy to ~
    copy to /usr/share/foobar
    """

    if parameters.strip() == '':
        print 'Missing parameters. Usage:'
        print '  copy to [path]'
        return

    # copy to [path]

    # Get "to" out of parameters 
    pred = parameters.split(' ')
    target = pred[1]

    # Expand path (aliases, home dir)
    target_dir = controller.expand_path(target)

    new_files = []

    for file in controller.files:
        # Copy the file
        shutil.copy(file, target_dir)

        # New filename
        new_filename = os.path.abspath(target_dir) + '/' + os.path.basename(file)

        # Push the new filename to the new list
        new_files.append(new_filename)

    controller.files = new_files

