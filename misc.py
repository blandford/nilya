#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# misc.py - Misc functions
# 
# Copyright © 2013 Jonathan Blandford, Eleanor Blandford
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

def bold (str):
    ## takes a string and makes it bold
    return "\033[1m" + str + "\033[0;0m"

def dont_understand (str):
    ##
    return "I don't understand how to '" + str + "'\n"

def short_direction (direction):
    direction_mapping = {
        # directions
        'north': 'n',
        'northeast': 'ne',
        'east': 'e',
        'southeast': 'se',
        'south': 's',
        'southwest': 'sw',
        'west': 'w',
        'northwest': 'nw',
    }
    if direction_mapping.has_key (direction):
        return direction_mapping[direction]
    return direction
