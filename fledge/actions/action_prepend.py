#!/usr/bin/env python
# -*- coding: utf-8 -*-

# prepend
def action_prepend(controller, parameters):
    """
  Prepends the text to the selected files.

    prepend ## Header
    prepend title: Foobar\\n\\nauthor: Me
    """

    # For each file, load the contents, prepend the text, then save the file
    for file in controller.files:
        with open(file, 'r') as f:
            contents = f.read()
            contents = parameters.decode('string_escape') + contents

        with open(file, 'w') as f:
            f.write(contents)
