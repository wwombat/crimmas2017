"""
Wow!!! a whole world
"""

class World(object):
    def __init__(initial_room):
        self.initial_room

        # you can always quit :')
        def quit(player, room):
            player.victory = True
        Action(quit, "Quit", "q")

    def initial_room():
        return self.initial_room

    def get_actions():
        return self.actions

