#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# world.py - overview.  Loads all the rooms and provides a world map.
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

class World:
    def __init__ (self):
        self.first_room = ''
        self.rooms = {}

    def load (self, file):
        pass



if __name__ == '__main__':
    world = World ()

