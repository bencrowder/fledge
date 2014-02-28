#!/usr/bin/env python
# -*- coding: utf-8 -*-

# replace
def action_replace(controller, parameters):
    """
  Replaces text using a regex.

    replace /pattern/replacement/
    replace /Chapter (\d+)/CHAPTER \\1.0/
    """

    # Get the pattern and replacement
    m = re.match(r"/(.*)(?<!\\)/(.*)/$", parameters)
    pattern, replacement = m.groups()

    # Replace any escaped slashes
    replacement = replacement.replace('\/', '/')

    # For each file, load the contents, run the regex, then save the file
    for file in controller.files:
        with open(file, 'r') as f:
            contents = f.read()
            contents = re.sub(pattern, replacement, contents)

        with open(file, 'w') as f:
            f.write(contents)

