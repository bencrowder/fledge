#!/usr/bin/env python
# -*- coding: utf-8 -*-

# with
def action_with(controller, parameters):
    """
  Starts a new selection.

    with *.jpg
    with *.text where size > 10000
    with *.jpg where width < 500 and height < 500
    with *.text where content matches /myregex/
    """

    if ' where ' in parameters:
        # Get the path and filters
        path, controller.filters = parameters.split(' where ')

        # Allow for multiple filters
        controller.filters = controller.filters.split(' and ')
    else:
        path = parameters
        controller.filters = []

    # Expand the path if there are aliases
    path = controller.expand_path(path)

    # Glob the files
    controller.files = controller.glob_path(path)

    # Apply any filters
    controller.apply_filters()
