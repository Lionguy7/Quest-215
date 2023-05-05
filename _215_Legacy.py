# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 13:19:34 2023

@author: alexe
"""
from boxmeta import BoxMeta as bm

def swap_slots(self, player, points):
    #Function that swaps 2 slots in the player's inventory
    
    swaps = [] #Container to hold slots
    
    #Loop to get the slot number of the first spot clicked
    i = 0
    found = False
    while not found and i < len(self.slots):
        if bm.containspoint(points[0], self.slots[i].hitbox): #If a slot contains the point,
            found = True
            swaps.append(int(self.slots[i].name)) #Add to swaps
            
        i += 1
    
    #Loop to get the slot number of the second spot clicked
    i = 0
    found = False  
    while not found and i < len(self.slots):
        if bm.containspoint(points[1], self.slots[i].hitbox): #If a slot contains the point,
            found = True
            swaps.append(int(self.slots[i].name)) #Add to swaps
            
        i += 1
        
    #If swaps has 2 slots from previous, this loop will be skipped.
    #Else, check the hotbar for a potential slot.
    i = 0
    found = False  
    while not found and i < len(self.hotbar):
        if bm.containspoint(points[1], self.hotbar[i].hitbox):
            found = True
            swaps.append(int(self.hotbar[i].name))
            
        i += 1
        
    #Debug print statement meta
    #print(swaps)
        
    #Found two existing slots
    if len(swaps) == 2:
        if swaps[0] != swaps[1]: #Are the slots the same? Yes: do nothing. No: swap
            if swaps[0] in player.inventory: #Does the first slot appear in the player's
                #inventory, i.e., does the player have an item in the slot?
                
                #If only first slot is in the inventory, and the second slot is not;
                #however, the second slot is also not a hotbar slot
                if (swaps[1] not in player.inventory
                    and swaps[1] not in player.hotbar):
                    #print("First is True")
                    name = player.inventory[swaps[0]]["name"] #get the item name
                    num = player.inventory[swaps[0]]["num"] #get the item amount
                    player.inventory.update({swaps[1]: #Add the new slot to the inventory
                        {"name": name, "num": num}})
        
                    del player.inventory[swaps[0]] #Delete the old slot
                    
        
                #The second slot is also in the player's inventory, i.e., they have
                #an item in both slots 1 and 2. (swaps[0] and swaps[1])
                elif swaps[1] in player.inventory:
                    #print("Second is True")
                    name_1 = player.inventory[swaps[0]]["name"] #Simplify variables
                    num_1 = player.inventory[swaps[0]]["num"]
                    name_2 = player.inventory[swaps[1]]["name"]
                    num_2 = player.inventory[swaps[1]]["num"]
                    if name_1 == name_2: #If the item has the same name,
                        #Increment the item amount and place in the SECOND slot.
                        player.inventory[swaps[1]]["num"] += num_1 
                        del player.inventory[swaps[0]] #Delete the old slot
                        
                    else:
                        #Trade the 2 slots' values
                        player.inventory[swaps[0]] = {"name": name_2, "num": num_2}
                        player.inventory[swaps[1]] = {"name": name_1, "num": num_1}
                        
                    
                #The first slot is in the player's inventory and the second slot
                #is in the player's hotbar
                elif swaps[1] in player.hotbar:
                    #print("Third is True")
                    
                    #Since the player's hotbar slots are always 25-30, their names
                    #are changed to "null" if no actual item is there
                    if player.hotbar[swaps[1]]["name"] == "null":
                        #print("It's null")
                        #Fill the hotbar slot with the inventory slot's item information
                        name = player.inventory[swaps[0]]["name"]
                        num = player.inventory[swaps[0]]["num"]
                        
                        player.hotbar[swaps[1]]["name"] = name
                        player.hotbar[swaps[1]]["num"] = num
                        
                        del player.inventory[swaps[0]] #Delete the old slot
                        
                    else:
                        #There exists an item in the hotbar slot
                        #print("It's not null")
                        
                        name_1 = player.inventory[swaps[0]]["name"] #Simplify variables
                        num_1 = player.inventory[swaps[0]]["num"]
                        name_2 = player.hotbar[swaps[1]]["name"]
                        num_2 = player.hotbar[swaps[1]]["num"]
                        
                        if name_1 == name_2: #If it's the same item in both slots
                            #Add the amount from the slot in the inventory to the amount
                            #in the hotbar
                            player.hotbar[swaps[1]]["num"] += num_1
                            del player.inventory[swaps[0]] #Delete the old slot
                            
                        else:
                            #Trade the 2 slots' values
                            player.hotbar[swaps[1]] = {"name": name_1, "num": num_1}
                            player.inventory[swaps[0]] = {"name": name_2, "num": num_2}
                                    
                                    
                                    
#Old class for Item, which has now been replace. Will delete this during refactoring and
#what not. o7 Legacy Code
"""class Item():
    alive_for = 0
    picked_up = False
    def __init__(self, name, icon, placeable, x, y, w, h, despawn_at, amt):
        self.name = name
        self.icon = icon
        self.placeable = placeable
        self.despawn_at = despawn_at
        self.x = x
        self.y = y
        self.hitbox = (x - 15, y - 15, w, h)
        self.amount = amt
        
    def display(self, window):
        self.alive_for += 1
        window.blit(self.icon, (self.x, self.y))
        #pygame.draw.rect(window, RED, self.hitbox, 
        
"""

""" 
#print(len(walls))
            #print(len(indexes))
                 
            #Sides = [Left, Right, Up, Down]
            #sides = [False, False, False, False]
            #placed = False
            #for w in walls:
                #if not placed:
                
                    if pos[0] == w.origin[0]:
                        print("At 1")
                        print(pos[1])
                        print(w.origin[1])
                        #To become BOTTOM RIGHT CORNER WALL
                        if pos[1] - 40 == w.origin[1]:
                            print("At 2")
                            
                            if (w.name == "Stone Wall Right"
                            or w.name == "Stone Wall Right Corner"):
                                print("At 3")
                                
                                obj_name = "Stone Wall Right Corner"
                                values = Items.items[obj_name]["hitbox"]
                                new_hitbox = (pos[0] + values[0],
                                  pos[1] + values[1], values[2], values[3])
                                
                                new_wall = GameClasses.Object(obj_name,
                                    Items.items[obj_name]["icon"],
                                    Items.items[obj_name]["type"], 4,
                                    
                                    (pos[0], pos[1]), new_hitbox, False)
                                objects.append(new_wall)
                                placed = True
                                
                            if (w.name == "Stone Wall Left"
                            or w.name == "Stone Wall Left Corner"):
                                print("At 4")
                                obj_name = "Stone Wall Left Corner"
                                values = Items.items[obj_name]["hitbox"]
                                new_hitbox = (pos[0] + values[0],
                                  pos[1] + values[1], values[2], values[3])
                                
                                new_wall = GameClasses.Object(obj_name,
                                    Items.items[obj_name]["icon"],
                                    Items.items[obj_name]["type"], 4,
                                    
                                    (pos[0], pos[1]), new_hitbox, False)
                                objects.append(new_wall)
                                placed = True
                                
                            if (w.name == "Stone Wall"
                            or w.name == "Stone Wall Right"):
                                print("At 8")
                                
                                obj_name = "Stone Wall Right"
                                values = Items.items[obj_name]["hitbox"]
                                new_hitbox = (pos[0] + values[0],
                                  pos[1] + values[1], values[2], values[3])
                                
                                new_wall = GameClasses.Object(obj_name,
                                    Items.items[obj_name]["icon"],
                                    Items.items[obj_name]["type"], 4,
                                    
                                    (pos[0], pos[1]), new_hitbox, False)
                                objects.append(new_wall)
                                placed = True
                                
                                
                        if pos[1] + 40 == w.origin[1]:
                            print("At 5")
                            if (w.name == "Stone Wall"
                            or w.name == "Stone Wall Right"):
                                
                                obj_name = "Stone Wall Right"
                                values = Items.items[obj_name]["hitbox"]
                                new_hitbox = (pos[0] + values[0],
                                  pos[1] + values[1], values[2], values[3])
                                
                                new_wall = GameClasses.Object(obj_name,
                                    Items.items[obj_name]["icon"],
                                    Items.items[obj_name]["type"], 4,
                                    
                                    (pos[0], pos[1]), new_hitbox, False)
                                objects.append(new_wall)
                                placed = True
                                
                            if (w.name == "Stone Wall"
                            or w.name == "Stone Wall Left"):
                                print("At 6")
                                obj_name = "Stone Wall Left"
                                values = Items.items[obj_name]["hitbox"]
                                new_hitbox = (pos[0] + values[0],
                                  pos[1] + values[1], values[2], values[3])
                                
                                new_wall = GameClasses.Object(obj_name,
                                    Items.items[obj_name]["icon"],
                                    Items.items[obj_name]["type"], 4,
                                    (pos[0], pos[1]), new_hitbox, False)
                                objects.append(new_wall)
                                placed = True
            
            if not placed: 
                print("At 7")
                obj_name = "Stone Wall"
                values = Items.items[obj_name]["hitbox"]
                new_hitbox = (pos[0] + values[0],
                  pos[1] + values[1], values[2], values[3])
                
                new_wall = GameClasses.Object(obj_name,
                    Items.items[obj_name]["icon"],
                    Items.items[obj_name]["type"], 4,
                    (pos[0], pos[1]), new_hitbox, False)
                objects.append(new_wall)
                placed = True          
               
                
                    if pos[0] == w.origin[0]:
                        if pos[1] == w.origin[1] - 40:
                            sides[3] = True
                            
                        if pos[1] == w.origin[1] + 40:
                            sides[2] = True
                            
                    if pos[1] == w.origin[1]:
                        if pos[0] == w.origin[0] - 40:
                            sides[1] = True
                            
                        if pos[0] == w.origin[0] + 40:
                            sides[0] = True
                        
            
            #Bottom Right Corner
            #Sides = [Left, Right, Up, Down]
            if sides[0] and sides[2] and not sides[3]:
                print("At 1")
                GameClasses.Wall.create_wall("Stone Wall Right Corner", pos, objects)
                placed = True
                
            if sides[0] and sides[3] and not sides[2]:
                print("At 2")
                GameClasses.Wall.create_wall("Stone Wall Right", pos, objects) #Should be Stone Wall Right Top Corner
                placed = True
                
            if sides[0] and sides[3] and sides[2]:
                print("At 3")
                GameClasses.Wall.create_wall("Stone Wall Right", pos, objects)
                placed = True
                
            if sides[3]:
                if not placed:
                    print("At 3.5")
                    GameClasses.Wall.create_wall("Stone Wall Left", pos, objects)
                    placed = True
                
            if sides[1] and sides[2] and not sides[3]:
                print("At 4")
                GameClasses.Wall.create_wall("Stone Wall Left Corner", pos, objects)
                placed = True
                
            if sides[1] and sides[3] and not sides[2]:
                print("At 5")
                GameClasses.Wall.create_wall("Stone Wall Left", pos, objects)
                placed = True
                
            if sides[0] and sides[3] and sides[2]:
                print("At 6")
                GameClasses.Wall.create_wall("Stone Wall Left", pos, objects)
                placed = True
                
            if sides[2]:
                if not placed:
                    print("At 6.5")
                    GameClasses.Wall.create_wall("Stone Wall Left", pos, objects)
                    placed = True

                
                
            if not placed:
                print("At 7")
                GameClasses.Wall.create_wall("Stone Wall", pos, objects)
"""

"""i = 1
            while i < 11:
                try:
                    if self.hotbar[i]["item"] == item.name:
                        self.hotbar[i]["amount"] += item.amount
                        item.picked_up = True
                        i += 10
                        
                except KeyError:
                    self.hotbar.update({i: {"item": item.name, "amount": item.amount}})
                    item.picked_up = True
                    i += 10
                    
                i += 1
"""
"""
            if ((coordinate[0] >= self.x)
            and (coordinate[0] <= self.x + self.collision_hitbox[2])
            and coordinate[1] <= self.collision_hitbox[1]):
                self.facing = "north"
                
            elif ((coordinate[0] >= self.x)
            and (coordinate[0] <= self.x + self.collision_hitbox[2])
            and coordinate[1] >= self.collision_hitbox[1]):
                self.facing = "south"
                
            elif coordinate[0] < self.x:
                self.facing = "left"
                
            elif coordinate[0] > self.x:
                self.facing = "right"
                
            if self.facing == "north":
                box = (self.x - 20, (self.collision_hitbox[1] - 65), 62, 65)
                
            elif self.facing == "right":
                box = (self.x + self.collision_hitbox[2], self.y - 20, 20, 90)
                
            elif self.facing == "left":
                box = ((self.collision_hitbox[0] - 20), self.y - 20, 20, 90)
                
            elif self.facing == "south":
                box = ((self.x - 20, self.collision_hitbox[1] + self.collision_hitbox[3], 62, 20))
            """
            
#pygame.draw.rect(window, RED, (pos[0], pos[1] + 10, 40, 30), 1)
            
        #if player.item == "Wood Gate":
            #window.blit(Sprites.wood_gate, (pos[0], pos[1]))
            #pygame.draw.rect(window, RED, (pos[0], pos[1], 40, 40), 1)
            
        #pygame.draw.rect(window, RED, (x_pos, pos[1] + 10, 40, 30), 1)
"""    
    if player.item == "Wood Gate":
        x_pos = (pos[0]) - (pos[0] % 40)
        y_pos = (pos[1]) - (pos[1] % 40)
        
    if player.item == "Left Wall":
        x_pos = (pos[0]) - (pos[0] % 40)
        y_pos = (pos[1]) - (pos[1] % 40)
        
    if player.item == "Right Wall":
        x_pos = (pos[0]) - (pos[0] % 40)
        y_pos = (pos[1]) - (pos[1] % 40)
    """
    
 #actions_tab = sprites.actions_tab
    #window.blit(actions_tab, (501, 0))
    #window.blit(sprites.inventory_tab, (501, 380))
    #if player.current_slot == 25: 
    #    window.blit(sprites.chosen_slot, (513, 387))
    #elif player.current_slot == 26:
    #    window.blit(sprites.chosen_slot, (560, 387))
    #elif player.current_slot == 27:
    #    window.blit(sprites.chosen_slot, (607, 387))
    #elif player.current_slot == 28:
    #    window.blit(sprites.chosen_slot, (654, 387))
    #elif player.current_slot == 29:
    #    window.blit(sprites.chosen_slot, (701, 387))
    #elif player.current_slot == 30:
    #    window.blit(sprites.chosen_slot, (513, 432))
    
def create_objects(sprites):
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
    
    at = (600, 100)
    rock4 = gc.Object("Rock Large", sprites.big_rock_pile, "minable", 4,
                      at, (at[0] + 11, at[1] + 50, 76, 20),
                      (at[0] + 10, at[1] + 25, 76, 50), True)
    
    at = (590, 30)
    rock5 = gc.Object("Rock Large", sprites.big_rock_pile, "minable", 4,
                      at, (at[0] + 11, at[1] + 50, 76, 20),
                      (at[0] + 10, at[1] + 25, 76, 50), True)
    
    at = (500, 20)
    rock6 = gc.Object("Rock Large", sprites.big_rock_pile, "minable", 4,
                      at, (at[0] + 11, at[1] + 50, 76, 20),
                      (at[0] + 10, at[1] + 25, 76, 50), True)
    
    at = (500, 230)
    tree1 = gc.Object("Tree Small", sprites.treeS, "chopable", 4,
                      at, (at[0] + 14, at[1] + 74, 18, 10),
                      (at[0] + 8, at[1] + 64, 30, 20), True)
    
    at = (10, 10)
    tree2 = gc.Object("Tree Large", sprites.treeL, "chopable", 4,
                      at, (at[0] + 30, at[1] + 157, 33, 10),
                      (at[0] + 20, at[1] + 127, 53, 40), True)
    
    at = (100, -15)
    tree3 = gc.Object("Tree Large", sprites.treeL, "chopable", 4,
                      at, (at[0] + 30, at[1] + 157, 33, 10),
                      (at[0] + 20, at[1] + 127, 53, 40), True)
    
    at = (75, 100)
    tree4 = gc.Object("Tree Apple", sprites.treeA, "chopable", 4,
                      at, (at[0] + 30, at[1] + 165, 30, 10),
                      (at[0] + 25, at[1] + 135, 40, 40), True)
    
    at = (2, 175)
    tree5 = gc.Object("Tree Large", sprites.treeL, "chopable", 4,
                      at, (at[0] + 30, at[1] + 157, 33, 10),
                      (at[0] + 20, at[1] + 127, 53, 40), True)
    
    at = (155, 70)
    tree6 = gc.Object("Tree Large", sprites.treeL, "chopable", 4,
                      at, (at[0] + 30, at[1] + 157, 33, 10),
                      (at[0] + 20, at[1] + 127, 53, 40), True)
    
    at = (200, 125)
    tree7 = gc.Object("Tree Large", sprites.treeL, "chopable", 4,
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
    tree13 = gc.Object("Tree Apple", sprites.treeA, "chopable", 4,
                      at, (at[0] + 30, at[1] + 165, 30, 10),
                      (at[0] + 25, at[1] + 135, 40, 40), True)
    
    at = (50, 250)
    tree14 = gc.Object("Tree Apple", sprites.treeA, "chopable", 4,
                      at, (at[0] + 30, at[1] + 165, 30, 10),
                      (at[0] + 25, at[1] + 135, 40, 40), True)
    
    objects.append(rock), objects.append(rock2), objects.append(rock3)
    objects.append(rock4), objects.append(rock5), objects.append(rock6)
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
    
    return objects

"""if saved_obj != None:
                diffx, diffy = bm.resolve(player.collision_hitbox,
                           saved_obj.hitbox,
                           player.blocked)"""
                
 #window.blit(sprites.rocks_on_sandLEND, (314, 220))
    #window.blit(sprites.rocks_on_sand, (442, 220))
    #window.blit(sprites.rocks_on_sand, (506, 220))
    #window.blit(sprites.rocks_on_sand, (570, 220))
    #window.blit(sprites.rocks_on_sand, (634, 220))
    #window.blit(sprites.rocks_on_sand, (698, 220))
    #window.blit(sprites.rocks_on_sand, (762, 220))
    #window.blit(sprites.flower_yellow, (400, 60))
    #window.blit(sprites.flower_yellow, (376, 53))
    #window.blit(sprites.flower_yellow, (412, 36))
    #window.blit(sprites.flower_yellow, (115, 450))
    #window.blit(sprites.flower_yellow, (250, 419))
    #window.blit(sprites.flower_yellow, (275, 384))
    #window.blit(sprites.flower_yellow, (677, 206))
    
"""for i in range(len(objects)):
                                if not added:
                                    if i == 0 and objects[0].hitbox[1] > new_hitbox[1]:
                                        objects.insert(0, new)
                                        added = True
                                        
                                    else:        
                                        if objects[i].hitbox[1] <= new_hitbox[1]:
                                            try:
                                                if objects[i + 1].hitbox[1] > new_hitbox[1]:
                                                    objects.insert(i + 1, new)
                                                    added = True
                                            except IndexError:
                                                if not added:
                                                    objects.append(new)
                                                    added = True"""
                                                    
#from collide bottom:
"""if ((agr[1] == res[1] + res[3])
            or (agr[1] <= res[1] + res[3] + a)):
            
            if not (agr[1] + agr[3] <= res[1]):
            
                if ((agr[0] >= res[0] and agr[0] <= res[0] + res[2])
                    or (agr[0] + agr[2] >= res[0] and agr[0] + agr[2] <= res[0] + res[2])
                    or (agr[0] >= res[0] and agr[0] + agr[2] <= res[0] + res[2])
                    or (res[0] >= agr[0] and res[0] + res[2] <= agr[0] + agr[2])
                    ):
                    bottom = True
                    """
                    
#from collidetop
"""if (agr[1] <= res[1] + res[3]) and (agr[1]  + agr[3] > res[1]):
            if (agr[0] + agr[2] > res[0]) and (agr[0] <  res[0] + res[2]):
                if agr[1] <= (res[1] + res[3]):
                    top = True"""
        
        
        """if ((agr[1] + agr[3] == res[1])
            or agr[1] + agr[3] >= res[1] + a):
            
            if not (agr[1] >= res[1] + res[3]):
            
                if ((agr[0] >= res[0] and agr[0] <= res[0] + res[2])
                    or (agr[0] + agr[2] >= res[0] and agr[0] + agr[2] <= res[0] + res[2])
                    or (agr[0] >= res[0] and agr[0] + agr[2] <= res[0] + res[2])
                    or (res[0] >= agr[0] and res[0] + res[2] <= agr[0] + agr[2])
                    ):
                    top = True
        """
#from collideright
"""      
        if ((agr[0] + agr[2] == res[0])
            or (agr[0] + agr[2] >= res[0] + a + 1)):
            
            if not (agr[0] >= res[0] + res[2]):
            
                if ((agr[1] <= res[1] + res[3] and agr[1] >= res[1])
                    or (agr[1] + agr[3] <= res[1] + res[3] and agr[1] + agr[3] >= res[1])
                    or (agr[1] >= res[1] and agr[1] + agr[3] <= res[1] + res[3])
                    or (res[1] >= agr[1] and res[1] + res[3] <= agr[1] + agr[3])
                    ):
                    left = True
                    """