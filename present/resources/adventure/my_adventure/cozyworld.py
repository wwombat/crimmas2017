from game_engine import * 
import time

foyer = Room("Foyer", """
        You find yourself in a cozy cave lit by a crackling hearth.
        A pile of neatly stacked potatoes rests in the corner, and
        two pairs of coats and scarves are hung up on the wall.
        """,
        "you see the warm glow of a hearth...",
        make_stat_incrementer("coziness", 2))

@Action("Put on scarf and coat", "p sc")
def put_on_scarf_and_coat(player, room):
    print("""
        You put on your favorite fuzzy scarf and your
        quilted coat""")
    increment_stat(player, "coziness", 3)
    increment_stat(player, "warmth", 10)

@Action("Take off scarf and coat", "p sc")
def take_off_scarf_and_coat(player, room):
    print("""
        You take off your scarf and coat and lay them
        gently on the ground.
        """)
    increment_stat(player, "coziness", -3)
    increment_stat(player, "warmth", -10)

scarf_and_coat = Thingy("scarf and coat", "sc",
        put_on_scarf_and_coat,
        take_off_scarf_and_coat,
        [],
        [])
register_action(foyer, scarf_and_coat.grab)

library = Room("Library", """
        You are in a tiny room entirely filled with books.

        Kai is nestled in a big, plush armchair in the corner,
        wrapped in a big fuzzy blanket and snoring softly.
        """,
        "you hear the sound of gentle snoring...",
        make_stat_incrementer("coziness", 5));

@Action("Read book", "rb")
def read_book(player, room):
    import books
    book = books.get_random()
    book(player, room)
register_action(library, read_book)

@Action("Poke Kai", "pk")
def poke_kai(player, room):
    print("""
        You poke kai, and he wrinkled his nose in his sleep,
        murmurs something about potatos, and then burrows deeper 
        into his blanket...""")
    increment_stat(player, "coziness", 1)
    delete_action(poke_kai)
register_action(library, poke_kai) 

den = Room("Den", """
        A long, low-ceilinged hall stretches in front of you,
        covered in carefully-applied wallpaper featuring illustrations
        of a North African city.

        Paper lanterns hanging from the ceiling shed a gentle
        golden-red glow everywhere.
        """,
        "you see a soft red glow...",
        make_stat_incrementer("coziness", 1));

@Action("Look at wall paper", "lw")
def look_at_wallpaper(player, room):
    print("""
        It's a drawing of a fishing town. 
        You see terraced buildings... sunlight... the sea...""")
    increment_stat("coziness", 1)
    increment_stat("wistfulness", 1)
    delete_action(look_at_wallpaper)
register_action(den, look_at_wallpaper)

def grab_lantern(player, room):
    print("""
        You carefully grab one of the paper lanterns.
        Its glow makes you feel cozy.""")
    increment_stat(player, "coziness", 1)
    increment_stat(player, "light", 1)
    increment_stat(room, "light", -1)

def drop_lantern(player, room):
    print("""
        You set the lantern to the side.
        """)
    decrement_stat(player, "coziness", 1)
    increment_stat(player, "light", -1)
    increment_stat(room, "light", 1)

lantern = Thingy("lantern", "l",
        grab_lantern,
        drop_lantern,
        [],
        [])
register_action(den, lantern.grab)

tower = Room("The Tower", """
        You are in a small garden at the top of a tower.

        The entire garden is cloaked in snow- stone beasts sit,
        stoic, beneath coats of snow, next to bare-limbed trees.
        Flakes of snow slowly drift down from the flat white sky.

        A chest-height wall rings the tower's top, and looking out,
        you can see a snowy forest stretching into the distance.

        In the summer, you think the garden must be truly beautiful-
        you see a trellis where you remembered that morning glories 
        would grow and open their faerie-blue trumpets, and a cluster 
        of ornamental figs (now tightly wrapped in blankets) huddled 
        around a stone bench in the shape of a turtle.
        """,
        "you feel a cold wind blowing...",
        seq([make_stat_incrementer("coziness", -3),
             make_stat_incrementer("wistfulness", 3)]))

kitchen = Room("Kitchen", """
        You see a small, but lovely kitchen, lit by a flickering
        candle and the dim blue-red glow of the oven's pilot
        light.
        """,
        "a delicious scent wafts...",
        make_stat_incrementer("coziness", 2))

@Action("Smell", "s")
def smell(player, room):
    print("""
        Smells like crimmas ~^~""")
    increment_stat(player, "coziness", 1)
register_action(kitchen, smell)

@Action("Eat cookies", "eat")
def eat(player, room):
    print("""
        NOM NOM NOM NOM NOM""")
    increment_stat(player, "coziness", 1)
    increment_stat(player, "satiety", 1)
    cookies.delete()

cookies = Thingy("cookies", "c",
        make_print_action("""
        You nab some delicious cookies."""),
        make_print_action("""
        You gently lay the sweet cookies down."""),
        [],
        [eat])
register_action(kitchen, cookies.grab)

# =====

link_rooms(den, library, "Through an old wooden door", ("n", "s"),
           "You slip through the door...")
link_rooms(foyer, den, "Through a wide arch", ("n", "s"),
           "You tip-toe through the arch...")
link_rooms(foyer, kitchen, "Through a little oak door", ("e", "w"),
           "You slip through the door...")
link_rooms(den, tower, "From a stone staircase", ("u", "d"),
           "You enter the staircase...")

# =====

class OneTimeConditionalAction(object):
    def __init__(self, action, condition):
        self.action = action
        self.condition = condition
    @onetime 
    def register(self, obj):
        register_action(obj, self.action)
    def check(self, player):
        if self.condition(player):
            self.register(player)

@Action("Apotheosize", "ap")
def apotheosis_action(player, room):
    print("""
        A golden light wreathes you, and your vision blurs.
        You feel a tremendous energy coursing through you-
        the power of COZINESS!!!

        Your coziness levels reached such a high level
        that you have become a COZY DEMIGOD
        """)
    increment_stat(player, "coziness", 998832419875)
    delete_action(apotheosis_action)
def apotheosis_check(player):
    return get_stat(player, "coziness") > 20
apotheosis = OneTimeConditionalAction(apotheosis_action, apotheosis_check)

def world():
    conditions = [apotheosis]
    def world_action(player):
        nonlocal conditions
        for condition in conditions:
            condition.check(player)

    return World(foyer, world_action)

def player():
    player = Player();
    set_stat(player, "coziness", 1)
    return Player()
