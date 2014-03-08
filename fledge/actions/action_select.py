#!/usr/bin/env python
# -*- coding: utf-8 -*-

# select
def action_select(controller, parameters):
    """
  Adds specified files to the current selection.

    select *.gif
    select file01.png
    """

    if parameters.strip() == '':
        print 'Missing parameters. Usage:'
        print '  select [files]'
        return

    # Add file(s) to selection
    file_list = controller.glob_path(controller.expand_path(parameters))

    for f in file_list:
        if f not in controller.files:
            controller.files.append(f)
