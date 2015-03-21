#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# nilya.py - A text adventure game
# Copyright © 2013 Jonathan Blandford
# Copyright © 2015 Eleanor Blandford
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
import signal
import world
import data
from verbs import Verbs
import state

PROMPT = '> '


## First, set up the world map
world_map = world.World ()
world_map.load_rooms (data.map_rooms)
world_map.load_connections (data.map_connections)
world_map.set_current_room ('stockton-home')

## Set up the world state
world_state = state.State ()
world_state.set_funds (100)
world_state.set_world_map (world_map)

## set up the parsing engine
verbs = Verbs ()


def tokenize_command (command):
    # Take a command and turn it into a list of tokens.  As an
    # example, it will turn "go south " into ['go', 'south']
    command = ' '.join (command.split ())
    return command.split(' ')


def read_input (tokenize):
    # Read in a set of commands from the prompt.  There can be
    # multiple commands per line separated by ';'.  This is the only
    # place that will read input for the user.  If tokenize is True,
    # it will return a list of lowercase tokens that can be parsed
    # individually.  As an example, it could return: [['take',
    # 'apple'], ['go', 'down'], ['w']]
    #
    # Otherwise, it will return the raw string in a list with one item

    try:
        user_input = raw_input(PROMPT)
        if tokenize:
            commands = user_input.lower().split(';') or ['']
            commands = map (tokenize_command, commands)
        else:
            commands = [user_input]
    except (KeyboardInterrupt, EOFError):
        # Someone hit C-c or C-D.  Treat it like they'd typed 'quit'
        # as a special case
        print
        commands = [ ['quit'] ]
    
    return commands
    

def evaluate_command (command):
    # Evaluate a command.  This is the only place that will print out
    # any output to the user.  It expects a set of tokens 

    message = verbs.eval (command, world_state)
    if message:
        print message

    status = world_state.get_game_status ()

    if status == state.STATUS_ALIVE:
        return True
    if status == state.STATUS_DEAD:
        return False
    if status == state.STATUS_SAVE:
        print 'Saving not implemented yet.  Sorry.'
        return True
    if status == state.STATUS_QUIT:
        print 'Goodbye!'
        return False

    return False


def mainloop ():
    keep_playing = True
    print data.initial_text
    evaluate_command (['look'])

    while keep_playing:
        commands = read_input (True)

        for command in commands:
            keep_playing = evaluate_command (command)
            if not keep_playing:
                # the game has ended!
                break

    # Put some white space at the end
    print

if __name__ == '__main__':
    mainloop ()
    sys.exit (0)
