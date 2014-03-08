#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# split
def action_split(controller, parameters):
    """
  Splits selected file on a regex.

    split on /Chapter \d+/ to chapter-%%.text
    split on /PART [IVXLCM]+/ to part-%%%.text starting with 5
    """

    if parameters.strip() == '':
        print 'Missing parameters. Usage:'
        print '  split on /[pattern]/ to [filenamespec]'
        return

    import re

    # For each file, load the contents, trim it, then save the file
    for file in controller.files:
        with open(file, 'r') as f:
            contents = f.read()
            contents = contents.strip()

        with open(file, 'w') as f:
            f.write(contents)

    # Parse the parameters
    # TODO: make this elegant
    m = re.match("on /(.+?)(?!<\\\)/ to ((.+)( starting with (\d+))|(.+))", parameters) 
    pattern = m.groups()[0]
    if m.groups()[4] != None:
        # We have a "starting with" clause
        filename_template = m.groups()[2]
        start_with = m.groups()[4]
    else:
        # We don't
        filename_template = m.groups()[1]
        start_with = None

    # Where to start with the numbering
    if start_with is not None:
        counter = int(start_with)
    else:
        counter = 1

    # Parse filename into counter template
    template = "%0" + str(filename_template.count('%')) + "d"

    # Start with a new selection
    new_files = []

    # For each file, load the contents, append the text, then save the file
    for file in controller.files:
        # Read contents
        with open(file, 'r') as f:
            contents = f.read()

        # Add null byte character before each split, based on regex
        # This way we can split on the null byte and keep the pattern text
        contents = re.sub("(" + pattern + ")", r"\x00\1", contents)

        # Split on regex
        split_contents = contents.split("\\x00")

        # Only split if there's actually something split
        if len(split_contents) > 1:
            # For each part
            for bit in split_contents:
                # Update output filename
                output = re.sub(r"%+", template, filename_template) % counter

                # Expand the output file path
                output = controller.expand_path(output)

                # Update counter
                counter += 1

                # Write output to a file
                with open(output, 'w') as f:
                    f.write(bit)

                # Add new file to selection
                new_files.append(output)

    controller.files = new_files
