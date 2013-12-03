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

from room import Room

# Status
# Fixme: move to status
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
        self.current_room = None
        self.rooms = {}
        self.inventory = []
        self.status = STATUS_ALIVE

    def load_rooms (self, rooms):
        for row in rooms:
            room = Room (row[0], row[1], row[2], '')
            self.rooms[room.id] = room

    def load_connections (self, connections):
        for connection in connections:
            # connection is of the form:
            # (room-id, (direction, target-room-id), ...
            # FIXME: will do a more robust job later
            
            room = self.rooms[connection[0]]
            for (direction, target_room_id) in connection[1:]:
                room.set_connection (direction, target_room_id)

    def set_current_room (self, room_id, ignore_visited=False):
        room = self.rooms[room_id]
        self.room = room
        if not ignore_visited:
            self.room.set_visited ()

    def get_current_room (self):
        return self.room

    def get_room (self, id):
        return self.rooms[id]

    def keep_playing (self):
        return (self.status == STATUS_ALIVE)

    def set_game_status (self, status):
        self.status = status

    def get_game_status (self):
        return self.status



if __name__ == '__main__':
    world = World ()

