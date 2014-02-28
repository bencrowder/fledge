#!/usr/bin/env python
# -*- coding: utf-8 -*-

# deselect
def action_deselect(controller, parameters):
    """
Removes specified files from the current selection.

  deselect *.pcx
  deselect file02.png
    """

    # Remove file(s) from selection
    file_list = controller.glob_path(controller.expand_path(parameters))
    controller.files = [f for f in controller.files if f not in file_list]
