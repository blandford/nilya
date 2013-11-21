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

# Statuses
STATUS_ALIVE = 1
STATUS_DEAD = 2
STATUS_SAVE = 3
STATUS_QUIT = 4

# Moving Directions
DIR_NORTH = 1
DIR_NORTHEAST = 2
DIR_EAST = 3
DIR_SOUTHEAST = 4
DIR_SOUTH = 5
DIR_SOUTHWEST = 6
DIR_WEST = 7
DIR_NORTHWEST = 8
DIR_UP = 9
DIR_DOWN = 10


class World:
    def __init__ (self):
        self.current_section = ''
        self.sections = {}
        self.inventory = []
        self.status = STATUS_ALIVE

    def load_sections (self, sections):
        pass

    def set_current_section (self, section):
        pass

    def keep_playing (self):
        return (self.status == STATUS_ALIVE)

    def set_game_status (self, status):
        self.status = status

    def get_game_status (self):
        return self.status



if __name__ == '__main__':
    world = World ()

