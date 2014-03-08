#!/usr/bin/env python
# -*- coding: utf-8 -*-

# trim
def action_trim(controller, parameters):
    """
  Trims any spaces from the edges of the file.

    trim
    """

    # For each file, load the contents, trim it, then save the file
    for file in controller.files:
        with open(file, 'r') as f:
            contents = f.read()
            contents = contents.strip()

        with open(file, 'w') as f:
            f.write(contents)
