#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# verbs.py - parser for the commands.
# 
# Copyright © 2013 Jonathan Blandford
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# Authors:
# Eleanor and Jonathan Blandford

import sys
import actions
import misc

Homonyms = {
    'get': 'take',
    'grab': 'take',
    
    'q': 'quit',
    'exit': 'quit',

    'l': 'look',

    # directions
    'n': 'go', 'ne': 'go',
    'e': 'go', 'se': 'go',
    's': 'go', 'sw': 'go',
    'w': 'go', 'nw': 'go',
    'up': 'go', 'down': 'go',
}

Actions = {
    'quit':actions.quit_game,
    'save':actions.save_game,
    'go': actions.move,
    'look': actions.look,
}


class Verbs:
    def __init__ (self):
        pass

    def eval (self, world_map, commands):
        # Finds the appropriate function and executes it.  Returns a
        # message to print.
        action = commands[0]

        if not action:
            return ''

        action = misc.short_direction (action)

        if Homonyms.has_key (action):
            action = Homonyms [action]

        func = None
        if Actions.has_key (action):
            func = Actions [action]

        if func:
            return func (world_map, commands)

        return ''
