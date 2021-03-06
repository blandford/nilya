#!/usr/bin/python


initial_text = """
Welcome to The Nilya Quest!

You are on a quest to find the nilya, and do amazing things with it.
"""
##
## Items
##
## List of tuples of the form [('id', 'short name', 'longer description'),...]
##
items = [
    ( 'stockton-key',
      'key',
      """A small silver key.  It only fits in one door"""),
    ( 'golden-marble',
      'marble',
      """A small, golden marble. It's your good luck charm."""),
    ( 'silver-needle',
      'needle',
      """A silver needle. It cuts through any fabric like a knife through butter."""),
    ( 'silk-thread',
      'thread',
      """A spool of purple silk thread."""),
    ( 'charm bracelet',
      'bracelet',
      """A tarnished, silver, charm bracelet. It has a moon charm on it."""),
    ( 'elderberry-candy',
      'candy'
      """Its a small elderberry candy. Your mothers speacialty."""),
    ( 'small-matchbox',
      'matchbox',
      """Its a box of matches."""),
    ( 'spellbonder-wand',
      'spellbonder',
      """A wand made out of pure mooncrest. It has a silver moon on top."""),
    ( 'magic-clay',
      'clay',
      """A very large lump of magic clay"""),
    ( 'sewing scissors',
      'scissors',
      """Very sharp scissors""")
]

## 
## Places
## 
## List ot tuples of the form [('id', 'short name', 'longer description'),..]
##
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
      """It's a brick house with a yellow roof and a wooden door. There are some windows and a field. It also has a garden."""),

    ( 'stockton-glorys-garden',
      'Glory\'s house',
      """It's a garden with lots of flowers.  There is a white picket fence around it."""),

    ( 'stockton-big-tree',
      'big tree',
      """Its a big tree."""),

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
      """It's a wooden dock with a boathouse.  There are two motorboats and one sailboat here. Would you like to buy a boat?"""
    ),

    ( 'stockton-crystal-lake',
      'Crystal Lake',
      """Its a beautiful lake thats clear and calm as crystal."""
    ),

    ( 'stockton-crystal-river',
      'Crystal River',
      """Its a river conected to Crystal Lake."""
    ),
    
    ( 'stockton-closet',
      'Closet',
      """Its a closet""")

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
     ('in','closet'),
    ),
    
    ('stockton-jacks-house',
     ('n', 'stockton-glorys-house'),
    ),

    ('stockton-glorys-house', 
     ('n', 'stockton-home'),
     ('s', 'stockton-jacks-house'),
     ('nw', 'stockton-general-store'),
     ('w', 'stockton-glorys-garden'),
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
     ('s', 'stockton-crystal-lake'),
    ),
    
    ('stockton-glorys-garden',
     ('up', 'stockton-big-tree'),
    ),

    ('stockton-big-tree',
     ('down', 'stockton-glorys-garden'),
    ),
    
    ('stockton-crystal-lake',
     ('n', 'stockton-dock'),
     ('se','stockton-crystal-river'),
    ),

    ('stockton-crystal-river',
     ('nw', 'stockton-crystal-lake'),
    ),
    
    ('stockton-closet',
     ('out','stockton-bedroom')
    ),
]
