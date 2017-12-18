from game_engine import * 
import time

foyer = Room("Foyer", """
        You find yourself in a cozy cave lit by a crackling hearth.
        A pile of neatly stacked potatoes rests in the corner, and
        three pairs of coats and scarves are hung up on the wall.
        """,
        "you see the warm glow of a hearth...",
        make_stat_incrementer("coziness", 2))

library = Room("Library", """
        You are in a tiny room entirely filled with books.

        Kai is nestled in a big, plush armchair in the corner,
        wrapped in a big fuzzy blanket and snoring softly.
        He has a copy of "The Rabbi's Cat" open on his lap.
        """,
        "you hear the sound of gentle snoring...",
        make_stat_incrementer("coziness", 5));

den = Room("Den", """
        A long, low-ceilinged hall stretches in front of you,
        covered in carefully-applied wallpaper featuring illustrations
        of some sort of North African city (terraced buildings, sunlight,
        the sea...)

        Paper lanterns hanging from the ceiling shed a gentle
        golden-red glow everywhere.
        """,
        "you see a soft red glow...",
        make_stat_incrementer("coziness", 1));

tower = Room("The Tower", """
        You are in a small garden at the top of a steep tower.

        The entire garden is cloaked in snow- stone beasts sit,
        stoic, beneath coats of snow, next to bare-limbed trees.
        Flakes of snow slowly drift down from the flat, bone-white
        sky.

        A chest-height wall rings the tower's top, and looking out,
        you can a vast landscape of snow, great pine trees burned with
        stretching away until they recede into blankness.

        In the summer, you think the garden must be truly lovely-
        you see a trellis where morning glories glow and open their
        faerie-blue trumpets, and a cluster of ornamental figs (now
        tightly wrapped in blankets) huddled around a stone bench in
        the shape of a turtle.
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
        Smells like cookies ~^~""")
    increment_stat(player, "coziness", 1)
    time.sleep(1)
register_action(kitchen, smell)

@Action("Eat cookies", "eat")
def eat(player, room):
    print("""
        NOM NOM NOM NOM NOM""")
    increment_stat(player, "coziness", 1)
    increment_stat(player, "satiety", 1)
    cookies.delete()
    time.sleep(1)

cookies = Thingy("cookies", "cookies",
        """
        Delicious chocolate chip cookies, straight from the oven.
        """,
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
        print("checking...")
        if self.condition(player):
            self.register(player)

@Action("Apotheosize", "ap")
def apotheosis_action(player, room):
    print("""
        A golden light wreathes you, and your vision blurs
        you feel a tremendous energy coursing through you-
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
