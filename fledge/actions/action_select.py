#!/usr/bin/env python
# -*- coding: utf-8 -*-

# select
def action_select(controller, parameters):
    """
  Adds specified files to the current selection.

    select *.gif
    select file01.png
    """

    # Add file(s) to selection
    file_list = self.glob_path(parameters)

    for f in file_list:
        if f not in self.files:
            controller.files.append(f)
