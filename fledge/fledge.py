#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import re
import time
import argparse
import shutil
from datetime import datetime
from PIL import Image
from cmd2 import Cmd
from pwd import getpwuid
from grp import getgrgid

class Fledge:
    files = []          # currently selected files
    filters = []        # where clauses on with statements
    lines = []

    aliases = {
        'actions': {},  # mv for move, etc.
        'paths': {},    # path shortcuts
    }

    # Initialize and load a file
    def __init__(self, filename=None):
        self.lines = []

        # Load ~/.fledge/fledgerc if it exists
        fledge_config_path = '%s/.fledge' % os.path.expanduser('~') 
        fledge_rc_path = '%s/fledgerc' % fledge_config_path
        if os.path.exists(fledge_rc_path):
            # Load the init file
            with open(fledge_rc_path, 'r') as f:
                self.lines = f.readlines()

            # And parse it
            self.parse()

        # Now load the file we've requested
        if filename:
            with open(filename, 'r') as f:
                self.lines = f.readlines()

    # Parse
    def parse(self, filename=None):
        # Load the file if specified
        if filename:
            with open(filename, 'r') as f:
                self.lines = f.readlines()

        # Parse each line
        for line in self.lines:
            if line.strip() != '':
                self.parse_line(line.strip())

    # Parse a line
    def parse_line(self, line):
        # Get the keyword
        tokens = line.split(' ')
        keyword = tokens[0]
        predicate = ' '.join(tokens[1:])

        # Check to see if keyword is an alias
        if keyword in self.aliases['actions']:
            keyword = self.aliases['actions'][keyword]

        # Import the action method
        name = 'action_%s' % keyword

        try:
            actions = __import__("fledge.actions.%s" % name, fromlist=[name])
            action = getattr(actions, name)
        except ImportError:
            print "Error importing that action"

        if action and callable(action):
            action(self, predicate)

    # Apply filters to a list of files
    def apply_filters(self):
        for filter_string in self.filters:
            # Parse the filter
            m = re.match(r"(.+?)\s*([><=!]+|matches)\s*(.+)", filter_string)
            keyword, operator, value = m.groups()

            # Function to handle the operator (<, >=, etc.)
            # TODO: some way to do this via metaprogramming?
            def apply_operator(operator, a, b):
                if operator == '<':
                    return a < b
                elif operator == '<=':
                    return a <= b
                elif operator == '>':
                    return a > b
                elif operator == '>=':
                    return a >= b
                elif operator == '==':
                    return a == b
                elif operator == '!=':
                    return a != b
                elif operator == 'matches':
                    return re.search(b, a)

            # Function to do the comparison
            def check_value(filename, keyword, operator, value):
                attribute = ''

                if keyword == 'size':
                    # File size
                    attribute = os.path.getsize(filename)

                    # Convert value to int so we can compare it
                    # TODO: allow things like 40K or 50M
                    value = int(value)

                elif keyword == 'lastmod':
                    # Last modified date
                    attribute = os.path.getmtime(filename)

                    # For dates, convert value to seconds as well
                    value = self.make_unix_date(value)

                elif keyword == 'width':
                    # Image width
                    img = Image.open(filename)
                    attribute = img.size[0]

                    # Convert value to integer
                    value = int(value)

                elif keyword == 'height':
                    # Image height
                    img = Image.open(filename)
                    attribute = img.size[1]

                    # Convert value to integer
                    value = int(value)

                elif keyword == 'wordcount':
                    # Word count (for text)
                    import subprocess
                    word_count_output = subprocess.check_output(['wc', filename])
                    attribute = int(re.sub(' +', ' ', word_count_output).strip().split(' ')[1])

                    # Convert value to integer
                    value = int(value)

                elif keyword == 'content':
                    # Content matches regex
                    f = open(filename, 'r')
                    attribute = f.read()

                    # Strip slashes off regex
                    value = value[1:-1]

                elif keyword == 'owner':
                    # Owner
                    attribute = getpwuid(os.stat(filename).st_uid).pw_name

                    # Strip slashes off regex if used
                    if value[0] == '/' and value[-1] == '/':
                        value = value[1:-1]

                elif keyword == 'group':
                    # Owner
                    attribute = getgrgid(os.stat(filename).st_gid).gr_name

                    # Strip slashes off regex if used
                    if value[0] == '/' and value[-1] == '/':
                        value = value[1:-1]

                return apply_operator(operator, attribute, value)

            # Use the built-in filter() function to, ahem, filter the list
            self.files = filter(lambda file: check_value(file, keyword, operator, value), self.files)

    # Globs a path and returns list of files therein
    def glob_path(self, path):
        files = []

        # Expand tilde if present
        path = os.path.expanduser(path)

        # Check for **/ in the path (indicates recursive from that point on)
        if '**/' in path:
            parts = path.split('**/')
            base = parts[0] or '.'
            pattern = parts[1]

            for root, dirs, file_list in os.walk(base):
                for file in file_list:
                    if glob.fnmatch.fnmatch(file, pattern):
                        files.append(os.path.join(root, file))
        else:
            # Check if the path is a directory, and if so, get all the files in it
            if os.path.isdir(path):
                files = glob.glob('%s/*' % path)
            else:
                files = glob.glob(path)

        abs_files = [os.path.abspath(f) for f in files]

        return abs_files

    # Converts a date string like "2013-09-11" or "2013-09-11 04:23" to Unix time
    def make_unix_date(self, date_string):
        # First, try with time
        try:
            date_obj = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
        except ValueError:
            # Now try with just the date 
            try:
                date_obj = datetime.strptime(date_string, '%Y-%m-%d')
            except ValueError:
                return -1 

        if date_obj:
            return float(date_obj.strftime('%s'))
