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

import world
import misc

def quit_game (world_map, args):
    world_map.set_game_status (world.STATUS_QUIT)

def save_game (world_map, args):
    # FIXME: implement
    pass

def look (world_map, args):
    room = world_map.get_current_room ()
    return room.get_description (True)


def move (world_map, args):
    # This updates our position on the world map.  It will update
    # world_map and return the current
    room = world_map.get_current_room ()

    # first, we have to handle the special 'go' verb
    if args[0] == 'go':
        args = args[:1]

    # then, we update our position
    direction = args[0]
    id = room.get_connection (direction)
    if id:
        new_room = world_map.get_room (id)
        str = new_room.get_description ()
        world_map.set_current_room (id)
        return str
    else:
        str = "I don't know how to go " + direction
        return str

