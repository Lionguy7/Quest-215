# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:14:55 2023

@author: me
"""

import pygame
from boxmeta import BoxMeta as bm
"""
x=100
y=100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)"""

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window = pygame.display.set_mode((750, 500))

class Player():
    compass = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 0)]
    point = 0
    def __init__(self, x, y):
        self.x = x #Player's X Coordinate
        self.y = y #Player's Y Coordinate
        self.vel = 1 #Amount of pixels per frame the Player moves
        self.half_vel = -1 #Half of the amount of pixels per frame the Player moves, minus 1
        self.icon = pygame.image.load("chartemp.png") #Player's Sprite
        self.hitbox = (x, y, 50, 50) #Player's Hitbox (should match Sprite)
        self.currentAnimation = "Standing" #Player's current animation
        self.rect = pygame.Rect(self.hitbox)
        self.xd = 0
        self.yd = 0
        #self.blocked = [Left, Right, Up, Down]
        self.blocked = [False, False, False, False]
        self.direction = [False, False, False, False]
        #self.move: X, Y (-1, 0, 1 as possible values)
        self.moving = [0, 0]
    
    def display(self, window):
        icon = self.icon #Player's Sprite
        x = self.x #Player's X Coordinate
        y = self.y #Player's Y Coordinate
        window.blit(icon, (x, y)) #Draw the sprite to the Pygame window
        self.hitbox = (x, y, 50, 50) #Readjust Player's hitbox.
        
class Window():
    def __init__(self):
        self.left = 0
        self.right = 750
        self.top = 0
        self.bottom = 500
        self.position = (0,0)
        
class Sprites():
    actions_tab = pygame.image.load("actions_tab_1.png")
    gold_ore = pygame.image.load("gold_ore_1.png")
    mine_label = pygame.image.load("mine_label.png")
    rock_1 = pygame.image.load("rock1.png")
    tree3 = pygame.image.load("tree3.png")
    bg1 = pygame.image.load("bg1.png")
    bush1 = pygame.image.load("bush1.png")
    flower1 = pygame.image.load("flower1.png")
    
class Object():
    seconds_count = 0
    respawn_at = 25
    destroyed = False
    obj_type = ""
    hitbox = (0,0,0,0)
    
    def __init__(self, icon, ot, origin, size):
        self.icon = icon
        self.obj_type = ot
        self.origin = origin
        self.hitbox = (origin[0], origin[1], size[0], size[1])
        self.rect = pygame.Rect(self.hitbox)
        
    def draw(self, window):
        window.blit(self.icon, self.origin)
        pygame.draw.rect(window, RED, self.hitbox, 1)

def create_pygame(): #initializes Pygame screen
    pygame.init()
    pygame.display.set_caption("Project")
    
def create_objects(sprites):
    objects = []
    
    rock = Object(sprites.rock_1, "minable", (270, 300), (32, 32))
    rock2 = Object(sprites.rock_1, "minable", (150, 300), (32, 32))
    rock3 = Object(sprites.rock_1, "minable", (90, 150), (32, 32))
    rock4 = Object(sprites.rock_1, "minable", (400, 256), (32, 32))
    tree1 = Object(sprites.tree3, "chopable", (350, 105), (62, 97))
    tree2 = Object(sprites.tree3, "chopable", (75, 256), (62, 97))
    
    objects.append(rock)
    objects.append(rock2)
    objects.append(rock3)
    objects.append(rock4)
    objects.append(tree1)
    objects.append(tree2)
    return objects

def draw_objects(objects, window):
    for o in objects:
        o.draw(window)
        
def destroy_object(obj):
    return

def collision(player, objects, pos):
    collision = False
    for obj in objects:
        if not collision:
            #if obj.rect.colliderect(player.rect):
            if player.x > pos[0]:
                x_dir = -1
            else:
                x_dir = 1
                
            if player.y > pos[1]:
                y_dir = -1
            else:
                y_dir = 1
                
            move_horizontal = False
            move_vertical = False
            new_target = (0, 0)
            
            
            """ ========== 
            Check for Collision of Player on RIGHT of sprite.
            ========== """
            '''if player.x == (obj.hitbox[0] + obj.hitbox[2]):
               # print("true")
                if ((player.y >= obj.hitbox[1] and player.y <= obj.hitbox[1] + obj.hitbox[3])
                    or (player.y + player.hitbox[3] >= obj.hitbox[1] and player.y + player.hitbox[3] <= obj.hitbox[1] + obj.hitbox[3])
                    or (player.y <= obj.hitbox[1] and player.y + player.hitbox[3] >= obj.hitbox[1] + obj.hitbox[3])):
                   # print("also true")
                   
                    if y_dir < 0:
                        new_target_y = obj.hitbox[1] - player.hitbox[3] - 1
                    else:
                        new_target_y = (obj.hitbox[1] + obj.hitbox[3]) + 1
                        
                    new_target = (obj.hitbox[0] + obj.hitbox[2], new_target_y)
                    #print("1,", new_target)
                        
            """elif (player.x + player.hitbox[2]) == obj.hitbox[0]:
                if y_dir < 0:
                    new_target_y = obj.hitbox[1] + player.hitbox[3] + 1
                else:
                    new_target_y = (obj.hitbox[1] + obj.hitbox[3]) + 1
                    
                new_target = (player.x, new_target_y)
                print("1,", new_target)"""'''
                
            if bm.collideright(player.hitbox, obj.hitbox, player.vel):
                #to_top = abs(player.hitbox[1] - obj.hitbox[1])
                #to_bottom = abs((obj.hitbox[1] + obj.hitbox[3]) - player.y)
               # print(to_top)
                #print(to_bottom)
                collision = True
                
                if pos[1] < obj.hitbox[1]:
                   # print("R: Going towards top")
                    new_target_y = obj.hitbox[1] - player.hitbox[3] - 1
                else:
                   # print("R: Going towards bottom")
                    new_target_y = (obj.hitbox[1] + obj.hitbox[3]) + 1
                        
                new_target = ((obj.hitbox[0] + obj.hitbox[2] + 1), new_target_y)
                
            #=================================================================
                
            elif bm.collideleft(player.hitbox, obj.hitbox, player.vel):
                collision = True
                if pos[1] < obj.hitbox[1] :
                    #print("L: Going towards top")
                    new_target_y = obj.hitbox[1] - player.hitbox[3] - 1
                else:
                    #print("L: Going towards bottom")
                    new_target_y = (obj.hitbox[1] + obj.hitbox[3]) + 1
                        
                new_target = ((obj.hitbox[0] - player.hitbox[2] - 1), new_target_y)
                #print("1,", new_target)
                    
             #=================================================================
                
            elif bm.collidetop(player.hitbox, obj.hitbox, player.vel):
                collision = True
                #to_left = abs(player.hitbox[0] - obj.hitbox[0])
                #to_right = abs((obj.hitbox[0] + obj.hitbox[2]) - player.hitbox[0])
                if pos[0] < obj.hitbox[0]:
                    new_target_x = obj.hitbox[0] - player.hitbox[2] - 1
                else:
                    new_target_x = obj.hitbox[0] + obj.hitbox[2] + 1
                        
                new_target = (new_target_x, (obj.hitbox[1] - player.hitbox[3] - 1))
                    #print("1,", new_target)
                    
            elif bm.collidebottom(player.hitbox, obj.hitbox, player.vel):
                collision = True
                #to_left = abs(player.hitbox[0] - obj.hitbox[0])
                #to_right = abs((obj.hitbox[0] + obj.hitbox[2]) - player.hitbox[0])
                
                if pos[0] < obj.hitbox[0]:
                    new_target_x = obj.hitbox[0] - player.hitbox[2] - 1
                else:
                    new_target_x = obj.hitbox[0] + obj.hitbox[2] + 1
                        
                new_target = (new_target_x, (obj.hitbox[1] + obj.hitbox[3]) + 1)
                    #print("1,", new_target)
                
                
            global window
            pygame.draw.circle(window, WHITE, new_target, 5)
                
            """
            elif player.y == obj.hitbox
            hitbox = obj.hitbox
            
            """ #LOGIC FOR PLAYER ENCOUNTERING TOP OF SPRITE """
            #if ((playerHitbox[1] + playerHitbox[3]) >= hitbox[1]) and (playerHitbox[1] < hitbox[1] + hitbox[3]):
             #   if (playerHitbox[0] + playerHitbox[2] > hitbox[0]) and (playerHitbox[0]  < hitbox[0] + hitbox[2]):
              #      pass
              
            """ LOGIC FOR PLAYER ENCOUNTERING LEFT OF SPRITE """
            """ if (player.hitbox[1] <= hitbox[1] + hitbox[3]) and (player.hitbox[1] + player.hitbox[3] >= hitbox[1]):
                if ((player.hitbox[0] + player.hitbox[2] + 1) >= hitbox[0]) and (player.hitbox[0] <= hitbox[0] + hitbox[2]):
                    if ((player.hitbox[0] + player.hitbox[2] + 1) >= hitbox[0]):
                        if y_dir < 0:
                            new_target_y = (obj.hitbox[1] + player.hitbox[3]) + 1
                        else:
                            new_target_y = (obj.hitbox[1] + obj.hitbox[3]) + 1
                            
                        new_target = (obj.hitbox[0], new_target_y)
                        print("2,", new_target)
                        global window
                        pygame.draw.circle(window, WHITE, new_target, 5)
                            
    
                    
                    #horizontal = player.hitbox[2] - obj.hitbox[0]
                    #target = (player.x - horizontal, player.y)"""
                
    return new_target

def adjust_position(player, objects, pos):
    new_pos = [pos[0], pos[1]]
    x_coord = 0
    y_coord = 0
    w = player.hitbox[2]
    h = player.hitbox[3]
    for obj in objects:
        
        p_hitbox = (pos[0], pos[1], w, h)
        
        while bm.collideright(p_hitbox, obj.hitbox, player.vel):
            x_coord -= 1
            p_hitbox = (pos[0] + x_coord, pos[1], w, h)
            
        while bm.collideleft(p_hitbox, obj.hitbox, player.vel):
            x_coord += 1
            p_hitbox = (pos[0] + x_coord, pos[1], w, h)
            
        while bm.collidetop(p_hitbox, obj.hitbox, player.vel):
            y_coord -= 1
            p_hitbox = (pos[0] + x_coord, pos[1] + y_coord, w, h)
            
        while bm.collidebottom(p_hitbox, obj.hitbox, player.vel):
            y_coord += 1
            p_hitbox = (pos[0] + x_coord, pos[1] + y_coord, w, h)
            
    if x_coord < 0:
        x_coord -= 1
    elif x_coord > 0:
        x_coord += 1
    
    if y_coord < 0:
        y_coord -= 1
    elif y_coord > 0:
        y_coord += 1
        
    new_pos[0] = new_pos[0] + x_coord
    new_pos[1] = new_pos[1] + y_coord
    
    if new_pos[0] < player.x:
        player.moving[0] = -1
        player.xd = -1
    elif new_pos[0] > player.x:
        player.moving[0] = 1
        player.xd = 1  
    else:
        player.xd = 0
        
    if new_pos[1] < player.y:
        player.moving[1] = -1
        player.yd = -1
    elif new_pos[1] > player.y:
        player.moving[1] = 1
        player.yd = 1
    else:
        player.yd = 0
        
    #print("xd", player.xd)
    #print("yd", player.yd)
        
    direction = False
    i = 0
    while not direction:
        if (player.compass[i][0] == player.xd) and (player.compass[i][1] == player.yd):
            player.point = i
            direction = True
        i += 1
            
    #print(player.point)
    return new_pos

 
def move_to_and_destroy():
    return
    

def pathfind(player, objects, pos):
    if pos[0] < player.x:
        player.xd = -1  
    elif pos[0] > player.x:
        player.xd = 1
    else:
        player.xd = 0
        
    if pos[1] < player.y:
        player.yd = -1  
    elif pos[0] > player.y:
        player.yd = 1
    else:
        player.yd = 0
        
    #print("x:", player.xd)
    #print("y:", player.yd)
    #player.x = player.x + (player.vel * player.xd)
    for obj in objects:
        if bm.collideright(player.hitbox, obj.hitbox):
            player.blocked[0] = True
        
        elif bm.collideleft(player.hitbox, obj.hitbox):
            player.blocked[1] = True
            
        if bm.collidetop(player.hitbox, obj.hitbox):
            player.blocked[3] = True
            
        elif bm.collidebottom(player.hitbox, obj.hitbox):
            player.blocked[2] = True
            
    if ((player.blocked[0] and player.blocked[2])
    or (player.blocked[0] and player.blocked[3])):
        player.direction[0] = False
        player.direction[1] = True
        
    if ((player.blocked[1] and player.blocked[2])
    or player.blocked[1] and player.blocked[3]):
        player.direction[0] = True
        player.direction[1] = False
        
        
    if player.xd < 0:
        if not player.blocked[1]:
            player.direction[0] = True
            player.direction[1] = False
        
            
    if player.blocked[0]:
        pass
    
    elif player.blocked[1]:
        pass
    
    else:
        if player.direction[1]:
            player.x = player.x + player.vel
        
        if player.direction[0]:
            player.x = player.x - player.vel
            
    if player.blocked[2]:
        pass
    
    elif player.blocked[3]:
        pass
        
    else:
        if player.direction[3]:
            player.y = player.y + player.vel
        
        if player.direction[2]:
            player.y = player.y - player.vel
            
    #print("Blocked", player.blocked)
    #print("Direction", player.direction)
            
    player.blocked = [False, False, False, False]
    
    """if player.xd < 0:
            if not bm.collideright(player.hitbox, obj.hitbox):
                player.x = player.x + (player.vel * player.xd)
        elif player.xd > 0:
            if not bm.collideleft(player.hitbox, obj.hitbox):
            
            player.blocked[1] = True
            
        if bm.collideright(player.hitbox, obj.hitbox):
            player.blocked[0] = True"""
            
def pathfinder(player, objects, pos):
    if pos[0] < player.x:
        player.xd = -1  
    elif pos[0] > player.x:
        player.xd = 1
    else:
        player.xd = 0
        
    if pos[1] < player.y:
        player.yd = -1  
    elif pos[0] > player.y:
        player.yd = 1
    else:
        player.yd = 0
        
    for obj in objects:
        if bm.collideright(player.hitbox, obj.hitbox):
            player.blocked[0] = True
        
        elif bm.collideleft(player.hitbox, obj.hitbox):
            player.blocked[1] = True
            
        if bm.collidetop(player.hitbox, obj.hitbox):
            player.blocked[3] = True
            
        elif bm.collidebottom(player.hitbox, obj.hitbox):
            player.blocked[2] = True
            
            
            
    if player.xd < 0:
        if player.blocked[1]:
            if player.yd < 0:
                if player.blocked[2]:
                    player.moving[0] *= -1
                    
            if player.yd > 0:
                if player.blocked[3]:
                    player.moving[0] *= -1
                    
    elif player.xd > 0:
        if player.blocked[0]:
            if player.yd < 0:
                if player.blocked[2]:
                    player.moving[0] *= -1
                    
            if player.yd > 0:
                if player.blocked[3]:
                    player.moving[0] *= -1
                    
    else:
        if player.xd == pos[0]:
            pass
            
                    
            
            
    """if player.xd < 0:
        if player.blocked[1]:
            player.moving[0] = 0
    
    if player.xd > 0:
        if player.blocked[0]:
            player.moving[0] = 0
        
    if player.moving[1] > 0:
        if player.blocked[2]:
            player.moving[1] = -1
            
    if player.moving[1] < 0:
        if player.blocked[3]:
            player.moving[1] = 1"""
            
    """if player.blocked[0] or player.blocked[1]:
        player.moving[0] = 0
        
    else:
        player.moving[0] = player.xd"""
    #print(type(player.moving))
    #print(player.moving[0])
    player.x = player.x + (player.vel * player.moving[0])
        
    """if player.blocked[1] or player.blocked[3]:
        player.moving[1] = 0
        
    else:
        player.moving[1] = player.yd"""
        
    player.y = player.y + (player.vel * player.moving[1])
            
    player.blocked = [False, False, False, False]
    
    
def compass_pathfind(player, objects, pos):
    
    for obj in objects:
        if bm.collideright(player.hitbox, obj.hitbox):
            player.blocked[0] = True
        
        elif bm.collideleft(player.hitbox, obj.hitbox):
            player.blocked[1] = True
            
        if bm.collidetop(player.hitbox, obj.hitbox):
            player.blocked[3] = True
            
        elif bm.collidebottom(player.hitbox, obj.hitbox):
            player.blocked[2] = True
 
        
    """direction = False
    i = 0
    #print("xd", player.xd)
    #print("yd", player.yd)
    while not direction:
       # print(i)
        if (player.compass[i][0] == player.xd) and (player.compass[i][1] == player.yd):
            player.point = i
            direction = True
        i += 1"""
        
    #compass = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 0)]
        
    flag = False
    if player.blocked[0]:
        if player.blocked[2]:
            player.point = 0
            flag = True
        
        elif player.blocked[3]:
            player.point = 0
            flag = True
            
        else:
            player.point = 2
            flag = True
        
    elif player.blocked[1]:
        if player.blocked[2]:
            player.point = 5
            flag = True
        
        elif player.blocked[3]:
            player.point = 5
            flag = True
            
        else:
            player.point = 7
            flag = True
        
    elif player.blocked[2]:
        player.point = 5
        flag = True
        
    elif player.blocked[3]:
        player.point = 0
        flag = True
        
    if not flag:
        direction = False
        i = 0
        #print("xd", player.xd)
        #print("yd", player.yd)
        while not direction:
           # print(i)
            if (player.compass[i][0] == player.xd) and (player.compass[i][1] == player.yd):
                player.point = i
                direction = True
            i += 1
        
    print(player.compass[player.point])
    #if player.x != pos[0]:
    player.x = player.x + (player.vel * player.compass[player.point][0])
        
    #if player.y != pos[1]:
    player.y = player.y + (player.vel * player.compass[player.point][1])
    
    if pos[0] < player.x:
        player.xd = -1  
    elif pos[0] > player.x:
        player.xd = 1
    else:
        player.xd = 0
        
    if pos[1] < player.y:
        player.yd = -1  
    elif pos[1] > player.y:
        player.yd = 1
    else:
        player.yd = 0
            
            
    player.blocked = [False, False, False, False]
            
            
    
    
def move_to_click(player, objects, position, attempts):
    original_position = position
    #Mod_X/Y: Get the distance from the nearest multiple of Player.vel
    pos = collision(player, objects, position)
    if pos[0] == 0 and pos[1] == 0:
        pos = position
        
    if pos[0] < player.x:
        x_dir = -1  
    elif pos[0] > player.x:
        x_dir = 1
    else:
        x_dir = 0

        
    if pos[1] < player.y:
        y_dir = -1
    elif pos[1] > player.y:
        y_dir = 1
    else:
        y_dir = 0
        
    if player.x + (player.vel * x_dir) != pos[0]: #Player's X is still not the Target X
            player.x = player.x + (player.vel * x_dir)
            
    if player.y + (player.vel * y_dir) != pos[1]:
        player.y = player.y + (player.vel * y_dir)
        
    if len(attempts) > 9:
        attempts.clear()
        
    if player.x == pos[0] and player.y == pos[1]:
        attempts.append(1)
        
    else:
        attempts.append(0)
        
    for i in attempts:
        if i == 1:
            flag = i
            
    try:
        if attempts[flag] == 1 and attempts[flag + 2] == 1 and attempts[flag + 4] == 1:
            pass
            #print("Flag is True, now what?")
            
    except: pass#print("index error or smth")
    """IMPORTANT:
        if X or Y keep changing their value by 1, i.e., from 137 to 138 to 137 to 138,
        ADJUST X or Y of point to be 1 HIGHER or LOWER than their original VALUE depending on the way
        X and Y are switching.
        
        
        So the idea is, move X by velocity. Check for a collision in left and right.
        If none exist, direction stays the same.
        If a collision exists, move Y only. While a collision exists in X-direction,
        keep moving Y. If a collision occurs in Y direction, swap X's direction.
        Go until there is a collision in the X direction again.
        If another collision occurs, change Y direction. Repeat.
        
        Move y by velocity. Check for a collision in up and down.
        If none exist, direction stays the same.
    """
    #print(attempts)
    #print(pos)
    #print(player.x, player.y)
        
        
    
    """
    mod_x = pos[0] % player.vel 
    mod_y = pos[1] % player.vel
    
    if pos[0] < player.x:
        x_dir = -1
    
    else:
        x_dir = 1
    
    if mod_x > player.half_vel + 1: #If/Else determines which multiple of Player.vel to go to.
        target_x = pos[0] + mod_x
        
    else:
        target_x = pos[0] - mod_x
        
    if x_dir > 0:
        if player.x + player.vel < target_x + 1: #Player's X is still not the Target X
            player.x = player.x + player.vel
            
    else:
        if player.x - player.vel > target_x - 1: #Player's X is still not the Target X
            player.x = player.x - player.vel
        
    #Now do same thing, but for the Player's Y coordinate.

    if pos[1] < player.y:
        y_dir = -1
    
    else:
        y_dir = 1  
        
    if mod_y > player.half_vel + 1:
        target_y = pos[1] + mod_y
        
    else:
        target_y = pos[1] - mod_y
        
    if y_dir > 0:
        if player.y + player.vel < target_y + 1:
            player.y = player.y + player.vel
            
    else:
        if player.y - player.vel > target_y - 1:
            player.y = player.y - player.vel
            """
            
def I_got_stuck(vertical_flag, horizontal_flag, pos):
    if vertical_flag > 9 or horizontal_flag > 9:
        fixed_pos = [pos[0], pos[1]]
        
        if vertical_flag > 9:
            fixed_pos = [pos[0], pos[1] + 1]
            
        if horizontal_flag > 9:
            fixed_pos = [pos[0] + 1, pos[1]]
            
    return tuple(fixed_pos)
            
    
    
            
def display_sidebar(sprites):
    actions_tab = sprites.actions_tab
    window.blit(actions_tab, (501, 0))
    #window.blit(sprites.gold_ore, (250, 250))
    #window.blit(sprites.rock_1, (100, 150))
    #window.blit(sprites.tree3, (200, 350))
    #window.blit(sprites.mine_label, (575, 50))
    #window.blit(sprites.flower1, (40, 70))
    #window.blit(sprites.bush1, (400, 50))
    
    
    
def Game():
    create_pygame()
    sprites = Sprites()
    objects = create_objects(sprites)
    run = True
    screen = 1
    player = Player(350, 350)
    border = Window()
    click_flag = 0
    select_flag = 0
    pos = (350, 350)
    select_pos = (350, 350)
    new_pos = (350, 350)
    new_select_pos = (350, 350)
    clock = pygame.time.Clock()
    attempts = []
    
    while run:
        pygame.time.delay(17)
        #clock.tick(12)#Framerate
        
        """ == Code for pressing the corner "X" button == """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        """ ============================================= """
        
        if screen == 1:
            
            keys = pygame.key.get_pressed()
            
            mouse_press = pygame.mouse.get_pressed()
            
            if mouse_press[2]:
                click_flag += 1
                
                if click_flag == 1:
                    new_pos = pygame.mouse.get_pos()
                    
                    if new_pos[0] < 500:
                        pos = tuple(adjust_position(player, objects, new_pos))
                        
            else:
                click_flag = 0
                        
            if mouse_press[0]:
                select_flag += 1
                
                if select_flag == 1:
                    new_select_pos = pygame.mouse.get_pos()
                    
                    if new_select_pos[0] < 500:
                        select_pos = new_select_pos
                
                        for i in objects:
                            if i.rect.collidepoint(select_pos):
                                print("True")
                            
            else:
                select_flag = 0
            
            if keys[pygame.K_d]:
                if (player.x + 50) + player.vel < border.right + 1:
                    player.x = player.x + player.vel
                    for w in objects:
                        if bm.collideleft(player.hitbox, w.hitbox, player.vel):
                            player.x = player.x - player.vel
                else: pass
            
            if keys[pygame.K_a]:
                if player.x - player.vel > -1:
                    player.x = player.x - player.vel
                    for x in objects:
                        if bm.collideright(player.hitbox, x.hitbox, player.vel):
                            player.x = player.x + player.vel
                else: pass
            
            if keys[pygame.K_w]:
                if player.y - player.vel > -1:
                    player.y = player.y - player.vel
                    for y in objects:
                        if bm.collidebottom(player.hitbox, y.hitbox, player.vel):
                            player.y = player.y + player.vel
                else: pass
            
            if keys[pygame.K_s]:
                if player.y + player.vel < 501:
                    player.y = player.y + player.vel
                    for z in objects:
                        if bm.collidetop(player.hitbox, z.hitbox, player.vel):
                            player.y = player.y - player.vel
                else: pass

            
        window.fill(BLACK)
        #window.blit(sprites.bg1, (0,0))
        pygame.draw.circle(window, RED, pos, 5)
        #pathfind(player, objects, pos)
        #move_to_click(player, objects, pos, attempts)
        #pathfinder(player, objects, pos)
        compass_pathfind(player, objects, pos)
        player.display(window)
        display_sidebar(sprites)
        draw_objects(objects, window)
        pygame.draw.rect(window, RED, player.hitbox, 1)
        pygame.draw.line(window, RED, (501, 0), (501, 500), 1)
        pygame.display.update()
              
        
    pygame.quit()
        

if __name__ == '__main__': #Run Program
    Game()
