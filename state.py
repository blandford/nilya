#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# state.py - Captures the current state of the system.  Used to
# save/restore a game, as well as keep track of items.
#
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

class State:
    # Class to encapsulate all the game state.  Used to save/load to
    # disk
    STATUS_ALIVE = 1
    STATUS_DEAD = 2
    STATUS_SAVE = 3
    STATUS_QUIT = 4

    def __init__ (self):
        self.items = []
        self.money = 0
        self.map = None

    def set_balance (self, money):
        assert (money > 0)
        self.money = money

    def get_balance (self):
        return self.money

    def add_funds (self, funds):
        self.money += funds

    def spend_funds (self, funds):
        if funds.money < funds:
            return False
        funds.money -= funds
        return True

    def keep_playing (self):
        return (self.status == STATUS_ALIVE)

    def set_game_status (self, status):
        self.status = status

    def get_game_status (self):
        return self.status
