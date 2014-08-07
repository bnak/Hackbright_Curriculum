import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys


#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 6
GAME_HEIGHT = 6

#### Put class definitions here ####
class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self,player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just won back a gem! You have %d items!" % (len(player.inventory)))

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = False

    #def interact(self, player):
         # player.IMAGE = "Invisible"
        #print "ROCK"
        # if direction == "up":
        #     return (player.x, player.y-2)
        # elif direction == "down":
        #     return (splayer.x, player.y+2)
        # elif direction == "left":
        #     return(player.x-2, player.y)
        # elif direction == "right":
        #     return (player.x+2, player.y)
        # else:
        #     return None

class Heart(GameElement):
    IMAGE = "Heart"
    SOLID = True

class Character(GameElement):
    IMAGE = "Dirt"
    def next_pos_none(self, direction):

        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return(self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        else:
            return None
    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []
        self.his_inventory = []

    def next_pos_element (self, direction):
        print "CHARACTER"
        if direction == "up":
            return (self.x, self.y-2)
        elif direction == "down":
            return (self.x, self.y+2)
        elif direction == "left":
            return(self.x-2, self.y)
        elif direction == "right":
            return (self.x+2, self.y)
        else:
            return None
        self.his_inventory.append(Rock)
        GAME_BOARD.draw_msg("History Inventory: %d" % (self.his_inventory)) 



class Character_Rock(Character):
    IMAGE = "Rock"





####   End class definitions    ####

def keyboard_handler():
    direction = None
    if KEYBOARD[key.UP]:
        direction = "up"
        
        
    elif KEYBOARD[key.DOWN]:
        direction = "down"
        
        
    elif KEYBOARD[key.LEFT]:
        direction = "left"
        
        
    elif KEYBOARD[key.RIGHT]:
        direction = "right"
        
        
    

    if direction:
        next_location = PLAYER.next_pos_none(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        if next_location[0] in range(0,GAME_WIDTH) and next_location[1] in range(0, GAME_HEIGHT):
            existing_el = GAME_BOARD.get_el(next_x, next_y)

            print isinstance(existing_el, Rock)

            if isinstance(existing_el, Rock):
                next_location = PLAYER.next_pos_element(direction)
                next_x = next_location[0]
                next_y = next_location[1]
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                GAME_BOARD.set_el(next_x, next_y, PLAYER)

            if existing_el:
                existing_el.interact(PLAYER)

            #if existing_el is not existing_el.SOLID:

            else:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
                GAME_BOARD.set_el(next_x, next_y, PLAYER)
        # else:
        #     GAME_BOARD.draw_msg("Cannot go off board")

def initialize():
    
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    rock_positions = [
            (2,1),
            (1,2),
            (3,2),
        ]

    rocks = []

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    # rocks[-5].SOLID = False

    for rock in rocks:
        print rock

    heart_positions = [
            (3,1),
            (2,4),
            (4,2),
        ]

    hearts = []

    for pos in heart_positions:
        heart = Heart()
        GAME_BOARD.register(heart)
        GAME_BOARD.set_el(pos[0], pos[1], heart)
        hearts.append(heart)

    # rocks[-5].SOLID = False

    for heart in hearts:
        print heart



    GAME_BOARD.draw_msg("YOU MUST WIN IT BACK")
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3,1, gem)

    keyboard_handler()