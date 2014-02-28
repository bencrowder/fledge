#!/usr/bin/env python
# -*- coding: utf-8 -*-

# append
def action_append(controller, parameters):
    """
  Appends the text to the selected files.

    append ---
    append \\n\\nMy footer
    """

    # For each file, load the contents, append the text, then save the file
    for file in self.files:
        with open(file, 'r') as f:
            contents = f.read()
            contents = contents + predicate.decode('string_escape')

        with open(file, 'w') as f:
            f.write(contents)
