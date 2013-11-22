#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# room.py - An individual room
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

import data
import misc

class Room:
    def __init__ (self, id, short_name, description, items):
        self.id = id
        self.short_name = short_name
        self.description = description
        self.items = items
        self.connections = {}
        self.visited = False
    
    def set_connection (self, direction, id):
        self.connections[direction] = id

    def get_connection (self, direction):
        try:
            return self.connections[direction]
        except KeyError:
            return None

    def get_description (self, ignore_visited=False):
        # Returns a string to describe the room.  The first time you
        # see a room we also include the long description
        str = misc.bold (self.short_name)
        if ignore_visited or not self.visited:
            str += '\n' + self.description
        return str


    def display (self):
        print self.get_description (False)

    def set_visited (self):
        self.visited = True

if __name__ == '__main__':
    pass

    
