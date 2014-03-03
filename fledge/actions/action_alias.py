#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter

# alias
def action_alias(controller, parameters):
    """
  Creates a new action or path alias.

    alias mv move
    alias r90 rotate 90
    alias {logs} /var/log/apache2/vhosts/
    """

    split_params = parameters.split(' ')
    alias = split_params[0]
    target = ' '.join(split_params[1:])

    if alias[0] == '{' and alias[:-1] == '}':
        # Path
        controller.aliases['paths'][alias] = target
    else:
        # Action
        controller.aliases['actions'][alias] = target
