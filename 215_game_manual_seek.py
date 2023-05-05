# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:07:09 2023

@author: alexe
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:14:55 2023

@author: alexeawdsa
"""

import pygame
from boxmeta import BoxMeta as bm
from _215_game_classes import GameClasses as gc

x=100
y=100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

window = pygame.display.set_mode((750, 500))
#window = pygame.display.set_mode((0,0), pygame.RESIZABLE)

def create_pygame(): #initializes Pygame screen
    pygame.init()
    pygame.display.set_caption("Project")
        
class Window():
    def __init__(self):
        self.left = 0
        self.right = 750
        self.top = 0
        self.bottom = 500
        self.position = (0,0)
    
def create_objects(sprites):
    objects = []
    #Name = gc.Object(Item Icon, Item Type, Item Health, Item Origin, (Item Width, Item Height))
    rock = gc.Object(sprites.rock_1, "minable", 4, (270, 300), (32, 32))
    rock2 = gc.Object(sprites.rock_1, "minable", 4, (150, 300), (32, 32))
    rock3 = gc.Object(sprites.rock_1, "minable", 4, (90, 150), (32, 32))
    rock4 = gc.Object(sprites.rock_1, "minable", 4, (400, 256), (32, 32))
    tree1 = gc.Object(sprites.tree3, "chopable", 4, (350, 105), (62, 97))
    tree2 = gc.Object(sprites.tree3, "chopable", 4, (75, 256), (62, 97))
    
    objects.append(rock)
    objects.append(rock2)
    objects.append(rock3)
    objects.append(rock4)
    objects.append(tree1)
    objects.append(tree2)
    return objects

def draw_objects(objects, window):
    for o in objects:
        #obj_range = ((o.hitbox[0] - 10), (o.hitbox[1] - 10),
              #(o.hitbox[2] + 20), o.hitbox[3] + 20)
    
        if not o.destroyed:
            #pygame.draw.rect(window, BLUE, obj_range, 1)
            o.draw(window)
            
def collect_alive(all_objects):
    objects = []
    for obj in all_objects:
        if not obj.destroyed:
            objects.append(obj)
            
    return objects


def object_loop(player, all_objects, window):
    hits = []
    for obj in all_objects:
        if not obj.destroyed:
            
            #Draw Object's Sprite
            obj.draw(window)
            
            
            #Destroy an object
            if bm.collisions(player.get_hit_range(window), obj.hitbox):
                if player.click_flag == 1:
                    hits.append(True)
                    
                    if player._cooldown == 0:
                        if obj.health > 0:
                            if obj.obj_type == "minable":
                                if player.item == "pickaxe":
                                    gc.SoundEffects.pickaxe_on_rock.play()
                                    obj.health -= 1
                                    obj.show_health = True
                                    obj.health_count = 60
                                    print("objectRock health:", obj.health)
                            
                            if obj.obj_type == "chopable":
                                if player.item == "axe":
                                    gc.SoundEffects.axe_on_wood.play()
                                    obj.health -= 1
                                    obj.show_health = True
                                    obj.health_count = 60
                                    print("objectTree health:", obj.health)
                                    
                        if obj.health == 0:
                            obj.destroyed = True
                    
                    player.activate_cooldown()
        
        #Respawn an Object if it can be respawned
        else:
            obj.seconds_count += 1
            if obj.seconds_count >= obj.respawn_at:
                if not bm.collisions(player.hitbox, obj.hitbox):
                    obj.destroyed = False
                    obj.health = obj.maxhealth
                    obj.seconds_count = 0
            
    if player.click_flag == 1:
        if True not in hits:
            if not player.item == "sword":
                print(hits)
                gc.SoundEffects.air_swipe.play()
        
                            
                                    
                            
        
        
def destroy_object(player, range_box, obj, hits):
    #obj_range = ((obj.hitbox[0] - 10), (obj.hitbox[1] - 10),
             # (obj.hitbox[2] + 20), obj.hitbox[3] + 20)
    
    #pygame.draw.rect(window, BLUE, obj_range, 1)
    
    if bm.collisions(range_box, obj.hitbox):
        hits.append(True)
        print("Object is in Range")
        if player._cooldown == 0:
            if obj.health > 0:
                if obj.obj_type == "minable":
                    if player.item == "pickaxe":
                        gc.SoundEffects.pickaxe_on_rock.play()
                        obj.health -= 1
                        obj.show_health = True
                        obj.health_count = 60
                        print("objectRock health:", obj.health)
                        
                if obj.obj_type == "chopable":
                    if player.item == "axe":
                        gc.SoundEffects.axe_on_wood.play()
                        obj.health -= 1
                        obj.show_health = True
                        obj.health_count = 60
                        print("objectTree health:", obj.health)
                
            if obj.health == 0:
                obj.destroyed = True
                
        player.activate_cooldown()
            
    else: hits.append(False)

        #print("Object is out of Range")
        
def attack(player, slime_dude, window):
    if player.click_flag == 1:
        box = player.get_hit_range(window)
        
        if player.item == "sword":
            if bm.collisions(box, slime_dude.hitbox):
                #gc.SoundEffects.sword_hit_slime.play()
                slime_dude.health -= 5
                player.activate_cooldown()
                print("Slime Dude's HP:", slime_dude.health)
                
            else:
                print("Can't attack, enemy out of range.")
                gc.SoundEffects.air_swipe.play()
            
def display_sidebar(player, sprites):
    actions_tab = sprites.actions_tab
    window.blit(actions_tab, (501, 0))
    window.blit(sprites.inventory_tab, (501, 380))
    if player.current_slot == 1: 
        window.blit(sprites.chosen_slot, (513, 387))
    elif player.current_slot == 2:
        window.blit(sprites.chosen_slot, (560, 387))
    elif player.current_slot == 3:
        window.blit(sprites.chosen_slot, (607, 387))
    elif player.current_slot == 4:
        window.blit(sprites.chosen_slot, (654, 387))
    elif player.current_slot == 5:
        window.blit(sprites.chosen_slot, (701, 387))
    elif player.current_slot == 6:
        window.blit(sprites.chosen_slot, (513, 432))
    elif player.current_slot == 7:
        window.blit(sprites.chosen_slot, (560, 432))
    elif player.current_slot == 8:
        window.blit(sprites.chosen_slot, (607, 432))
    elif player.current_slot == 9:
        window.blit(sprites.chosen_slot, (654, 432))
    elif player.current_slot == 10:
        window.blit(sprites.chosen_slot, (701, 432))
        
    window.blit(sprites.sword, (510, 378))
    window.blit(sprites.axe, (604, 385))
    #window.blit(sprites.gold_ore, (250, 250))
    #window.blit(sprites.rock_1, (100, 150))
    #window.blit(sprites.tree3, (200, 350))
    #window.blit(sprites.mine_label, (575, 50))
    #window.blit(sprites.flower1, (40, 70))
    #window.blit(sprites.bush1, (400, 50))
    
def spawn_hit_range(player, objects, slime_dude):
    print("cooldown:", player._cooldown)
    if player.facing == "north":
        box = (player.x - 20, (player.hitbox[1] - 20), 90, 20)
        
    elif player.facing == "east":
        box = (player.x + player.hitbox[2], player.y - 20, 20, 90)
        
    elif player.facing == "west":
        box = ((player.hitbox[0] - 20), player.y - 20, 20, 90)
        
    elif player.facing == "south":
        box = ((player.x - 20, player.hitbox[1] + player.hitbox[3], 90, 20))
         
    #pygame.draw.rect(window, GREEN, box, 1)
    
    if player.item == "pickaxe" or player.item == "axe":
        hits = []
        for obj in objects:
            destroy_object(player, box, obj, hits)
            
        if True not in hits:
            gc.SoundEffects.air_swipe.play()
            
        
    elif player.item == "sword":
        attack(player, box, slime_dude)
        
    else:
        gc.SoundEffects.air_swipe.play()

def get_direction(player):
    coordinate = pygame.mouse.get_pos()
    if ((coordinate[0] > player.x)
    and (coordinate[0] <= player.x + player.hitbox[2])
    and coordinate[1] <= player.y):
        player.facing = "north"
        
    elif ((coordinate[0] > player.x)
    and (coordinate[0] <= player.x + player.hitbox[2])
    and coordinate[1] >= player.y):
        player.facing = "south"
        
    elif coordinate[0] < player.x:
        player.facing = "west"
        
    elif coordinate[0] > player.x:
        player.facing = "east"
        
    if player.facing == "north":
        box = (player.x - 20, (player.hitbox[1] - 20), 90, 20)
        
    elif player.facing == "east":
        box = (player.x + player.hitbox[2], player.y - 20, 20, 90)
        
    elif player.facing == "west":
        box = ((player.hitbox[0] - 20), player.y - 20, 20, 90)
        
    elif player.facing == "south":
        box = ((player.x - 20, player.hitbox[1] + player.hitbox[3], 90, 20))
        
    pygame.draw.rect(window, GREEN, box, 1)
        
    
    
def Game():
    create_pygame()
    sprites = gc.Sprites()
    objects = create_objects(sprites)
    #objects = collect_alive(all_objects)
    run = True
    screen = 1
    player = gc.Player(350, 350)
    player.change_item()
    border = Window()
    click_flag = 0
    select_flag = 0
    pos = (350, 350)
    select_pos = (350, 350)
    new_pos = (350, 350)
    new_select_pos = (350, 350)
    clock = pygame.time.Clock()
    tick = 0
    seconds = 0
    slime_dude = gc.Slime(sprites.slime, sprites.slime_angry, 20, 155, 155)
    
    while run:
        #pygame.time.delay(17)
        tick += 1
        seconds += 1
        if tick == 18:
            """for obj in all_objects:
                if obj.destroyed:
                    obj.seconds_count += 1
                    if obj.seconds_count >= obj.respawn_at:
                        if not bm.collisions(player.hitbox, obj.hitbox):
                            obj.destroyed = False
                            obj.health = obj.maxhealth
                            obj.seconds_count = 0"""
                        
            #objects = collect_alive(all_objects)
            tick = 0
            
        clock.tick(27)#Framerate
        
        """ == Code for pressing the corner "X" button == """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        """ ============================================= """
        
        if screen == 1:
            
            keys = pygame.key.get_pressed()
            
            mouse_press = pygame.mouse.get_pressed()
            
            """if mouse_press[2]:
                click_flag += 1
                
                if click_flag == 1:
                    new_pos = pygame.mouse.get_pos()
                    
                    if new_pos[0] < 500:
                        pos = tuple(adjust_position(player, objects, new_pos))
                        
            else:
                click_flag = 0"""
                        
            if mouse_press[0]:
                player.click_flag += 1
                attack(player, slime_dude, window)
                
                #if select_flag == 1:
                   # new_select_pos = pygame.mouse.get_pos()
                    
                   # if new_select_pos[0] < 500:
                       # select_pos = new_select_pos
                
                            #if i.rect.collidepoint(select_pos):
                       # spawn_hit_range(player, objects, slime_dude)
                                #destroy_object(player, i)
                            
            else:
                player.click_flag = 0
            
            if keys[pygame.K_d]:
                player.facing = "east"
                if (player.x + 50) + player.vel < border.right + 1:
                    player.x = player.x + player.vel
                    for w in objects:
                        if bm.collideleft(player.hitbox, w.hitbox, player.vel):
                            player.x = player.x - player.vel
                else: pass
            
            if keys[pygame.K_a]:
                player.facing = "west"
                if player.x - player.vel > -1:
                    player.x = player.x - player.vel
                    for x in objects:
                        if bm.collideright(player.hitbox, x.hitbox, player.vel):
                            player.x = player.x + player.vel
                else: pass
            
            if keys[pygame.K_w]:
                player.facing = "north"
                if player.y - player.vel > -1:
                    player.y = player.y - player.vel
                    for y in objects:
                        if bm.collidebottom(player.hitbox, y.hitbox, player.vel):
                            player.y = player.y + player.vel
                else: pass
            
            if keys[pygame.K_s]:
                player.facing = "south"
                if player.y + player.vel < 501:
                    player.y = player.y + player.vel
                    for z in objects:
                        if bm.collidetop(player.hitbox, z.hitbox, player.vel):
                            player.y = player.y - player.vel
                else: pass
            
            if keys[pygame.K_1]:
                player.current_slot = 1
                player.change_item()
            if keys[pygame.K_2]:
                player.current_slot = 2
                player.change_item()
            if keys[pygame.K_3]:
                player.current_slot = 3
                player.change_item()
            if keys[pygame.K_4]:
                player.current_slot = 4
                player.change_item()
            if keys[pygame.K_5]:
                player.current_slot = 5
                player.change_item()
            if keys[pygame.K_6]:
                player.current_slot = 6
                player.change_item()
            if keys[pygame.K_7]:
                player.current_slot = 7
                player.change_item()
            if keys[pygame.K_8]:
                player.current_slot = 8
                player.change_item()
            if keys[pygame.K_9]:
                player.current_slot = 9
                player.change_item()
            if keys[pygame.K_0]:
                player.current_slot = 10
                player.change_item()

            
        window.fill(BLACK)
        #window.blit(sprites.bg1, (0,0))
        #pygame.draw.circle(window, RED, pos, 5)
        player.display(window)
        player.cooldown()
        #get_direction(player)
        slime_dude.display(window)
        slime_dude.check_for_player(player, objects)
        object_loop(player, objects, window)
        display_sidebar(player, sprites)
        #draw_objects(objects, window)
        pygame.draw.rect(window, RED, player.hitbox, 1)
        pygame.draw.line(window, RED, (501, 0), (501, 500), 1)
        pygame.display.update()
              
        
    pygame.quit()
        

if __name__ == '__main__': #Run Program
    Game()