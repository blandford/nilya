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


import sys
import signal



def evaluate (reply):
    print reply
    return True

def mainloop ():
    alive = True
    
    while alive:
        try:
            replies = raw_input('> ').lower().split(';') or ['']
        except (KeyboardInterrupt, EOFError):
            replies = []
            alive = False
            
        for reply in replies:
            alive = evaluate (reply)
    print


if __name__ == '__main__':
    mainloop ()
    sys.exit (0)
