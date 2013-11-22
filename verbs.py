#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# nilya.py - A text adventure game
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

import json
import sys
import actions

Homonyms = {
    'get': 'take',
    'grab': 'take',
    
    'exit': 'quit',

    # directions
    'north': 'go', 'n': 'go',
    'northeast': 'go', 'ne': 'go',
    'east': 'go', 'e': 'go',
    'southeast': 'g', 'se': 'go',
    'south': 'go', 's': 'go',
    'southwest': 'go', 'sw': 'go',
    'west': 'go', 'w': 'go',
    'northwest': 'go', 'nw': 'go',
}

Actions = {
    'quit':actions.quit_game,
    'save':actions.save_game,
    'go': actions.move,
    'look': actions.look,
}




class Verbs:
    def __init__ (self, filename):
        pass

    def eval (self, world_map, commands):
        # Finds the appropriate function and executes it.  Returns a
        # message to print.
        action = commands[0]

        if not action:
            return ''

        if Homonyms.has_key (action):
            action = Homonyms [action]

        func = None
        if Actions.has_key (action):
            func = Actions [action]

        if func:
            return func (world_map, commands)

        return ''



# 
if __name__ == '__main__':
    verbs = Verbs ('verbs.json')

    print json.dumps (homonyms)
    sys.exit (0)
