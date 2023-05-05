# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:25:25 2023

@author: alexe
"""
from _215_sprites import Sprites
from _215_game_classes import GameClasses as gc
sprites = Sprites()

objects = []
#Name = gc.Object(Item Icon, Item Type, Item Health, Item Origin, (Item Hitbox, X, Y, W, H))
at = (500, 100)
rock = gc.Object("Rock", sprites.rock_1, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (450, 30)
rock2 = gc.Object("Rock", sprites.rock_2, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (490, 10)
rock3 = gc.Object("Rock", sprites.rock_1, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (547, 131)
rock4 = gc.Object("Rock", sprites.rock_2, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (665, 55)
rock6 = gc.Object("Rock", sprites.rock_1, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (643, 161)
rock7 = gc.Object("Rock", sprites.rock_2, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (397, 102)
rock8 = gc.Object("Rock", sprites.rock_2, "minable", 4,
                 at, (at[0], at[1] + 22, 32, 10),
                 (at[0], at[1] + 8, 33, 24), True)

at = (600, 100)
rockl1 = gc.Object("Rock Large", sprites.big_rock_pile, "minable", 7,
                  at, (at[0] + 3, at[1] + 22, 73, 20),
                  (at[0], at[1], 76, 48), True)

at = (557, 47)
rockl2 = gc.Object("Rock Large", sprites.big_rock_pile, "minable", 7,
                  at, (at[0] + 3, at[1] + 22, 73, 20),
                  (at[0], at[1], 76, 48), True)

at = (550, 161)
rockl3 = gc.Object("Rock Large", sprites.big_rock_pile, "minable", 7,
                  at, (at[0] + 3, at[1] + 22, 73, 20),
                  (at[0], at[1], 76, 48), True)

at = (357, 200)
tree1 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                  at, (at[0] + 14, at[1] + 74, 18, 10),
                  (at[0] + 8, at[1] + 64, 30, 20), True)

at = (10, 10)
tree2 = gc.Object("Tree Large", sprites.treeL, "chopable", 7,
                  at, (at[0] + 30, at[1] + 157, 33, 10),
                  (at[0] + 20, at[1] + 127, 53, 40), True)

at = (100, -15)
tree3 = gc.Object("Tree Large", sprites.treeL, "chopable", 7,
                  at, (at[0] + 30, at[1] + 157, 33, 10),
                  (at[0] + 20, at[1] + 127, 53, 40), True)

at = (75, 100)
tree4 = gc.Object("Tree Apple", sprites.treeA, "chopable", 5,
                  at, (at[0] + 30, at[1] + 165, 30, 10),
                  (at[0] + 25, at[1] + 135, 40, 40), True)

at = (2, 175)
tree5 = gc.Object("Tree Large", sprites.treeL, "chopable", 7,
                  at, (at[0] + 30, at[1] + 157, 33, 10),
                  (at[0] + 20, at[1] + 127, 53, 40), True)

at = (155, 70)
tree6 = gc.Object("Tree Large", sprites.treeL, "chopable", 7,
                  at, (at[0] + 30, at[1] + 157, 33, 10),
                  (at[0] + 20, at[1] + 127, 53, 40), True)

at = (200, 125)
tree7 = gc.Object("Tree Large", sprites.treeL, "chopable", 7,
                  at, (at[0] + 30, at[1] + 157, 33, 10),
                  (at[0] + 20, at[1] + 127, 53, 40), True)

at = (200, 40)
tree8 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                  at, (at[0] + 14, at[1] + 74, 18, 10),
                  (at[0] + 8, at[1] + 64, 30, 20), True)

at = (10, 120)
tree9 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                  at, (at[0] + 14, at[1] + 74, 18, 10),
                  (at[0] + 8, at[1] + 64, 30, 20), True)

at = (90, 250)
tree10 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                  at, (at[0] + 14, at[1] + 74, 18, 10),
                  (at[0] + 8, at[1] + 64, 30, 20), True)

at = (150, 270)
tree11 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                  at, (at[0] + 14, at[1] + 74, 18, 10),
                  (at[0] + 8, at[1] + 64, 30, 20), True)

at = (250, 70)
tree12 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                  at, (at[0] + 14, at[1] + 74, 18, 10),
                  (at[0] + 8, at[1] + 64, 30, 20), True)

at = (290, 30)
tree13 = gc.Object("Tree Apple", sprites.treeA, "chopable", 5,
                  at, (at[0] + 30, at[1] + 165, 30, 10),
                  (at[0] + 25, at[1] + 135, 40, 40), True)

at = (50, 250)
tree14 = gc.Object("Tree Apple", sprites.treeA, "chopable", 5,
                  at, (at[0] + 30, at[1] + 165, 30, 10),
                  (at[0] + 25, at[1] + 135, 40, 40), True)

objects.append(rock), objects.append(rock2), objects.append(rock3)
objects.append(rock4), objects.append(rock6)
objects.append(rock7), objects.append(rock8)
objects.append(rockl1), objects.append(rockl2), objects.append(rockl3)
objects.append(tree1)
objects.append(tree2)
objects.append(tree3)
objects.append(tree4)
objects.append(tree5)
objects.append(tree6)
objects.append(tree7)
objects.append(tree8)
objects.append(tree9)
objects.append(tree10)
objects.append(tree11)
objects.append(tree12)
objects.append(tree13)
objects.append(tree14)

gatherables = []
cottonball1 = gc.Item(
         "Cottonball", 400, 300, 50, 50, False, 0, 1)
cb2 = gc.Item(
         "Cottonball", 300, 290, 50, 50, False, 0, 1)
cb3 = gc.Item(
         "Cottonball", 460, 121, 50, 50, False, 0, 1)
cb4 = gc.Item(
         "Cottonball", 176, 255, 50, 50, False, 0, 1)
cb5 = gc.Item(
         "Cottonball", 200, 350, 50, 50, False, 0, 1)
cb6 = gc.Item(
         "Cottonball", 230, 320, 50, 50, False, 0, 1)
cb7 = gc.Item(
         "Cottonball", 493, 161, 50, 50, False, 0, 1)
rf1 = gc.Item(
         "Red Flower", 310, 72, 50, 50, False, 0, 1)
rf2 = gc.Item(
         "Red Flower", 300, 30, 50, 50, False, 0, 1)
rf3 = gc.Item(
         "Red Flower", 320, 60, 50, 50, False, 0, 1)
rf4 = gc.Item(
         "Red Flower", 340, 332, 50, 50, False, 0, 1)
rf5 = gc.Item(
         "Red Flower", 320, 360, 50, 50, False, 0, 1)
rf6 = gc.Item(
         "Red Flower", 35, 421, 50, 50, False, 0, 1)
rf7 = gc.Item(
         "Red Flower", 15, 450, 50, 50, False, 0, 1)
rf8 = gc.Item(
         "Red Flower", 139, 400, 50, 50, False, 0, 1)
rf9 = gc.Item(
         "Red Flower", 716, 177, 50, 50, False, 0, 1)
                   
gatherables.append(cottonball1)
gatherables.append(cb2)
gatherables.append(cb3)
gatherables.append(cb4)
gatherables.append(cb5)
gatherables.append(cb6)
gatherables.append(cb7)
gatherables.append(rf1)
gatherables.append(rf2)
gatherables.append(rf3)
gatherables.append(rf4)
gatherables.append(rf5)
gatherables.append(rf6)
gatherables.append(rf7)
gatherables.append(rf8)
gatherables.append(rf9)

class GroundSprite():
    def __init__(self, sprite, location):
        self.icon = sprite
        self.location = location
        
ground_deco = []
at = (400, 60)
yf1 = GroundSprite(sprites.flower_yellow, at)
at = (376, 53)
yf2 = GroundSprite(sprites.flower_yellow, at)
at = (412, 36)
yf3 = GroundSprite(sprites.flower_yellow, at)
at = (115, 450)
yf4 = GroundSprite(sprites.flower_yellow, at)
at = (250, 419)
yf5 = GroundSprite(sprites.flower_yellow, at)
at = (677, 384)
yf6 = GroundSprite(sprites.flower_yellow, at)

at = (600, 400)
wf1 = GroundSprite(sprites.wood_floor_tile, at)
at = (640, 400)
wf2 = GroundSprite(sprites.wood_floor_tile, at)
at = (600, 440)
wf3 = GroundSprite(sprites.wood_floor_tile, at)
at = (640, 440)
wf4 = GroundSprite(sprites.wood_floor_tile, at)
at = (560, 400)
wf5 = GroundSprite(sprites.wood_floor_tile, at)
at = (560, 440)
wf6 = GroundSprite(sprites.wood_floor_tile, at)
at = (680, 400)
wf7 = GroundSprite(sprites.wood_floor_tile, at)
at = (680, 440)
wf8 = GroundSprite(sprites.wood_floor_tile, at)
at = (560, 480)
wf9 = GroundSprite(sprites.wood_floor_tile, at)
at = (600, 480)
wf10 = GroundSprite(sprites.wood_floor_tile, at)
at = (640, 480)
wf11 = GroundSprite(sprites.wood_floor_tile, at)
at = (680, 480)
wf12 = GroundSprite(sprites.wood_floor_tile, at)

        
ground_deco.append(yf1)
ground_deco.append(yf2)
ground_deco.append(yf3)
ground_deco.append(yf4)
ground_deco.append(yf5)
ground_deco.append(yf6)
#ground_deco.append(wf1)
#ground_deco.append(wf2)
#ground_deco.append(wf3)
#ground_deco.append(wf4)
#ground_deco.append(wf5)
#ground_deco.append(wf6)
#ground_deco.append(wf7)
#ground_deco.append(wf8)
#ground_deco.append(wf9)
#ground_deco.append(wf10)
#ground_deco.append(wf11)
#ground_deco.append(wf12)