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

class Room:
    def __init__ (self, id, short_name, description, items):
        self.id = id
        self.short_name = short_name
        self.description = description
        self.items = items
        self.neighbors = {}
        self.visited = False
    
    def display (self):
        print "\033[1m" + self.short_name + "\033[0;0m"
        print self.description

if __name__ == '__main__':
    rooms = []
    for (id, short_name, description) in data.map_sections:
        room = Room (id, short_name, description, [])
        rooms.append (room)
    for room in rooms:
        room.display ()
        print

    
