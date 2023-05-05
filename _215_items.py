# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:52:19 2023

@author: Lionguy7
"""

from _215_sprites import Sprites
class Items():
    
    items = {
            
            "sword": {"icon": Sprites.sword, "offx": 0, "offy": 0, "placeable": False, "invoff": (0, -3)},
            
            "pickaxe": {"icon": Sprites.pickaxe, "offx": 0, "offy": 0, "placeable": False, "invoff": (7, 5)},
            
            "axe": {"icon": Sprites.axe, "offx": 0, "offy": 0, "placeable": False, "invoff": (7, 5)},
            
            "Rock": {"icon": Sprites.rock_drop, "offx": 0, "offy": 0, "placeable": False, "invoff": (13, 10)},
             
             "Log": {"icon": Sprites.log_pile, "offx": -15, "offy": -10, "placeable": False, "invoff": (0, -10)},
             
             "Cottonball": {"icon": Sprites.cottonball, "offx": -7, "offy": -15,
                            "placeable": False, "invoff": (8, -5)},
                            
             "Red Flower": {"icon": Sprites.flower_red, "offx": 0, "offy": 0,
                            "placeable": False, "invoff": (17, 13)},
            
            "Apple": {"icon": Sprites.apple, "offx": -7, "offy": -15,
               "placeable": False, "eat": True, "invoff": (9, 4), "heals": 5},
             
             
             "Stone Wall": {"icon": Sprites.stone_wall, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (4, 2),
                             "hitbox": (0, 30, 39, 10), "type": "minable", "drops": "Rock"},
                              
            "Stone Wall Left": {"icon": Sprites.stone_brick_left, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (-4, 4), "hitbox": (1, 1, 8, 39),
                             "type": "minable" , "drops": "Rock"},
                                
            "Stone Wall Left Bottom": {"icon": Sprites.stone_brick_left_bottom, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (-4, 4), "hitbox": (1, 3, 38, 37),
                             "type": "minable", "drops": "Rock"},
                                       
            "Stone Wall Left Top": {"icon": Sprites.stone_brick_left_top, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (-4, 4), "hitbox": (1, 30, 38, 10),
                             "type": "minable", "drops": "Rock"},
                          
            "Stone Wall Right": {"icon": Sprites.stone_brick_right, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (11, 4), "hitbox": (31, 1, 8, 39), 
                             "type": "minable", "drops": "Rock"},
                                 
            "Stone Wall Right Bottom": {"icon": Sprites.stone_brick_right_bottom, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (11, 4), "hitbox": (1, 3, 38, 37),
                             "type": "minable", "drops": "Rock"},
                                        
            "Stone Wall Right Top": {"icon": Sprites.stone_brick_right_top, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Rock": 4, "Crafting Bench": -1},
                             "amt": 1, "invoff": (11, 4), "hitbox": (0, 30, 38, 10),
                             "type": "minable", "drops": "Rock"},
                              
             "Wood Gate": {"icon": Sprites.wood_gate, "offx": 0, "offy": 0,
                             "placeable": True, "recipe": {"Wood Planks": 8, "Crafting Bench": -1},
                             "amt": 1, "invoff": (4, 2), "hitbox": (0, 30, 39, 10),
                             "type": "chopable", "drops": "Wood Planks"},
                           
            "Wood Gate Open": {"icon": Sprites.wood_gate_open, "offx": 0, "offy": 0,
                             "placeable": True,
                             "invoff": (4, 2), "hitbox": (0, 30, 39, 10),
                             "type": "chopable", "drops": "Wood Planks"},
                           
             "Wood Planks": {"icon": Sprites.wood_planks, "offx": -10, "offy": -10,
                             "placeable": False, "recipe": {"Log": 1}, "amt": 2, "invoff": (3, 0)},
                            
             "Stone Hammer": {"icon": Sprites.stone_hammer, "offx": 0, "offy": 0,
                             "placeable": False, "recipe": {"Wood Planks": 2, "Rock": 4, "Twine": 2},
                             "amt": 1, "invoff": (8, 5)},
                              
             "Twine": {"icon": Sprites.twine, "offx": 0, "offy": 0,
                             "placeable": False, "recipe": {"Cottonball": 5}, "amt": 2, "invoff": (10, 0)},
             
             "Crafting Bench": {"icon": Sprites.crafting_bench, "offx": 0, "offy": 0,
                             "placeable": False, "recipe":
                                 {"Wood Planks": 4, "Rock": 4, "Twine": 2, "Stone Hammer": -1},
                                 "amt": 1, "invoff": (3, -3)},
                 
            "Cabinet": {"icon": Sprites.cabinet2doors, "offx": 0, "offy": 0,
                             "placeable": True, "recipe":
                                 {"Wood Planks": 8, "Crafting Bench": -1},
                                 "amt": 1, "invoff": (5, 0),
                                 "hitbox": (3, 27, 33, 10),
                                 "type": "chopable", "drops": "Wood Planks"},
                
            "Bed": {"icon": Sprites.bed, "offx": 0, "offy": 0,
                             "placeable": True, "recipe":
                                 {"Wood Planks": 4, "Cottonball": 5, "Red Flower": 2, "Crafting Bench": -1},
                                 "amt": 1, "invoff": (4, -1),
                                 "hitbox": (1, 15, 38, 25),
                                 "type": "chopable", "drops": "Wood Planks"},
                
             "Table": {"icon": Sprites.table, "offx": 0, "offy": 0,
                             "placeable": True, "recipe":
                                 {"Wood Planks": 6, "Crafting Bench": -1},
                                 "amt": 1, "invoff": (4, -1),
                                 "hitbox": (1, 15, 38, 25),
                                 "type": "chopable", "drops": "Wood Planks"},
                 
            "Wardrobe": {"icon": Sprites.wardrobe, "offx": 0, "offy": 0,
                             "placeable": True, "recipe":
                                 {"Wood Planks": 10, "Crafting Bench": -1},
                                 "amt": 1, "invoff": (5, 4),
                                 "hitbox": (3, 15, 33, 24),
                                 "type": "chopable", "drops": "Wood Planks"},
                
            "Floor Tile Wood": {"icon": Sprites.wood_floor_tile, "offx": 0, "offy": 0,
                             "placeable": True, "recipe":
                                 {"Wood Planks": 5, "Crafting Bench": -1},
                                 "amt": 1, "invoff": (5, 4),
                                 "hitbox": 0,
                                 "type": "chopable", "drops": "Wood Planks"}
             }
