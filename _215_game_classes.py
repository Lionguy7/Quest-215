# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 11:10:02 2023

@author: Lionguy7
"""

import pygame
import random
from boxmeta import BoxMeta as bm
from _215_items import Items


#Globals/CONSTANTS
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
FPS = 30

class GameClasses():

    class Player():
        blocked = [False, False, False, False] #Which directions are blocked (for movement)
        placing = False #If the player's item can be placed/if they are placing it
        walking = False #If W, A, S, or D is pressed on this tick
        dead = False #If the player is, well, dead
        animation_lock = False #If the playing animation disables movement or not (default False)
        
        _cooldown = 0 #Cooldown upon swing (and hit) 
        current_slot = 25 #Current slot in player's hotbar
        click_flag = 0 #If the player has left clicked in on this tick
        right_click_flag = 0 #If the player has right clicked in this tick
        health = 1 #Player's health
        max_health = 20 #Player's maximum hp
        animation_tick = 0 #Counts of ticks to determine end/reset of animation
        frame = 0 #Index of the current animation. Advances 1 every 3 ticks 
        death_state = 0 #What stage of death the player is on. See self.die() for more.
        walk_frame = 0 #Animation tick special case, for walking animations only.
        walk_frame_tick = 0 #Frame, but for walking animations
        stopper = 0 #Helps stop walking animation, but not instantly reset any other
        stamina = 5 * FPS #How long the player can sprint (hold SHIFT) for.
        
        hotbar = {25: {"name":"sword", "num": 1},    #The 6 slots displayed at the bottom
               26: {"name": "pickaxe", "num": 1},    #of the game screen, that holds which
               27: {"name": "axe", "num": 1},        #items the player can interact with/use
               28: {"name": "Apple", "num": 20},       #during gameplay.
               29: {"name": "Stone Wall", "num": 99},
               30: {"name": "null", "num": 3}
               }
        
        #A dictionary of the player's items.
        #Format: {<inventory_slot>: "name": "item name", "num": amount the player has}
        inventory = {1: {"name":"Rock", "num": 99},
                     2: {"name":"Log", "num": 99},
                     3: {"name":"Cottonball", "num": 99},
                     4: {"name":"Red Flower", "num": 99},
                     5: {"name":"Floor Tile Wood", "num": 99},
        }
        
        item = "sword" #Player's current item, i.e., what item is used upon click/right click
        
        
        """ ========== Player Animations ==========
        ===========================================
        """
        standing_left = [pygame.image.load("standingl1.png"), pygame.image.load("standingl1.png"),
                         pygame.image.load("standingl2.png"), pygame.image.load("standingl2.png"),
                         pygame.image.load("standingl3.png"), pygame.image.load("standingl3.png"),
                         pygame.image.load("standingl2.png"), pygame.image.load("standingl2.png"),
                         pygame.image.load("standingl1.png"), pygame.image.load("standingl1.png")]
        
        standing_right = [pygame.image.load("standingr1.png"), pygame.image.load("standingr1.png"),
                          pygame.image.load("standingr2.png"), pygame.image.load("standingr2.png"),
                          pygame.image.load("standingr3.png"), pygame.image.load("standingr3.png"),
                          pygame.image.load("standingr2.png"), pygame.image.load("standingr2.png"),
                          pygame.image.load("standingr1.png"), pygame.image.load("standingr1.png")]
        
        walking_left = [pygame.image.load("walkingl1.png"), pygame.image.load("walkingl2.png"),
                        pygame.image.load("walkingl3.png"), pygame.image.load("walkingl4.png"),
                        pygame.image.load("walkingl5.png"), pygame.image.load("walkingl6.png"),
                        pygame.image.load("walkingl7.png"), pygame.image.load("walkingl8.png")]
        
        walking_right = [pygame.image.load("walkingr1.png"), pygame.image.load("walkingr2.png"),
                         pygame.image.load("walkingr3.png"), pygame.image.load("walkingr4.png"),
                         pygame.image.load("walkingr5.png"), pygame.image.load("walkingr6.png"),
                         pygame.image.load("walkingr7.png"), pygame.image.load("walkingr8.png")]
        
        pickaxe_left = [pygame.image.load("pickl1.png"), #pygame.image.load("pickl1.png"),
                        pygame.image.load("pickl2.png"), pygame.image.load("pickl3.png"),
                        pygame.image.load("pickl4.png"), pygame.image.load("pickl4.png")]
        
        pickaxe_right = [pygame.image.load("pickr1.png"), #pygame.image.load("pickr1.png"),
                         pygame.image.load("pickr2.png"), pygame.image.load("pickr3.png"),
                         pygame.image.load("pickr4.png"), pygame.image.load("pickr4.png")]
        
        axe_left = [pygame.image.load("axel1.png"), #pygame.image.load("axel1.png"),
                    pygame.image.load("axel2.png"), pygame.image.load("axel3.png"),
                    pygame.image.load("axel4.png"), pygame.image.load("axel4.png")]
        
        axe_right = [pygame.image.load("axer1.png"), #pygame.image.load("axer1.png"),
                    pygame.image.load("axer2.png"), pygame.image.load("axer3.png"),
                    pygame.image.load("axer4.png"), pygame.image.load("axer4.png")]
        
        sword_left = [pygame.image.load("swswingl1.png"), pygame.image.load("swswingl2.png"),
                      pygame.image.load("swswingl3.png"), pygame.image.load("swswingl4.png")]
        
        sword_right = [pygame.image.load("swswingr1.png"), pygame.image.load("swswingr2.png"),
                      pygame.image.load("swswingr3.png"), pygame.image.load("swswingr4.png")]
        
        eating_left = [pygame.image.load("eatingl1.png"), pygame.image.load("eatingl2.png"),
                      pygame.image.load("eatingl3.png"), pygame.image.load("eatingl4.png"),
                      pygame.image.load("eatingl5.png"), pygame.image.load("eatingl6.png"),
                      pygame.image.load("eatingl7.png"), pygame.image.load("eatingl8.png")]
        
        eating_right = [pygame.image.load("eatingr1.png"), pygame.image.load("eatingr2.png"),
                      pygame.image.load("eatingr3.png"), pygame.image.load("eatingr4.png"),
                      pygame.image.load("eatingr5.png"), pygame.image.load("eatingr6.png"),
                      pygame.image.load("eatingr7.png"), pygame.image.load("eatingr8.png")]
        
        death = [pygame.image.load("dying1.png"), pygame.image.load("dying2.png"),
                     pygame.image.load("dying3.png"),pygame.image.load("dying4.png"),
                     pygame.image.load("dying5.png"),pygame.image.load("dying6.png"),
                     pygame.image.load("dying7.png"),pygame.image.load("dying8.png")]
        
        animation = standing_left #Current animation, as list of images
        an_off = [-4, 0] #Offset to add to current animation's X/Y coordinates to "center" them
        
        def __init__(self, x, y):
            self.spawnpoint = [x, y] #Where the player respawns at
            self.x = x #Player's X Coordinate
            self.y = y #Player's Y Coordinate
            self.vel = 1 #Amount of pixels per frame the Player moves
            self.half_vel = -1 #Half of the amount of pixels per frame the Player moves, minus 1 (Disused)
            self.hitbox = (x, y, 22, 50) #Player's Hitbox (should match Sprite) - no it shouldn't
            self.collision_hitbox = (x, y + 40, 50, 9)
            self.rect = pygame.Rect(self.hitbox)
            self.facing = "left"
            self.animation_facing = "left" #Direction of animation
            self.change_animation = False #Whether or not the animation should be changed
            self.stop_animation_at = -1 #When the animation automatically stops
        
        def display(self, window):
            if not self.dead:
                if not self.walking:
                    #Upon walking = False, stopper is incremented by 1 to
                    #force an animation change. Then it is incremented again
                    #so the animation isn't changed again until it needs to be;
                    #the player clicks, starts moving again, or dies.
                    
                    self.stopper += 1
                    if self.stopper == 1 and not self.animation_lock:
                        self.change_animation = True
                        
                    #----------------------------------------------------------
                        
                    self.walk_frame = 0 #Reset these variables as they are no longer in use
                    self.walk_frame_tick = 0
                    
                    if self.animation_tick == 27: #For 'infinite' animations, this resets the frame
                        self.animation_tick = 0
                        self.frame = 0
                        
                    if self.animation_tick % 3 == 0: #The frame is incremented every 3 game ticks
                        self.frame += 1
                    
                else:
                    #Since the player is walking, the walking variables will be used
                    self.walk_frame_tick += 1
                    
                    if self.walk_frame_tick % 3 == 0: #Increment frame
                        self.walk_frame += 1
                    
                    if self.walk_frame >= self.stop_animation_at: #A full walking cycle
                        self.walk_frame = 0                       #has been completed
                        self.walk_frame_tick = 0
                        self.change_animation = True #Look for a new animation
                    
                if not self.walking:                     #(non walking) -v
                    if self.frame == self.stop_animation_at: #The current animation has ended
                        self.change_animation = True #Look for a new animation
                    
                #Hey look a debugging statement
                #print(self.frame)
                
                #Look for a new animation
                if self.change_animation:
                    self.animate()
                
                #Place shadow
                window.blit(pygame.image.load("shadow.png"), (self.x - 14,
                                                                self.y + 6))
                if not self.walking: #Place non-walking animation
                    window.blit(self.animation[self.frame],
                                (self.x + self.an_off[0],
                                 self.y + self.an_off[1]))
                    
                else: #Place walking animation
                    window.blit(self.animation[self.walk_frame],
                                      (self.x + self.an_off[0],
                                       self.y + self.an_off[1]))
                
                self.hitbox = (self.x, self.y, 22, 50) #Readjust Player's hitbox(s).
                self.collision_hitbox = (self.x - 1, self.y + 46, 22, 5)
                self.animation_tick += 1 #Increment tick
        
        def display_hotbar(self, window, sprites, font):
            window.blit(sprites.hotbar, (240, 442))
            positions = {1: 240, 2: 288, 3: 336, 4: 384, 5: 432, 6: 480}
            
            y = 442
            for m in self.hotbar:
                x = positions[m - 24]
                if self.hotbar[m]["name"] != "null":                
                    n = Items.items[self.hotbar[m]["name"]]
                    window.blit(n["icon"], (
                            x + n["invoff"][0],
                            y + n["invoff"][1]))
                    
                    #pygame.draw.rect(window, RED, (x, y, 48, 48), 1)
                    
                    if self.hotbar[m]["num"] > 1:
                        window.blit(font.render(str(self.hotbar[m]["num"]),
                                            True, BLACK), (x + 20,y + 30))
                    x += 48
                    
                if m == self.current_slot:
                        window.blit(sprites.chosen_slot, (positions[m - 24] - 2, y - 2))
                        
        def display_health(self, window, sprites):
            
            window.blit(sprites.hearts_bg, (3, -15))
            y = 10
            x = 10
            i = 5
            while i < 21:
                if i <= self.health:
                    window.blit(sprites.heart, (x, y))
                    
                else:
                    window.blit(sprites.empty_heart, (x, y))
                        
                i += 5
                x += 52
            
        def change_item(self):
            #Function to change player's current item
            if self.current_slot in self.hotbar:
                self.item = self.hotbar[self.current_slot]["name"]
                #print(self.item)
                
        def activate_cooldown(self, add = 0):
            #Function that initalizes the player's cooldown. Does not really need its own function
            if self._cooldown == 0:
                self._cooldown = (1 * FPS) + add
            
        def cooldown(self):
            #Function that decrements the player's cooldown, if it [the cooldown] is active
            if self._cooldown > 0:
                self._cooldown -= 1
                
                
        def get_hit_range(self, window):
            #Function that determines which direction the player is facing,
            #based on the mouse's current position
            
            coordinate = pygame.mouse.get_pos() #Get the mouses's current position
            
            #Get the direction
            if coordinate[0] <= self.x + 10:
                self.facing = "left"
            else:
                self.facing = "right"
                
            #Create the hit range box, based on the direction
            if self.facing == "right":
                box = (self.x + 10, self.y - 20, 30, 90)
                
            if self.facing == "left":
                box = ((self.collision_hitbox[0] - 20), self.y - 20, 30, 90)
                
            pygame.draw.rect(window, GREEN, box, 1)
            pygame.draw.rect(window, RED, (self.hitbox), 1)
            pygame.draw.rect(window, RED, (self.collision_hitbox), 1)
            
            return box
        
        def get_sprite(self, sprites):
            #Function that returns the sprite of the player's current item
            return Items.items[self.item]["icon"]
        
        
        def pickup_item(self, item):
            found = False
            for slot in self.inventory:
                if self.inventory[slot]["name"] == item.name:
                    self.inventory[slot]["num"] += item.amount
                    found = True
                    item.picked_up = True
                
            i = 0
            while not found:
                i += 1
                if i not in self.inventory:
                    self.inventory.update({i: {"name": item.name,
                                               "num": item.amount}})
                    found = True
                    item.picked_up = True
                    
            #print(self.inventory)
            
            
        def remove_item(self):
            #Function to remove/decrement an item/amount from the player's hotbar
            item = self.item
            for i in self.hotbar: #Find the item in the player's hotbar
                if self.hotbar[i]["name"] == item:
                    self.hotbar[i]["num"] -= 1
                    if self.hotbar[i]["num"] == 0:
                        self.hotbar[i]["name"] = "null" #Reset the item if amount is 0
                        self.item = "null"
                        
                        
        def can_place(self):
            #Function that determines if the player's current item is placeable
            state = False
            if self.item != "null": #If the item exists
                if Items.items[self.item]["placeable"] is True: #Decided by Items class 
                    state = True
                
            return state
        
        
        def can_eat(self, chat):
            try:
                if not self.animation_lock:
                    if Items.items[self.item]["eat"]:
                        gain = Items.items[self.item]["heals"]
                        if self.health < self.max_health:
                            if self.health + gain <= self.max_health:
                                self.health += gain
                                chat.add("Player ate {}".format(self.item))
        
                            else:
                                
                                self.health = self.max_health
                            self.remove_item()
                            if self.animation_facing == "left":
                                self.animation = self.eating_left
                                self.an_off = [-4, 0]
                            if self.animation_facing == "right":
                                self.animation = self.eating_right
                                self.an_off = [-6, 0]
                            
                            self.reset_animation(8, True)
                        
                        
            except KeyError:
                pass
                    
        def interact(self, objects):
            #Function that determines what kind of interact has taken place
            #So only 1 interaction per left/right click. Currently an unused stub
            return
        
                        
        def animate(self):
            #Function for changing Player's animation
            #Looks at: which direction player is facing,
            #what item the player is currently holding,
            #whether or not the player has left/right clicked
            #If the player is walking, running, or not in motion
            #Based on these criteria, an animation is chosen
            
            if self.animation_facing == "left": #Direction
                if self._cooldown == 1 * FPS: #Whether or not the player has clicked
                    self.walking = False
                    if self.item == "pickaxe": #What item the player is holding
                        self.animation = self.pickaxe_left #Assign the correct animation
                        self.reset_animation(5, True) #Initialze animation stuff. Pass frames, lock
                        self.an_off = [-23, -30] #Animation offset, so player remains in the same place.
                                                 #Animations may have different sprite sizes
                        
                    if self.item == "axe":
                        self.animation = self.axe_left
                        self.reset_animation(5, True)
                        self.an_off = [-27, -30]
                        
                    if self.item == "sword":
                        self.animation = self.sword_left
                        self.reset_animation(4, True)
                        self.an_off = [-33, -27]
                        
                else:
                    if self.walking:
                        self.animation = self.walking_left
                        self.reset_animation(8)
                        self.an_off = [-4, 0]
                        
                    else:
                        self.animation = self.standing_left
                        self.reset_animation(-1)
                        self.an_off = [-4, 0]
                    
            if self.animation_facing == "right":
                #print("right")
                if self._cooldown == 1 * FPS:
                    self.walking = False
                    if self.item == "pickaxe":
                        self.animation = self.pickaxe_right
                        self.reset_animation(5, True)
                        self.an_off = [-7, -30]
                        
                    if self.item == "axe":
                        self.animation = self.axe_right
                        self.reset_animation(5, True)
                        self.an_off = [-3, -30]
                    
                    if self.item == "sword":
                        self.animation = self.sword_right
                        self.reset_animation(4, True)
                        self.an_off = [-4, -27]
                        
                else:
                    if self.walking:
                        self.animation = self.walking_right
                        self.reset_animation(8)
                        self.an_off = [-6, 0]
                        
                    else:
                        self.animation = self.standing_right
                        self.an_off = [-6, 0]
                        self.reset_animation(-1)
                        
                        
        def reset_animation(self, stop, lock = False):
            #Function to "reset" animation - actually acts more like an animation initialization
            self.change_animation = False #Selected new animation, so don't need to look for one
            self.frame = 0 #Reset the frame for the new animation
            self.animation_tick = 0 #Reset tick counter for frames/animation whatnot
            self.animation_lock = lock #Defaulted False, whether or not the animation allows
                                       #movement while it's playing  
            self.stop_animation_at = stop #How many frames the animation has
            
            
        def die(self, window, sprites):
            #Function that plays the death animation. Half in main, half here
            self.dead = True #Player is dead
            self.animation_tick += 1 #Increase animation_tick for the animation, obviously
            
            if self.animation_tick % 3 == 0: #Increase animation frame
                self.frame += 1
                     
            #Place player's sprite
            window.blit(self.death[self.frame], (self.x - 20, self.y - 50))
            
            #If the death animation has ended, increase the "state" of death
            #There are 3 stages. 0 -> alive. 1 -> just died. 3 -> death animation is finished
            if self.frame == 7:
                self.death_state = 3
    
                
        def reset_death(self):
            #Function that basically resets game/player upon player respawning
            self.dead = False
            self.health = 5
            self.death_state = 0
            self.frame = 0
            self.animation_tick = 0
            self.x = self.spawnpoint[0]
            self.y = self.spawnpoint[1]
            #Reset inventory and hotbar
            

    """ END OF CLASS PLAYER
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
START OF CLASS SLIME """
                
    class Slime():
        following = False
        dead = False
        knocked_back = False
        
        anger_level = 0
        respawn_at = 0
        move_time = 0
        move_seconds = random.randint(2, 5)
        new_x = 0
        new_y = 0
        attack_cooldown = 0
        animation_tick = 0
        frame = 0
        kb_time = 0
        
        ignored = ["Wood Gate Open"]
        
        left_passive = [
        pygame.image.load("slime_dude1lp.png"), pygame.image.load("slime_dude2lp.png"),
        pygame.image.load("slime_dude3lp.png"), pygame.image.load("slime_dude4lp.png"),
        pygame.image.load("slime_dude5lp.png"), pygame.image.load("slime_dude4lp.png"),
        pygame.image.load("slime_dude3lp.png"), pygame.image.load("slime_dude2lp.png")
        ]
        
        left_angry = [
        pygame.image.load("slime_dude1la.png"), pygame.image.load("slime_dude2la.png"),
        pygame.image.load("slime_dude3la.png"), pygame.image.load("slime_dude4la.png"),
        pygame.image.load("slime_dude5la.png"), pygame.image.load("slime_dude4la.png"),
        pygame.image.load("slime_dude3la.png"), pygame.image.load("slime_dude2la.png")
        ]
        
        right_passive = [
        pygame.image.load("slime_dude1rp.png"), pygame.image.load("slime_dude2rp.png"),
        pygame.image.load("slime_dude3rp.png"), pygame.image.load("slime_dude4rp.png"), 
        pygame.image.load("slime_dude5rp.png"), pygame.image.load("slime_dude4rp.png"), 
        pygame.image.load("slime_dude3rp.png"), pygame.image.load("slime_dude2rp.png")
        ]
        
        right_angry = [
        pygame.image.load("slime_dude1ra.png"), pygame.image.load("slime_dude2ra.png"), 
        pygame.image.load("slime_dude3ra.png"), pygame.image.load("slime_dude4ra.png"),
        pygame.image.load("slime_dude5ra.png"), pygame.image.load("slime_dude4ra.png"),
        pygame.image.load("slime_dude3ra.png"), pygame.image.load("slime_dude2ra.png")
        ]
    
        animation = left_passive
        emotion = "passive"
        facing = "left"
        
        shadow = pygame.image.load("slime_shadow.png")
        
        def __init__(self, i, ia, h, x, y):
            self.icon = i
            self.icon_angry = ia
            self.maxhealth = h
            self.health = h
            self.aware_range = 60
            self.velocity = 1
            self.spawn = (x, y)
            self.x = x
            self.y = y
            self.hitbox = (x, y, 32, 22)
            self.aware_box = (self.hitbox[0] - self.aware_range / 2,
                             self.hitbox[1] - self.aware_range / 2,
                             self.hitbox[2] + self.aware_range,
                             self.hitbox[3] + self.aware_range)
            
            self.blocked = [False, False, False, False]
            self.previous = [0, 0]
            self.stuck_count = []
            
        def display(self, window, objects, border):
            #Function for displaying Slime
            
            if self.animation_tick == 24: #Loop tick
                self.animation_tick = 0
                
            if self.animation_tick % 3 == 0: #Increase frame
                self.frame += 1
                if self.frame == 8: #Reset frame at the animation's end
                    self.frame = 0
                
            if self.health <= 0: #Check if the Slime has perished
                if not self.dead: #Activates ONLY on the FIRST TICK the Slime hs <= health
                    self.dead = True
                    self.respawn_at = 5 * FPS #Respawn timer
                    self.following = False
                    self.anger_level = 0
                
                else: #The Slime is currently dead, so decrease its respawn timer
                    self.respawn_at -= 1
                    
                if self.respawn_at == 0: #The Slime's respawn time is up
                    self.following = False
                    self.dead = False
                    self.health = self.maxhealth #Reset HP
                    self.anger_level = 0
                    self.attack_cooldown = 2 * FPS
                    self.x = self.spawn[0] #Back to spawnpoint
                    self.y = self.spawn[1]
                    
            else: #The Slime is alive
                
                #Choose Slime's emotion (for animation)
                if self.anger_level > 1 * FPS or self.following:
                    self.emotion = "angry"
                else:
                    self.emotion = "passive"
                    
                #Check Slime's movement, to obtain which direction the Slime is moving
                if not self.knocked_back:
                    self.movement(objects, border)
                else:
                    self.get_hit(objects, border)
                
                #Choose an animation based on the Slime's emotion and direction
                if self.emotion == "passive":
                    if self.facing == "left":
                        self.animation = self.left_passive
                    if self.facing == "right":
                        self.animation = self.right_passive
                        
                else:
                    if self.facing == "left":
                        self.animation = self.left_angry
                    if self.facing == "right":
                        self.animation = self.right_angry
                        
                window.blit(self.shadow, (self.x - 7, self.y + 5))
                    
                window.blit(self.animation[self.frame], (self.x - 10,
                            self.y - 14)) #Draw the sprite to the Pygame window
                
                #Readjust hitbox and aware range, because of the Slime's movement
                self.hitbox = (self.x, self.y, 32, 22)
                self.aware_box = (self.hitbox[0] - self.aware_range / 2,
                                 self.hitbox[1] - self.aware_range / 2,
                                 self.hitbox[2] + self.aware_range,
                                 self.hitbox[3] + self.aware_range)
                
                pygame.draw.rect(window, RED, self.hitbox, 1)
                pygame.draw.rect(window, GREEN, self.aware_box, 1)
                
                self.animation_tick += 1 #Increase animation tick
            
        def check_for_player(self, player, objects, chat):
            #Function that determines if the Player is in range of the Slime
            
            if self.following: #If the Slime is following player, it doesn't need to check
                self.follow_player(player, objects, chat)
                
            else: #The Slime is not following the player
                if bm.collisions(player.hitbox, self.aware_box): #If the player is in the aware range
                    self.attack(player, chat) #Try attacking first
                    
                    if self.anger_level <= 2 * FPS: #Not angry enough to follow
                        if not self.following: #Should always be True, in this case
                            self.anger_level += 1 #Increase anger
                        
                    else: #The Slime is now angry enough to follow the player
                        self.following = True
                        self.move_time = 0
                        
                else: #The player is not in range
                    if self.anger_level > 0: #If angry...,
                        self.anger_level -= 1 #...cooldown
                
                
        def follow_player(self, player, objects, chat):
            #Function that makes Slime follow player
            
            if self.anger_level > 0: #Attack, obviously
                self.attack(player, chat)
                
                self.anger_level -= 1 #Cooldown anger
                self.blocked = self.get_blocked_directions(objects) #Get blocked directions
                    
                #If not blocked, follow the player's X
                if player.x < self.x:
                    if not self.blocked[0]:
                        self.x -= 1
                elif player.x > self.x:
                    if not self.blocked[1]:
                        self.x += 1
                else:
                    pass
                    
                #If not blocked, follow the player's Y
                if player.y < self.y:
                    if not self.blocked[2]:
                        self.y -= 1  
                elif player.y > self.y:
                    if not self.blocked[3]:
                        self.y += 1 
                else:
                    pass
                
                self.blocked = [False, False, False, False]
                
            else: #The Slime has been following for 2 seconds, and not attacked...,
                self.following = False #...so it is no longer interested in the player
                
        def movement(self, objects, border):
            #Function that generates the Slime's random movement, when not following
            self.move_time += 1 #Ticks the Slime has been moving for
            
            if not self.following:
                #After a certain amount of time, the Slime will change its direction
                if self.move_time > self.move_seconds * FPS:
                    self.new_x = random.randint(-1, 1) #Choose new direction
                    self.new_y = random.randint(-1, 1)
                    self.move_time = 0
                    self.move_seconds = random.randint(2, 5) #Choose new amount of time to move for
                    
                #Find out if the Slime is blocked, in any direction.
                self.blocked = self.get_blocked_directions(objects)
                
                #Move and adjust direction (for animation)
                if self.new_x > 0:
                    if not self.blocked[1] and self.x + self.hitbox[2] < border.right:
                        self.x = self.x + 1
                        self.facing = "right"
                        
                if self.new_x < 0:
                    if not self.blocked[0] and self.x > border.left:
                        self.x = self.x - 1
                        self.facing = "left"
                        
                if self.new_y < 0:
                    if not self.blocked[2] and self.y > border.top:
                        self.y = self.y - 1
                
                if self.new_y > 0:
                    if not self.blocked[3] and self.y + self.hitbox[3] < border.bottom:
                        self.y = self.y + 1

                #This is in the event of the Slime getting stuck. If it has not moved in 9 seconds,
                #it will kill itself and respawn at its spawnpoint in 1 second.
                if (self.x == self.previous[0]
                    and self.y == self.previous[1]):
                        self.stuck_count.append(1)
                        
                        if len(self.stuck_count) > 9 * FPS:
                            print("True")
                            self.stuck_count = []
                            self.health = (self.maxhealth + 1) * -1
                            self.respawn_at = 1 * FPS
                            self.following = False
                        
                else: #The Slime has moved X/Y in the past 9 seconds, and is not stuck.
                    self.previous[0] = self.x
                    self.previous[1] = self.y
                    self.stuck_count = []
                    
                self.blocked = [False, False, False, False]
                
        def attack(self, player, chat):
            #Function for the Slime attacking the player
            if not self.dead: #Don't want dead mobs to attack, obviously
                if self.attack_cooldown > 0: #If the Slime has attacked recently
                    self.attack_cooldown -= 1 #Lower cooldown, in game ticks
                    
                if self.attack_cooldown == 0: #Slime can attack, and is not on attack cooldown
                    if bm.collisions(player.hitbox, self.hitbox): #If the Slime can hit the player
                        player.health -= 5 #Reduce player's hp
                        self.following = False #Slime has attacked, and has lost interest in the player
                        self.move_time = 0
                        self.anger_level = 0 #Slime is no longer angry
                        self.attack_cooldown = 4 * FPS #Initialize Slime's attack cooldown
                        chat.add("Player took damage") #Add a message to chat in bottom left
                        
        def get_hit(self, objects, border):
            self.following = False
            
            if self.kb_time == int(FPS / 2):
                self.move_time = 0
                self.anger_level += 2 * FPS
                
            if self.kb_time > 0:
                self.kb_time -= 1
                self.blocked = self.get_blocked_directions(objects)       
                                
                if self.new_x > 0:
                    if not self.blocked[1] and self.x + self.hitbox[2] < border.right:
                        self.x = self.x + 1
                        
                if self.new_x < 0:
                    if not self.blocked[0] and self.x > border.left:
                        self.x = self.x - 1
                        
                if self.new_y < 0:
                    if not self.blocked[2] and self.y > border.top:
                        self.y = self.y - 1
                
                if self.new_y > 0:
                    if not self.blocked[3] and self.y + self.hitbox[3] < border.bottom:
                        self.y = self.y + 1
                        
            else:
                self.kb_time = 0
                self.new_y *= -1
                self.new_x *= -1
                self.knocked_back = False
                
        def get_blocked_directions(self, objects):
            #Function that determines which directions are blocked.
            #Was copy paste but I made it a function cause I used it 3 times and
            #this makes the code slightly shorter
            
            status = [False, False, False, False]
            for obj in objects:
                #Left, Right, Up, Down
                if not obj.destroyed:
                    if obj.name not in self.ignored:
                        if bm.collideright(tuple(self.hitbox), obj.hitbox):
                            status[0] = True
                            
                        if bm.collideleft(tuple(self.hitbox), obj.hitbox):
                            status[1] = True
                            
                        if bm.collidebottom(tuple(self.hitbox), obj.hitbox):
                            status[2] = True
                        
                        if bm.collidetop(tuple(self.hitbox), obj.hitbox):
                            status[3] = True
                                
            return status
            
                
        def find_knockback_direction(self, player):
            if player.collision_hitbox[0] + player.collision_hitbox[2] < self.x:
                self.new_x = 1
                
            elif player.collision_hitbox[0] > self.x:
                self.new_x = -1
                
            else:
                self.new_x = 0
                
            if player.collision_hitbox[1] + player.collision_hitbox[3] < self.y:
                self.new_y = 1
                
            elif player.collision_hitbox[1] > self.y:
                self.new_y = -1
                
            else:
                self.new_y = 0
            
   
    """ END OF CLASS SLIME
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
        START OF CLASS SOUND EFFECTS """
        
    class SoundEffects():
        #Class for Sound Effects
        #What more do I need to say
        pygame.mixer.init()
        pickaxe_on_rock = pygame.mixer.Sound("pickaxe_on_rock.mp3")
        axe_on_wood = pygame.mixer.Sound("axe_on_wood.mp3")
        air_swipe = pygame.mixer.Sound("swipe_in_air.mp3")
        wood_gate_open = pygame.mixer.Sound("wood_gate_open.mp3")
        wood_gate_close = pygame.mixer.Sound("wood_gate_close.mp3")
        #sword_hit_slime = pygame.mixer.Sound("sword_hit.mp3")
        
    """ END OF CLASS SOUND EFFECTS
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
        START OF CLASS OBJECTS """
        
    class Object():
        #Class for Objects, that have hitboxes and an area
        seconds_count = 0 #How long an object has been dead for
        respawn_at = 20 * FPS #When an object respawns, if it does
        destroyed = False #If an object is destroyed, i.e., it won't have an area
        obj_type = "" #What tool can be used to destroy the object
        hitbox = (0,0,0,0) #Where the object is place, and how large it is
        
        #Sprites for the object's health bar
        health_sprites = [pygame.image.load("24health0.png"),
                          pygame.image.load("24health25.png"),
                          pygame.image.load("24health50.png"),
                          pygame.image.load("24health75.png"),
                          pygame.image.load("24health100.png")]
        
        health_count = 0 #How much health the object has
        show_health = False #If the object should show its health
        dropped = False #If the object has been destroyed and dropped and object
        
    
        """ For Object Constructor
========| Takes icon: Obj's Sprite | obj_type: object type     |========================
        | health: How many hits it takes to destroy object     |                    #nou
        | origin: X/Y Coordinate of where to draw the sprite   |
        | hitbox: Tuple of where the obj's hitbox is.          |
        | area: Range of where the player can click on object  |
========| respawn: Boolean. Whether or not the object respawns |========================
        """ #Addition of name, to be used to determine what drop an object has
        def __init__(self, name, icon, obj_type,
                     health, origin, hitbox, area, respawn):
            self.name = name
            self.icon = icon
            self.obj_type = obj_type
            self.origin = origin
            self.hitbox = hitbox
            self.area = area
            self.rect = pygame.Rect(self.hitbox)
            self.health = health
            self.maxhealth = health
            self.respawn = respawn
            
        def draw(self, window):
            #Function for displaying the object
            #Place the sprite
            window.blit(self.icon, self.origin)
            
            #Draw for debugging
            pygame.draw.rect(window, BLUE, self.area, 1)
            pygame.draw.rect(window, RED, self.hitbox, 1)
            self.display_health(window)
            
            
        def display_health(self, window):
            #Function for displaying the object's health bar
            if self.show_health: #If true, display the correct health sprite based on health_count
                window.blit(self.health_sprites[self.health],
                            (self.origin[0], self.origin[1] - 15))
                self.health_count -= 1 #Decrement for the next time
                
            if self.health_count <= 0: #Object has been destroyed for the next 20 seconds
                #No need to show its health bar
                self.show_health = False
                
        def drop_item(self, gatherables):
            #Function for determining which drop an item should have
            if self.obj_type == "minable":
                try:
                    drop_name = Items.items[self.name]["drops"]
                        #Create a new drop, of type Item (the class below this one)
                    drop = GameClasses.Item(
                            drop_name, self.origin[0] + 5, self.origin[1] + 10, 50, 50,
                            True, self.respawn_at, 4)
                    
                except KeyError:
                    if self.name == "Rock":
                        drop = GameClasses.Item(
                            "Rock", self.origin[0] + 5, self.origin[1] + 10, 50, 50,
                            True, self.respawn_at, 4)
                        
                    if self.name == "Rock Large":
                        drop = GameClasses.Item(
                            "Rock", self.origin[0] + 20, self.origin[1] + 20, 50, 50,
                            True, self.respawn_at, 10)
                   
                gatherables.append(drop) #Add the drop to the list of gatherable items
                
            #Same deal for a different type
            if self.obj_type == "chopable":
                try:
                    drop_name = Items.items[self.name]["drops"]
                    drop = GameClasses.Item(
                    drop_name, self.origin[0] + 10, self.origin[1] + 10, 50, 50,
                    True, self.respawn_at, 3)
                    
                except KeyError:
                    if self.name == "Tree Large":
                        drop = GameClasses.Item(
                            "Log", self.origin[0] + 40, self.origin[1] + 130,
                            50, 50, True, self.respawn_at, 6)
                        
                    if self.name == "Tree Small":
                        drop = GameClasses.Item(
                            "Log", self.origin[0] + 20, self.origin[1] + 40,
                            50, 50, True, self.respawn_at, 3)
                        
                    if self.name == "Tree Apple":
                        drop = GameClasses.Item(
                            "Apple", self.origin[0] + 40, self.origin[1] + 150,
                            50, 50, True, self.respawn_at, 3)
                    
                   
                gatherables.append(drop)
                
    """ END OF CLASS OBJECT
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
        START OF CLASS ITEM """
    
    class Item():
        #Class for dropable/gatherable items
        alive_for = 0 #How long the item has been alive (in ticks)
        respawn_tick = 0 #How long the item has been picked up for
        picked_up = False #If the item has been picked up or not
        respawn_at = 10 * FPS #When the item respawns
        
        def __init__(self, name, x, y, w, h, despawns, at, amt):
            self.name = name #Item's name
            self.despawns = despawns #If the item despawns
            self.despawn_at = at #When the item despawns
            self.x = x #X-coordinate
            self.y = y #Y-coordinate
            self.hitbox = (x - 15, y - 15, w, h) #Hitbox (x, y, width, height); as passed
            self.amount = amt #How many of the item is there; when picked up, how many items
                              #does the user get?
            
        def display(self, window):
            #Function for displaying the item
            if self.despawns: #If the item despawns, 
                self.alive_for += 1 #increment the alive_for tick
                #What is this doing? If an item despawns, that means it dropped
                #from an object. So when the object REspawns, the item, if not
                #picked up, will DESPAWN.
            
            else: #The item does NOT depsawn, meaning it will RESPAWN.
                if self.picked_up: #If the item has been picked up
                    self.respawn_tick += 1 #Increment the time it has been picked up for
                
            if self.respawn_tick > self.respawn_at: #Respawn the item
                if self.picked_up: #This should always be true, but just in case...
                    self.picked_up = False #The item has respawned, so it's no longer picked up
                    self.respawn_tick = 0 #Reset the respawn tick
                        
            if not self.picked_up: #If the item hasn't been picked up, it should be displayed
                offx = Items.items[self.name]["offx"] #Hitbox/Sprite adjustments
                offy = Items.items[self.name]["offy"]
                window.blit(Items.items[self.name]["icon"],
                            (self.x + offx, self.y + offy))
            
                #More hitbox debugging
                #pygame.draw.rect(window, RED, self.hitbox, 1)
                
    """ END OF CLASS ITEM
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
        START OF CLASS CRAFTING """
                
                
    #Class for Crafting Interface
    class Crafting():
        #List of interface buttons, of type Crafting.Button
        buttons = []
        buttonList = []
        category = 0
        
        #Sub Class for Interface Buttons
        #Args: Name, Hitbox: [x, y, w, h], location to place at: (x,y)
        class Button():
            #Button Constructor
            def __init__(self, name, hitbox, blit_at = (0,0)):
                self.name = name
                self.hitbox = hitbox
                self.pos = blit_at
                
        class ErrorMessage():
            alive_for = 2 * FPS
            tick = 0
            message = "Not enough {}"
            text = "None"
            pos = (205, 315)
                
            def on_tick(self, window, font):
                if self.text != "None":
                    message = self.message.format(self.text)
                    self.tick += 1
                    label = font.render(message, True, BLACK)
                    window.blit(label, self.pos)
                        
                if self.tick > self.alive_for:
                    self.text = "None"
                    self.tick = 0
                    
        class ButtonCategory():
            def __init__(self, name, buttons):
                self.name = name
                self.buttons = buttons
                self.image = None
                
        
        #Constructor for Crafting Class
        def __init__(self):
            #Define the Crafting Interface Buttons
            
            self.p_cat_button = GameClasses.Crafting.Button(
                    "Placeable Category", (4, 101, 95, 38))
            self.r_cat_button = GameClasses.Crafting.Button(
                    "Resource Category", (100, 101, 95, 38))
            
            #Placeables
            self.sb_button = GameClasses.Crafting.Button(
                    "Stone Wall", (4, 141, 193, 38), (590, 145))
            self.wg_button = GameClasses.Crafting.Button(
                    "Wood Gate", (4, 181, 193, 38), (590, 150))
            self.bed_button = GameClasses.Crafting.Button(
                    "Bed", (4, 221, 193, 38), (591, 150)) #341
            self.c2d_button = GameClasses.Crafting.Button(
                    "Cabinet", (4, 261, 193, 38), (591, 150)) #381
            self.tbl_button = GameClasses.Crafting.Button(
                    "Table", (4, 301, 193, 38), (591, 150)) #421
            self.wdrb_button = GameClasses.Crafting.Button(
                    "Wardrobe", (4, 341, 193, 38), (591, 150)) #461
            self.wdtl_button = GameClasses.Crafting.Button(
                    "Floor Tile Wood", (4, 381, 193, 38), (591, 150)) #461
            
            p = []
            p.append(self.sb_button), p.append(self.wg_button),
            p.append(self.bed_button),p.append(self.c2d_button),
            p.append(self.tbl_button),p.append(self.wdrb_button)
            p.append(self.wdtl_button)
            
            
            #Resources
            self.wp_button = GameClasses.Crafting.Button(
                    "Wood Planks", (4, 141, 193, 38), (590, 150))
            self.cb_button = GameClasses.Crafting.Button(
                    "Crafting Bench", (4, 181, 193, 38), (588, 147))
            self.sh_button = GameClasses.Crafting.Button(
                    "Stone Hammer", (4, 221, 193, 38), (592, 153))
            self.tw_button = GameClasses.Crafting.Button(
                    "Twine", (4, 261, 193, 38), (595, 150))
            #self.sbl_button = GameClasses.Crafting.Button(
            #        "Left Wall", (0, 260, 198, 3), (595, 150))
            #self.sbr_button = GameClasses.Crafting.Button(
            #        "Right Wall", (0, 285, 198, 25), (595, 150))
            r = []
            r.append(self.wp_button), r.append(self.cb_button),
            r.append(self.sh_button), r.append(self.tw_button),
            
            
            self.close_button = GameClasses.Crafting.Button(
                    "Close", (650, 0, 100, 100))
            self.craft_button = GameClasses.Crafting.Button(
                    "Craft", (573, 283, 75, 65))
            
            p_cat = GameClasses.Crafting.ButtonCategory("Placeables", p)
            r_cat = GameClasses.Crafting.ButtonCategory("Resources", r)
            self.buttonList.append(p_cat)
            self.buttonList.append(r_cat)
            
            #Add the buttons to the buttons list
            #self.buttons.append(self.sb_button)
            #self.buttons.append(self.wg_button)
            #self.buttons.append(self.wp_button)
            #self.buttons.append(self.sh_button)
            #self.buttons.append(self.tw_button)
            #self.buttons.append(self.sbl_button)
            #self.buttons.append(self.sbr_button)
            #self.buttons.append(self.cb_button)
            #self.buttons.append(self.bed_button)
            #self.buttons.append(self.c2d_button)
            #self.buttons.append(self.tbl_button)
            #self.buttons.append(self.wdrb_button)
            
            self.error = GameClasses.Crafting.ErrorMessage()
        
        def draw(self, window):
            #Function made for testing/drawing button locations
            #Now disused because all the buttons have been placed.
            #Could probably get rid of it, but I'll leave it here just in case...
            """
            pygame.draw.rect(window, RED, (650, 0, 100, 100), 2)
            pygame.draw.rect(window, RED, (0, 102, 198, 30), 2)
            pygame.draw.rect(window, RED, (0, 130, 198, 25), 2)
            pygame.draw.rect(window, RED, (0, 155, 198, 25), 2)
            pygame.draw.rect(window, RED, (0, 180, 198, 30), 2)
            pygame.draw.rect(window, RED, (0, 210, 198, 25), 2)
            pygame.draw.rect(window, RED, (0, 235, 198, 25), 2)
            """
            #for button in self.buttons:
            #   pygame.draw.rect(window, RED, button.hitbox, 1)
               
            #pygame.draw.rect(window, RED, self.p_cat_button.hitbox, 1)  
            #pygame.draw.rect(window, RED, self.r_cat_button.hitbox, 1)
            
            #for b in self.buttonList[self.category].buttons:
            #    pygame.draw.rect(window, RED, b.hitbox, 1)
                    
            return
            
            """
            pygame.draw.rect(window, RED, self.sb_button, 1)
            pygame.draw.rect(window, RED, self.wg_button, 1)
            pygame.draw.rect(window, RED, self.wp_button, 1)
            pygame.draw.rect(window, RED, self.cb_button, 1)
            pygame.draw.rect(window, RED, self.sh_button, 1)
            pygame.draw.rect(window, RED, self.tw_button, 1)
            pygame.draw.rect(window, RED, self.craft_button, 1)
            pygame.draw.rect(window, RED, self.close_button, 1)
            """
            
        def check_buttons(self, press, window, labels):
            #This function gets which button was pressed, based
            #on where the mouse positon is when it was clicked.
            #This position will be referred to as "press".
            
            call = "" #Command, is either "Craft" or "Call". Returned & used in main.py.
                
            #These 4 if statements are special case buttons
            if bm.containspoint(press, self.close_button.hitbox):
                call = "Close"
            
            if bm.containspoint(press, self.craft_button.hitbox):
                call = "Craft"
                
            if bm.containspoint(press, self.p_cat_button.hitbox):
                self.category = 0
                labels[0] = ""
            
            if bm.containspoint(press, self.r_cat_button.hitbox):
                self.category = 1
                labels[0] = ""
            
            #Get the button that was pressed
            for b in self.buttonList[self.category].buttons:
                if bm.containspoint(press, b.hitbox):
                    labels[0] = b.name #Make the item name to labels[0]
          
            return call #Returns command or ""
        
        def display_info(self, player, labels, window, font, font2, font3):
            #Function for displaying various moving parts
            #of the crafting Interface, such as inventory, amount, etc.
            
            #Place the button image
            if self.category == 0:
                buttons_bar = pygame.image.load("p_cat_buttons.png")
            if self.category == 1:
                buttons_bar = pygame.image.load("r_cat_buttons.png")

            window.blit(buttons_bar, (0, 141))
            
            item = labels[0] #Get the selected item
            
            #Iterate through the buttons and find a match.
            for button in self.buttonList[self.category].buttons:
                if button.name == item:
                    b = button #Save the button that matches
                    
            try:
                icon = Items.items[item]["icon"] #Get the item's sprite/icon
                window.blit(icon, b.pos) #Place the icon on the window
                

                ings_labels = [] #List for ingredients, of type pygame label.
                amts_labels = [] #List for ingredient amounts, of pygame label.
                
                #Collect the ingredients as labels,
                for i in Items.items[item]["recipe"]:
                    ings_labels.append(font.render(i, True, BLACK))
                    
                    #If the item has an amount of -1, that means you just need
                    #at least 1 in your inventory, so no amount is associated
                    #with this ingredient label.
                    if Items.items[item]["recipe"][i] != -1:
                        k = Items.items[item]["recipe"][i] #Simplifying
                        amts_labels.append(font.render(str(k), True, BLACK))
                        
                y = 150 #Set Y-Coordinate
                for i in ings_labels:
                    #Place the labels in a column at X = 250
                    window.blit(i, (250, y))
                    y += 30 #Increase Y-Coordinate
                    
                #Same deal as the above loop, but for the ingredient amounts
                y = 150
                for j in amts_labels:
                    window.blit(j, (210, y))
                    y += 30
                    
            #In theory, this should never be excepted, because all the items
            #in the game are in Items.items (see _215_items.py)
            except KeyError:
                pass
            
            #The "You Have" number above the craft button
            has = False #Does the player have it? We don't know yet.
            #Iterate through the player's items
            for slot in player.inventory:
                if player.inventory[slot]["name"] == item: #It's a match, the player has the item
                    amount = player.inventory[slot]["num"] #Get how many of the item the player has
                    has = True
                
            if not has: #The player does not have this item, assign amount to 0.
                amount = 0
            
            #Place the label with the amount
            num_label = font.render(str(amount), True, BLACK)
            window.blit(num_label, (580, 245))
            
            #Fun stuff now!
            #This loop will place the sprites into the inventory area
            #under the main crafting interface
            x = 201 #initialze a starting X and Y
            y = 350
            for k in player.inventory:
                l = Items.items[player.inventory[k]["name"]] #Simplify. l is the item's name
                
                #Place the icon, at defined X/Y coordinates, and adjust them using the 
                #Inventory offset the item has, that will mostly center its sprite
                #into the inventory slot it's in. Purely for aesthetics.
                window.blit(l["icon"], (x + l["invoff"][0], y + l["invoff"][1]))
                
                #Debug again...
                #pygame.draw.rect(window, RED, (x, y, 48, 48), 1)
                
                #Place the amount of the item the player has in roughly
                #the center of the inventory slot.
                window.blit(font2.render(str(player.inventory[k]["num"]),
                                        True, BLACK), (x + 20, y + 30))
                x += 48 #Increment X
                
                if x > 583: #Hit the end of the row, move back and down
                    x = 200
                    y += 48
                    
            self.error.on_tick(window, font3)
                
            
        def craft(self, player, item):
            #Function for actually crafting an item.
            
            if item != "": #If labels[0] from main isn't empty...
                has_not = [] #List of how many ingredient requirements the player doesn't meet
                has = [] #List of what the player does have
                
                
                #Alright, more annoying, I mean fun, loops.
                #This one will update has and has_not
                #Start by iterating through the item's recipe
                for r in Items.items[item]["recipe"]:
                    try:
                        found = False
                        #Now look in the player's inventory, and see if the player has the ingredient
                        for slot in player.inventory:
                            if player.inventory[slot]["name"] == r:
                                if player.inventory[slot]["num"] >= Items.items[item]["recipe"][r]:
                                    found = True
                                    has.append(r) #Add it to the list of what the player has
                                     
                                else: #The player doesn't have the ingredient
                                    #altogether, or doesn't have enough to craft the item
                                    has_not.append(r)
                                
                        if not found:
                            has_not.append(r)
                    #In theory, this should be hit anymore.
                    #It was for the previous inventory format, but, you know, JUST IN CASE...
                    except KeyError:
                        has_not.append(r)
                        
                #The player can't craft the item, because they don't have enough resources
                #If True, the rest of the function is useless
                if len(has_not) > 0 or len(has) < len(Items.items[item]["recipe"]):
                    self.error.text = has_not[0]
                    
                    
                else:
                    #print("crafting") #HAHAH LOOK AN OLD DEBUG PRINT STATEMENT! COOL!
                    #Anyways, the player has enough materials to craft the item
                    amount = Items.items[item]["amt"] #Amount of ingredient needed
                    
                    #Look to see if the player already has some of the item in their inventory.
                    found = False
                    for slot in player.inventory:
                        if player.inventory[slot]["name"] == item: #They have it, so
                            player.inventory[slot]["num"] += amount #increment its amount.
                            found = True #Amount was added, so don't bother with the while loop
                
                    #While loop controller
                    i = 0
                    while not found: #If the item wasn't added in the above for loop,
                        i += 1 #increment i. Weird place, but it makes sense because inv starts at 1.
                        if i not in player.inventory: #If the slot isn't in the player's inventory,
                            #update theplayer's inventory with the slot number, item name, and amount.
                            player.inventory.update({i: {"name": item,
                                                       "num": amount}})
                            found = True #Added, so end loop.
                    
                    #Loop to remove used ingredients from player's inventory
                    for i in has:
                        try:
                            for slot in player.inventory:  #Look through the player's inventory  
                                if player.inventory[slot]["name"] == i: #Match item with ingredient
                                    #If the ingredient amount is -1, don't subtract. Else, do.
                                    if Items.items[item]["recipe"][i] != -1:
                                        player.inventory[slot]["num"] -= Items.items[item]["recipe"][i]
                                        if player.inventory[slot]["num"] == 0: #If item is 0,
                                            del player.inventory[slot] #delete item so it looks better
                                    
                        #Lol ignore this.
                        #(JK) If player runs out of an ingredient it will be deleted from the
                        #loop possibly before iteration ends. To prevent that, catch
                        #and continue loop with the next ingredient
                        except RuntimeError:
                            continue
                        
    """ END OF CLASS CRAFTING
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
===================================================================
    START OF CLASS INVENTORY """
                            
    class Inventory():
        #Class for Inventory, screen = 3
        slots = [] #Inventory slots, 0-23, of type GameClasses.Inventory.Slot
        hotbar = [] #Hotbar slots, 24-29 of type GameClasses.inventory.Slot
        
        class Slot():
            #Sub class that really doesn't use anything, but exists out of
            #sheer spite.
            def __init__(self, name, hitbox, contains):
                self.name = name #Name of the slot (1 higher than its index)
                self.hitbox = hitbox #Hitbox of the slot - the only useful thing
                self.contains = contains #Literally nothing
                
            def display(self, window):
                #Function that displays the inventory slot's hitbox. Used for debugging
                pygame.draw.rect(window, RED, (self.hitbox[0],
                                               self.hitbox[1], 48, 48), 1)

                
        #Constructor for GameClasses.Inventory
        def __init__(self):
            self.location = (183, 142) #X/Y coordinate of main window position
            x = 186 #Initial coordinates for slot hitboxes
            y = 145
            #A loop that creates the slots
            for i in range(24):
                self.slots.append(
                        GameClasses.Inventory.Slot(str(i + 1),
                                                   (x, y, 48, 48), "null"))
                x += 48 #Increment the X
                
                if x > 569: #Reset: Move down 1 row, go back to column 1
                    x = 186
                    y += 48
                    
            x = 234 #New coordinates, but for the hotbar slots
            y = 307
            #Same deal as the inventory, but with only 6 slots
            for j in range(24, 30, 1):
                self.hotbar.append(
                        GameClasses.Inventory.Slot(str(j + 1),
                                                   (x, y, 48, 48), "null"))
                x += 48
            
        def display(self, sprites, player, font, window):
            #Function that displays the inventory and hotbar and contents
            window.blit(sprites.inventory_main, self.location) #Place down the frame first
            
            for slot in self.slots: #Display the slot's hitboxes, for debugging
                slot.display(window)
                
            for slot in self.hotbar: #Same as above loop
                slot.display(window)

            for k in player.inventory: #Loop through then player's items, and place them
                l = Items.items[player.inventory[k]["name"]] #Simplify
                display_x = self.slots[k - 1].hitbox[0]
                display_y = self.slots[k - 1].hitbox[1]
                window.blit(l["icon"], ( #Place, including inventory offsets from Items class
                        display_x + l["invoff"][0],
                        display_y + l["invoff"][1]))
                
                #If the player has more than one of the item, place down the amount they have
                if player.inventory[k]["num"] > 1:
                    window.blit(font.render(str(player.inventory[k]["num"]),
                                True, BLACK), (display_x + 20, display_y + 30))
                    
            #Same as the above, but for the hotbar
            for m in player.hotbar:
                if player.hotbar[m]["name"] != "null": #Hotbar always has 6 slots, but "empty"
                                                       #slots are named "null".
                    n = Items.items[player.hotbar[m]["name"]]
                    display_x = self.hotbar[m - 25].hitbox[0]
                    display_y = self.hotbar[m - 25].hitbox[1]
                    window.blit(n["icon"], (
                            display_x + n["invoff"][0],
                            display_y + n["invoff"][1]))
                    
                    if player.hotbar[m]["num"] > 1:
                        window.blit(font.render(str(player.hotbar[m]["num"]),
                                    True, BLACK), (display_x + 20, display_y + 30))

                    
        def check_slot(self, point):
            #Function that determines if a slot in the player's inventory
            #Was selected. Used for testing, now unused - not anymore, it has a use now
            
            #Initalize
            i = 0
            found = False
            #Loop until the slot is found or the range is exhausted
            while not found and i < len(self.slots):
                if bm.containspoint(point, self.slots[i].hitbox):
                    found = True
                    
                i += 1
                
            #If the slot was not found in the inventory's slots, it may be
            #in the inventory's hotbar
            if not found:
                i = 0 #Reset control
                found = False
                while not found and i < len(self.hotbar):
                    #Loop through hotbar instead
                    if bm.containspoint(point, self.hotbar[i].hitbox):
                        found = True
                        
                    i += 1
                    
                i += 24 #If the slot is found in the hotbar, add 24 so the right
                        #index is returned
                
            #i gets +1 after every loop iteration, so it will get an extra +1,
            #even if the index is found. Just knock if off and return the slot index.
            return found, (i - 1)
        
               
        def swap_slots_fixed(self, player, slots): 
            #FIXED function for swapping 2 slots that works better, is more simple,
            #and is just built different. Also works with hotbar into inventory, which
            #the old one did not
            first_item = None
            second_item = None
            slot1 = slots[0] + 1
            slot2 = slots[1] + 1
        
            #So the idea is, if 2 slots exist, they'll
            #be found by check_slot. Slots has the names, so use those
            
            #If the first slot is less than 24, it must in the inventory.
            #But the player may not have anything in that slot. If they do,
            #then collect the data associated with the item.
            if slots[0] < 24:
                if (slots[0] + 1) in player.inventory:
                    name1 = player.inventory[slot1]["name"]
                    num1 = player.inventory[slot1]["num"]
                    first_item = {"name": name1, "num": num1}
                
            #If the slot is 24 or greater, it must be in the player's hotbar
            #Since the hotbar always has 6 keys, check the slot to see if the
            #name of the item in the slot is "null". If it is not, collect data
            else:
                if player.hotbar[slots[0] + 1 ]["name"] != "null":
                    name1 = player.hotbar[slot1]["name"]
                    num1 = player.hotbar[slot1]["num"]
                    first_item = {"name": name1, "num": num1}
                    
            #Now repeat, but with the second slot
            if slots[1] < 24:
                if (slots[1] + 1) in player.inventory:
                    name2 = player.inventory[slot2]["name"]
                    num2 = player.inventory[slot2]["num"]
                    second_item = {"name": name2, "num": num2}
                    
            else:
                if player.hotbar[slots[1] + 1 ]["name"] != "null":
                    name2 = player.hotbar[slot2]["name"]
                    num2 = player.hotbar[slot2]["num"]
                    second_item = {"name": name2, "num": num2}
                    
            #Ultimate Debugging Kit :tm:
            #print(first_item)
            #print(second_item)
                    
            #Now just trade the values. If the first item is None, do nothing
            #If not, follow these steps:
            #Determine whether there exists an item in the second slot
            #Determine if the slot is in the inventory (<24) or hotbar (24>)
            #Based on the previous 2 decisions, trade appropriately.
            if first_item != None:
                #print("At 1")
                if second_item != None:
                    #print("At 1.5")
                    if slots[0] < 24:
                        #print("At 2")
                        player.inventory[slot1] = second_item
                    else:
                        #print("At 3")
                        player.hotbar[slot1] = second_item
                    
                    if slots[1] < 24:
                        #print("At 4")
                        player.inventory[slot2] = first_item
                    else:
                        #print("At 5")
                        player.hotbar[slot2] = first_item
                        
                else:
                    #print("At 6")
                    if slots[0] < 24:
                        #print("At 7")
                        del player.inventory[slot1]
                        
                    else:
                        #print("At 8")
                        player.hotbar[slot1]["name"] = "null"
                        
                    if slots[1] < 24:
                        #print("At 9")
                        player.inventory.update({slot2: first_item})   
                    else:
                        #print("At 10")
                        player.hotbar[slot2] = first_item
                        
            #Moar debugging
            #print(player.inventory)
            #print(player.hotbar)
            
            
        def quick_move(self, player, point):
            i = 0
            found = False  
            slot = 0
            while not found and i < (len(self.hotbar)):
                if bm.containspoint(point, self.hotbar[i].hitbox):
                    found = True
                    slot = (i + 25)
                i += 1
                
            if slot > 24 and player.hotbar[slot]["name"] != "null":
                found = False
                i = 0
                while not found and i < len(self.slots):
                    if (i + 1) in player.inventory:
                        if (player.inventory[i + 1]["name"] == 
                            player.hotbar[slot]["name"]):
                            player.inventory[i + 1]["num"] += player.hotbar[slot]["num"]
                            player.hotbar[slot]["name"] = "null"
                            found = True
                    i += 1
                
            if slot > 24 and player.hotbar[slot]["name"] != "null":
                i = 0
                while not found and i < len(self.slots):
                    if (i + 1) not in player.inventory:
                        name = player.hotbar[slot]["name"]
                        num = player.hotbar[slot]["num"]
                        player.inventory.update({(i + 1): {"name": name, "num": num}})
                        
                        player.hotbar[slot]["name"] = "null"
                        found = True
                            
                    i += 1
                    
            if slot < 24:
                found = False
                i = 0
                while not found and i < (len(self.slots)):
                    if bm.containspoint(point, self.slots[i].hitbox):
                        found = True
                        slot = (i + 1)
                        
                    i += 1
                    
                if slot in player.inventory:
                    found = False
                    i = 0
                    while not found and i < len(self.hotbar):
                        if (player.hotbar[i + 25]["name"] ==
                            player.inventory[slot]["name"]):
                            player.hotbar[i + 25]["num"] += player.inventory[slot]["num"]
                            del player.inventory[slot]
                            found = True
                            
                        i += 1
                    
                    i = 0
                    while not found and i < len(self.hotbar):
                        if (i + 25) in player.hotbar:
                            if player.hotbar[i + 25]["name"] == "null":
                                name = player.inventory[slot]["name"]
                                num = player.inventory[slot]["num"]
                                player.hotbar[i + 25] = {"name": name, "num": num}
                            
                                del player.inventory[slot]
                                found = True
                                
                        i += 1
                        
    class Wall():
        
        def place_wall(pos, objects):
            walls = []
            indexes = []
            i = 0
            for obj in objects:
                if ("Stone Wall" in obj.name
                    or "Wood Gate" in obj.name):
                    walls.append(obj)
                    indexes.append(i)
                i += 1
                    
            values = Items.items["Stone Wall"]["hitbox"]
            new_hitbox = (pos[0] + values[0],
                          pos[1] + values[1], values[2], values[3])
            
            can_place = True
            for obj in objects:
                if bm.collisions(new_hitbox, obj.hitbox):
                    can_place = False
                    
            if can_place:
                GameClasses.Wall.create_wall("Stone Wall", pos, objects)
                indexes.append(len(objects) - 1)
                
                GameClasses.Wall.adjust_walls(objects, indexes)
                
        def create_wall(name, pos, objects, index = -1):
            values = Items.items[name]["hitbox"]
            new_hitbox = (pos[0] + values[0],
              pos[1] + values[1], values[2], values[3])
            
            new_wall = GameClasses.Object(name,
                Items.items[name]["icon"],
                Items.items[name]["type"], 4,
                (pos[0], pos[1]), new_hitbox, (pos[0], pos[1], 40, 40), False)
            
            if index < 0:  
                objects.append(new_wall)
                
            else:
                objects[index] = new_wall
            
        def adjust_walls(objects, indexes):
            
            for i in indexes:
                sides = [False, False, False, False]
                side = ""
                name = ""
                
                w = objects[i]
                pos = w.origin
                for obj in objects:
                    if ("Stone Wall" in obj.name
                    or "Wood Gate" in obj.name):
                        if pos[0] == obj.origin[0]:
                            if pos[1] == obj.origin[1] - 40:
                                sides[3] = True
                                
                            if pos[1] == obj.origin[1] + 40:
                                sides[2] = True
                                #print(obj.name)
                                if "Right" in obj.name:
                                    side = "Right"
                                elif "Left" in obj.name:
                                    side = "Left"
                                else:
                                    side = "Right"
                                                        
                        if pos[1] == obj.origin[1]:
                            if pos[0] == obj.origin[0] - 40:
                                sides[1] = True
                                
                            if pos[0] == obj.origin[0] + 40:
                                sides[0] = True
                        
                        if "Wood Gate" not in w.name:
                            if sides[1] and sides[3]: #Top Left Corner
                                name = "Stone Wall Left Top"    
                        
                            if sides[0] and sides[1]: #Middle
                                name = "Stone Wall"         
                                
                            if sides[0] and sides[3]: #Top Right Corner
                                name = "Stone Wall Right Top"   
                                
                            if sides[2] and sides[3]: #Side
                                name = "Stone Wall {}".format(side) 
                                
                            if sides[1] and sides[2]: #Bottom Left Corner
                                name = "Stone Wall Left Bottom"             
                            
                            if sides[0] and sides[2]: #Bottom Right Corner
                                name = "Stone Wall Right Bottom" 
                            
                        #print("Index {} is a {} and has name {}".format(i, w.name, name))
                        #print("It is blocked at {}".format(sides))
                            
                        if len(name) > 0:
                            GameClasses.Wall.create_wall(name, pos, objects, i)
                            
                        else:
                            if "Wood Gate" not in w.name:
                                GameClasses.Wall.create_wall("Stone Wall",
                                                             pos, objects, i)
                                
    class AimlessSlime():
        x = 350
        y = 250
        hitbox = [0, 0, 32, 22]
        
        def __init__(self, x, y):
            self.x_direction = x
            self.y_direction = y
            self.starting_movement = (x, y)
        
        def move(self, border):
            
            self.x += (3 * self.x_direction)
            self.y += (3 * self.y_direction)
            
            if self.x + self.hitbox[2] + 3 > border.right or self.x - 3 < 0:
                self.x_direction *= -1
                
            if self.y + self.hitbox[3] + 3 > border.bottom or self.y - 3 < 0:
                self.y_direction *= -1
                
        def reset(self):
            self.x = 350
            self.y = 250
            self.x_direction = self.starting_movement[0]
            self.y_direction = self.starting_movement[1]
