#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter

# aliases
def action_aliases(controller, parameters):
    """
  Prints existing aliases

    aliases
    """

    for alias, target in controller.aliases['actions'].iteritems():
        print '%s: %s' % (alias, target)

    for alias, target in controller.aliases['paths'].iteritems():
        print '{%s}: %s' % (alias, target)
