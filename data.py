#!/usr/bin/python


initial_text = """
Welcome to The Nilya Quest!

You are on a quest to find the nilya, and do amazing things with it.
"""
map_rooms = [
    ( 'stockton-home',
      'Home', 
      """A white house with a red roof.  There is a wooden door and some small windows here.  It has a small garden and field and a white fence around it.  It is very pretty.""",),

    ( 'stockton-jacks-house',
      'Jack\'s house', 
      """It's a brown house with a wooden roof.  It has two floors and has a chicken coop, a well and a field."""),

    ( 'stockton-glorys-house',
      'Glory\'s house',
      """It's a brick house with a yellow roof and a wooden door.  There are some windows, a fence, and a field."""),

    ('stockton-school',
     'The Stockton School',
     """ """),

    ( 'stockton-market',
      'The Stockton Market',
      """ """),

    ( 'stockton-general-store',
      'The Stockton Store',
      """ """),
]


map_connections = [
    ('stockton-home', 
     ('n', 'stockton-market'),
     ('w', 'stockton-general-store'),
     ('s', 'stockton-glorys-house'),
    ),

    ('stockton-glorys-house', 
     ('n', 'stockton-home'),
    ),

]


