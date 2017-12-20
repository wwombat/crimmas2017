"""
ADVENTURE AWAITS
"""

import cozyworld
import time

def game_eval(player, room, world):
    room.act(player)
    world.act(player)
    actions = []
    for thing in [room, player, world]:
        actions += list(thing.actions.values())
    return actions

def interactive_choose(actions):
    ''' Get the next action '''
    choice = input("Action: ")
    for action in actions:
        if choice == action.hotkey:
            return action

def play(player, world, chooser):
    ''' the main loop '''
    while not player.victory:
        room = player.room
        print(str(room))
        actions = game_eval(player, room, world)
        print()
        print(str(player))
        print()
        for action in actions:
            print("{}".format(action.desc))
        action = None
        while action is None:
            action = chooser(actions)
        action(player, room)

if __name__ == "__main__":
    world = cozyworld.world()
    player = cozyworld.player()
    player.room = world.initial_room
    play(player, world, interactive_choose)
