#!/usr/bin/python


initial_text = """
Welcome to The Nilya Quest!

You are on a quest to find the nilya, and do amazing things with it.
"""
map_rooms = [
    ( 'stockton-home',
      'Home', 
      """A white house with a red roof.  There is a wooden door and some small windows here.  It has a small garden and field and a white fence around it.  It is very pretty.""",),

    ( 'stockton-kitchen',
      'Kitchen', 
      """You are in your kitchen.  It smells like elderberry juice and gingerbread."""),

    ( 'stockton-bedroom',
      'bedroom',
      """You are in your bedroom.  It has two beds,a table, a lamp  and a closet."""),

    ( 'stockton-jacks-house',
      'Jack\'s house', 
      """It's a brown house with a wooden roof.  It has two floors and has a chicken coop, a well and a field."""),

    ( 'stockton-glorys-house',
      'Glory\'s house',
      """It's a brick house with a yellow roof and a wooden door.  There are some windows, a fence, and a field."""),

    ('stockton-school',
     'The Stockton School',
     """A small brown schoolhouse"""),

    ( 'stockton-market',
      'The Stockton Market',
      """Stockton Market.  You buy turnips here."""),

    ( 'stockton-general-store',
      'The Stockton Store',
      """Stockton Store.  You buy castles here"""),

    ( 'stockton-church',
      'Church',
      """A brown, wooden church with stained glass windows.  It's very popular."""
    ), 

    ( 'stockton-dock',
      'The Docks',
      """It's a wooden dock with a boathouse.  There are two motorboats and one sailboat here."""
    ),
]

map_connections = [
    ('stockton-home', 
     ('n', 'stockton-market'),
     ('w', 'stockton-general-store'),
     ('s', 'stockton-glorys-house'),
     ('e', 'stockton-church'),
     ('ne', 'stockton-school'),
     ('in', 'stockton-kitchen'),
    ),

    ('stockton-kitchen',
     ( 'out', 'stockton-home'),
     ('in', 'stockton-bedroom'),
    ),

    ('stockton-bedroom',
     ( 'out', 'stockton-kitchen'),
    ), 


    ('stockton-jacks-house',
     ('n', 'stockton-glorys-house'),
    ),

    ('stockton-glorys-house', 
     ('n', 'stockton-home'),
     ('s', 'stockton-jacks-house'),
     ('nw', 'stockton-general-store'),
    ),

    ('stockton-market', 
     ('s', 'stockton-home'),
     ('e', 'stockton-school'),
     ('se', 'stockton-church'),
     ('sw', 'stockton-general-store'),
    ),

    ('stockton-general-store', 
     ('e', 'stockton-home'),
     ('ne', 'stockton-market'),
     ('sw', 'stockton-glorys-house'),
    ),

    ('stockton-school',
     ('w', 'stockton-market'),
     ('s', 'stockton-church'),
     ('sw', 'stockton-home'),
    ),

    ('stockton-church',
     ('w', 'stockton-home'),
     ('n', 'stockton-school'),
     ('s', 'stockton-dock'),
     ('nw', 'stockton-market'),
    ),

    ('stockton-dock',
     ('n', 'stockton-church'),
    ),
    
]
