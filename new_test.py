# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:00:12 2023

@author: Lionguy7
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:07:09 2023

@author: Lionguy7
"""

#------------------------------------------
""" lol ignore this
TO DO LIST ===============================
Add more ground sprites
Make Pause menu
make Main Menu
Add more Sound Effects
Fix death screen
add eating animation
END TODO =================================
"""
#------------------------------------------

import pygame
from boxmeta import BoxMeta as bm
from _215_game_classes import GameClasses as gc
from _215_sprites import Sprites
from _215_items import Items
from _215_objects import objects, gatherables, ground_deco, GroundSprite

x=100
y=100
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
FPS = 30

window = pygame.display.set_mode((750, 500))
#window = pygame.display.set_mode((0,0), pygame.RESIZABLE)


def create_pygame(): #initializes Pygame screen
    pygame.init()
    pygame.display.set_caption("Quest 215")
    pygame.display.set_icon(pygame.image.load("slime_dude.png"))
    pygame.font.init()
    #print(pygame.font.get_fonts())
    
        
class Window():
    def __init__(self):
        size = pygame.display.get_window_size()
        #print(size)
        self.left = 0
        self.right = size[0]
        self.top = 0
        self.bottom = size[1]
        self.position = (0,0)
        self.tick = 0
        
    def resize(self):
        size = pygame.display.get_window_size()
        #print("Resized:", size)
        self.left = 0
        self.right = size[0]
        self.top = 0
        self.bottom = size[1]
        self.position = (0,0)
        
class Arrow_Indicator():
    def __init__(self, x, y):
        self.x = x
        self.y = 0
        self.offset_y = -30
        self.origin = (x, y)
        
class Chat():
    chat_log = []
    last_updated = 0
    __hide = 5 * FPS
    show = True
    prev_mes = ""
    pmcount = 1
    
    def clear_chat(self):
        if len(self.chat_log) > 5:
            self.chat_log.pop(4)
            
    def display(self, window):
        if self.show:
            y = 480
            for ch in self.chat_log:
                message = ch.content
                if ch.count > 1:
                    message += " ({})".format(ch.count)
                window.blit(self.font.render(message, True, BLACK), (0, y))
                y -= 15
                
            
    def hide(self):
        if self.last_updated > self.__hide:
            self.show = False
        
    def add(self, message):
        if len(self.chat_log) > 0:
            if not self.chat_log[0].compare(message):         
                self.chat_log.insert(0, ChatMessage(message))
        else:
            self.chat_log.append(ChatMessage(message))
            
        self.last_updated = 0
        self.show = True
        
    def increment(self):
        self.last_updated += 1
        
    def chat(self, window):
        self.clear_chat()
        self.display(window)
        self.increment()
        self.hide()
        
class ChatMessage():
    def __init__(self, content):
        self.content = content
        self.count = 1
        
    def increment(self):
        self.count += 1
        
    def compare(self, other):
        state = False
        if other == self.content:
            self.increment()
            state = True
            
        return state
        
        
def sort_objects(objects):
    k = len(objects)
    j = 0
    
    while j <= k:
        for i in range(len(objects)):
            try:
                if objects[i].hitbox[1] > objects[i + 1].hitbox[1]:
                    temp = objects[i]
                    objects[i] = objects[i + 1]
                    objects[i + 1] = temp
                    
            except IndexError:
                #print("End of list")
                pass
                
        j += 1
            
    #for obj in objects:
        #print(obj.hitbox)
                
                
def create_enemies(sprites):
    enemies = []
    slime_dude = gc.Slime(sprites.slime, sprites.slime_angry, 20, 155, 155)
    slime_dude2 = gc.Slime(sprites.slime, sprites.slime_angry, 20, 600, 220)
    
    enemies.append(slime_dude)
    enemies.append(slime_dude2)
    
    return enemies
    
def object_loop(player, all_objects, window, gatherables, score, hits, chat,
                point = (-999999, -999999)):
    under = []
    over = []
    i = 0
    for obj in all_objects:
        if not obj.destroyed:
            
            #Assign precedence to object's sprite
            if player.collision_hitbox[1] >= obj.hitbox[1] + obj.hitbox[3]:
                under.append(obj)
            else:
                over.append(obj)       
            
            #Destroy an object
            if bm.collisions(player.get_hit_range(window), obj.hitbox):
                if player.click_flag == 1:
                    if player._cooldown == 0:
                        if obj.health > 0:
                            if obj.obj_type == "minable":
                                if player.item == "pickaxe":
                                    if bm.containspoint(point, obj.area):
                                        hits.append(True)
                                        player.animation_facing = player.facing
                                        player.change_animation = True
                                        gc.SoundEffects.pickaxe_on_rock.play()
                                        obj.health -= 1
                                        #obj.show_health = True
                                        obj.health_count = 2 * FPS
                                        player.activate_cooldown()
                                        chat.add("{} took damage".format(obj.name))
                            
                            if obj.obj_type == "chopable":
                                if player.item == "axe":
                                    if bm.containspoint(point, obj.area):
                                        hits.append(True)
                                        player.animation_facing = player.facing
                                        player.change_animation = True
                                        gc.SoundEffects.axe_on_wood.play()
                                        obj.health -= 1
                                        #obj.show_health = True
                                        obj.health_count = 2 * FPS
                                        player.activate_cooldown()
                                        chat.add("{} took damage".format(obj.name))
                                        
                                    
                        if obj.health == 0:
                            obj.destroyed = True
                            if "Large" in obj.name:
                                score.score += 20
                            else:
                                score.score += 5
                            obj.drop_item(gatherables)
                            obj.dropped = True
                            
                            if not obj.respawn:
                                all_objects.remove(obj)
                
                if player.right_click_flag == 1:
                    if obj.name == "Wood Gate":    
                        values = Items.items["Wood Gate Open"]["hitbox"]
                        x = obj.origin[0]
                        y = obj.origin[1]
                        new_hitbox = (x, y + values[1], values[2], values[3])
        
                        all_objects[i] = gc.Object("Wood Gate Open",
                                Items.items["Wood Gate Open"]["icon"],
                                Items.items["Wood Gate Open"]["type"], 4,
                                (x, y), new_hitbox,(x, y, 40, 40), False)
                        gc.SoundEffects.wood_gate_open.play()
                        
                        
                    if obj.name == "Wood Gate Open":    
                        values = Items.items["Wood Gate"]["hitbox"]
                        x = obj.origin[0]
                        y = obj.origin[1]
                        new_hitbox = (x, y + values[1], values[2], values[3])
        
                        all_objects[i] = gc.Object("Wood Gate",
                                Items.items["Wood Gate"]["icon"],
                                Items.items["Wood Gate"]["type"], 4,
                                (x, y), new_hitbox, (x, y, 40, 40), False)
                        gc.SoundEffects.wood_gate_close.play()
                        
                    
                    if obj.name == "Bed":
                        if bm.containspoint(point, obj.area):
                            player.spawnpoint = [obj.origin[0] + 5, obj.origin[1]]
                            chat.add("Reset Player's spawn")
                        
        #Respawn an Object if it can be respawned
        else:
            if obj.respawn:
                obj.seconds_count += 1
                if obj.seconds_count >= obj.respawn_at:
                    if not bm.collisions(player.hitbox, obj.hitbox):
                        obj.destroyed = False
                        obj.health = obj.maxhealth
                        obj.seconds_count = 0
                        
        i += 1
            
    if player.click_flag == 1:
        if True not in hits:
            if player._cooldown == 0:
                gc.SoundEffects.air_swipe.play()
    
    for obj in under:
        obj.draw(window)
        
    player.display(window)
    
    for obj in over:
        obj.draw(window)
        
    
def enemy_loop(player, enemies, objects, window, border, chat):
    for emy in enemies:
        emy.display(window, objects, border)
        if not emy.knocked_back:
            emy.check_for_player(player, objects, chat)
        
        
def attack(player, enemies, window, score, hits, chat):
    if player.click_flag == 1:
        box = player.get_hit_range(window)
        
        if player.item == "sword":
            if player._cooldown == 0:
                
                for emy in enemies:
                    if bm.collisions(box, emy.hitbox):
                        if not emy.dead:
                            hits.append(True)
                            #gc.SoundEffects.sword_hit_slime.play()
                            emy.knocked_back = True
                            emy.kb_time = int(FPS / 2)
                            emy.find_knockback_direction(player)
                            emy.health -= 5
                            player.animation_facing = player.facing
                            player.change_animation = True
                            player.activate_cooldown(1)
                            chat.add("Slime took damage")
                            #print("Slime Dude's HP:", emy.health)
                            
                            if emy.health <= 0:
                                score.score += 50
                                emy.kb_time = 0
                                emy.knocked_back = False
                    
                else: pass
                    #print("Can't attack, enemy out of range.")
                   # gc.SoundEffects.air_swipe.play()
                   
def position_object(player, objects, window, pos):
    x_pos = 0
    y_pos = 0
    if player.can_place():
        x_pos = (pos[0]) - (pos[0] % 40)
        y_pos = (pos[1]) - (pos[1] % 40)
        
    return [x_pos, y_pos]
        
def draw_placeable(player, pos, sprites):
    if player.placing:
        sprite = player.get_sprite(player)
        window.blit(sprite, (pos[0], pos[1]))
                    
def place_object(player, objects, pos, chat):
    if ((abs(pos[0] - player.x) < 121)
    and abs(pos[1] - player.y) < 121):
        
        if player.item != "null":
            item_name = player.item
            if Items.items[player.item]["placeable"]:
                values = Items.items[player.item]["hitbox"]
                added = False
                blocked = False
                if values != 0:
                    new_hitbox = (pos[0] + values[0],
                                  pos[1] + values[1], values[2], values[3])
            
                    for obj in objects:
                        if bm.occupied(new_hitbox, obj.hitbox):
                            blocked = True
        
                if not blocked:
                    if player.item == "Stone Wall":
                        gc.Wall.place_wall(pos, objects)
                        added = True
                        
                    else:
                        if "Floor Tile" not in player.item:
                            new = gc.Object(player.item, Items.items[player.item]["icon"],
                                            Items.items[player.item]["type"], 4,
                                            (pos[0], pos[1]), new_hitbox,
                                            (pos[0], pos[1], 40, 40), False)
                        
                            objects.append(new)
                            added = True
                                                    
                        if "Floor Tile" in player.item:
                            new = GroundSprite(Items.items[player.item]["icon"],
                                               pos)
                            ground_deco.append(new)
                            added = True
                    
                    if added:
                        sort_objects(objects)
                        player.placing = False
                        player.remove_item()
                        chat.add("Placed {}".format(item_name))
        
            
def display_ground(sprites, gatherables):
    for deco in ground_deco:
        window.blit(deco.icon, deco.location) 
    
    for item in gatherables:
        if item.despawns:
            if (item.alive_for >= item.despawn_at
                or item.picked_up):
                gatherables.remove(item)
            
        item.display(window)
        
def display_GUI(player, window, sprites, font, border, score, arrow, chat):
    player.display_hotbar(window, sprites, font)
    player.display_health(window, sprites)
    window.blit(sprites.label_back1, (border.right - 155, 6))
    window.blit(font.render("Score: {:,}".format(score.score),
                                True, BLACK), (border.right - 150, 10))
    chat.chat(window)
    
    if border.tick >= 12:
        halfway = -1
    else:
        halfway = 1
        
    arrow.offset_y = ((border.tick % 2) * halfway) + arrow.offset_y
    arrow.y = player.y + arrow.offset_y
    arrow.x = player.x
    
    window.blit(sprites.ring_i, (arrow.x, player.y - 18))
    window.blit(sprites.arrow_i, (arrow.x, arrow.y))
    
    
class Score():
    score = 0
    
def Game():
    create_pygame()
    sprites = Sprites()
    #objects = create_objects(sprites)
    ignored = ["Wood Gate Open"]
    sort_objects(objects)
    enemies = create_enemies(sprites)
    #gatherables = create_gatherables(sprites)
    respawn = gc.Crafting.Button("Respawn", (275, 255, 200, 40), (310, 250))
    quit_button = gc.Crafting.Button("Quit", (305, 305, 140, 40), (345, 302))
    saved_objs = []
    run = True
    score = Score()
    directioned = False
    screen = 1
    font_30 = pygame.font.SysFont("caladea", 30, True, False)
    font_20 = pygame.font.SysFont("caladea", 20, False, True)
    font_20_bold = pygame.font.SysFont("caladea", 20, True, False)
    chat_font = pygame.font.SysFont("caladea", 12, True, False)
    labels = [""]
    checks = [False, -1]
    slots = []
    hits = []
    slot = 0
    call = ""
    c_flag = 0
    r_flag = 0
    m_flag = 0
    f_flag = 0
    left_point = (-99999, -99999)
    place_at = [0, 0]
    player = gc.Player(350, 350)
    player.change_item()
    border = Window()
    arrow = Arrow_Indicator(player.x + 10, player.y - 30)
    craft_menu = gc.Crafting()
    inventory = gc.Inventory()
    slimes = [gc.AimlessSlime(1, 1), gc.AimlessSlime(-1, -1)]
    chat = Chat()
    chat.font = chat_font
    clock = pygame.time.Clock()
    
    while run:
        #pygame.time.delay(17)
            
        clock.tick(FPS)#Framerate
        
        """ == Code for pressing the corner "X" button == """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        """ ============================================= """
        
        
        if screen == 1:
            
            keys = pygame.key.get_pressed()
            
            mouse_press = pygame.mouse.get_pressed()
                        
            if mouse_press[0]:
                left_point = pygame.mouse.get_pos()
                #print(left_point)
                player.click_flag += 1
                attack(player, enemies, window, score, hits, chat)
                            
            else:
                player.click_flag = 0
                
            
            if mouse_press[2]:
                left_point = pygame.mouse.get_pos()
                player.right_click_flag += 1
                pos = pygame.mouse.get_pos()
                if player.can_place():
                    player.placing = True
                    place_at = position_object(player, objects, window,
                                               pos)
                
                if player.right_click_flag == 1:
                    player.can_eat(chat)
                #else:
                #    player.interact(objects)
                            
            else:
                if player.placing:
                    place_object(player, objects, place_at, chat)
                    
                player.placing = False
                player.right_click_flag = 0
                
            for obj in objects:
                #Left, Right, Up, Down
                if not obj.destroyed:
                    if obj.name not in ignored:
                        if bm.collideright(player.collision_hitbox, obj.hitbox):
                            player.blocked[0] = True
                            if obj not in saved_objs:
                                saved_objs.append(obj)
                            
                        if bm.collideleft(player.collision_hitbox, obj.hitbox):
                            player.blocked[1] = True
                            if obj not in saved_objs:
                                saved_objs.append(obj)
                            
                        if bm.collidebottom(player.collision_hitbox, obj.hitbox):
                            player.blocked[2] = True
                            if obj not in saved_objs:
                                saved_objs.append(obj)
                        
                        if bm.collidetop(player.collision_hitbox, obj.hitbox):
                            player.blocked[3] = True
                            if obj not in saved_objs:
                                saved_objs.append(obj)
                        
                
            if keys[pygame.K_LSHIFT]:
                if player.stamina > 0:
                    if player.walk_frame % 2 == 0:
                        player.walk_frame += 1
                    boost = 2
                    player.stamina -= 1
                else:
                    boost = 1
                    
            else:
                boost = 1
                if player.stamina < (5 * FPS):
                    player.stamina += 1
                
                
            if not player.animation_lock and not player.dead:
                if keys[pygame.K_d]:
                    player.stopper = 0
                    player.animation_facing = "right"
                    player.walking = True
                    player.change_animation = True
                    directioned = True
                    if (player.x + 50) + player.vel < border.right + 1:
                        if not player.blocked[1]:
                            player.x = player.x + (player.vel * boost)
    
                if keys[pygame.K_a]:
                    player.stopper = 0
                    player.change_animation = True
                    player.animation_facing = "left"
                    player.walking = True
                    directioned = True
                    if player.x - player.vel > -1:
                        if not player.blocked[0]:
                            player.x = player.x - (player.vel * boost)
                                
                
                if keys[pygame.K_w]:
                    player.stopper = 0
                    player.walking = True
                    if not directioned:
                        player.animation_facing = player.facing
                    player.change_animation = True
                    if player.y - player.vel > -1:
                        if not player.blocked[2]:
                            player.y = player.y - (player.vel * boost)
                
                if keys[pygame.K_s]:
                    player.stopper = 0
                    player.walking = True
                    if not directioned:
                        player.animation_facing = player.facing
                    player.change_animation = True
                    if player.y + player.vel < border.bottom:
                        if not player.blocked[3]:
                            player.y = player.y + (player.vel * boost)
                   
            for s_obj in saved_objs:
                diffx, diffy = bm.resolve(player.collision_hitbox,
                                          s_obj.hitbox, player.blocked)
                #print(diffx, diffy)
                player.x += diffx
                player.y += diffy
                
            saved_objs.clear()
            
            player.blocked = [False, False, False, False]
            #print(player.walking)
            
            if keys[pygame.K_1]:
                player.current_slot = 25
               # player.change_item()
            if keys[pygame.K_2]:
                player.current_slot = 26
                #player.change_item()
            if keys[pygame.K_3]:
                player.current_slot = 27
                #player.change_item()
            if keys[pygame.K_4]:
                player.current_slot = 28
                #player.change_item()
            if keys[pygame.K_5]:
                player.current_slot = 29
                #player.change_item()
            if keys[pygame.K_6]:
                player.current_slot = 30
            
            player.change_item()
                
                
            if keys[pygame.K_n]:
                border.resize()
                
            if keys[pygame.K_m]:
                m_flag += 1
                if m_flag == 2 * FPS:
                    player.x = player.spawnpoint[0]
                    player.y = player.spawnpoint[1]
            else:
                m_flag = 0
                
            if keys[pygame.K_c]:
                c_flag += 1
                if c_flag == 1:
                    screen = 2
            else:
                c_flag = 0
                
            if keys[pygame.K_r]:
                r_flag += 1
                if r_flag == 1:
                    screen = 3
            else:
                r_flag = 0
                
                
            if keys[pygame.K_f]:
                f_flag += 1
                
                if f_flag == 1:
                    for drop in gatherables:
                        if f_flag == 1:
                            if bm.collisions(player.hitbox, drop.hitbox):
                                if not drop.picked_up:
                                    player.pickup_item(drop)
                                    chat.add("Picked up {} x{:,}".format(
                                            drop.name, drop.amount))
                                    f_flag += 1
                                
            else:
                f_flag = 0
                            

            border.tick += 1
            
            if border.tick == 24:
                border.tick = 0
                
            window.fill(BLACK)
            window.blit(sprites.grass4, (0,0))
            #player.display(window)
            player.cooldown()
            display_ground(sprites, gatherables)
            enemy_loop(player, enemies, objects, window, border, chat)
            object_loop(player, objects, window, gatherables, score,
                        hits, chat, left_point)
            draw_placeable(player, place_at, sprites)
            display_GUI(player, window, sprites, font_20_bold, border, score,
                        arrow, chat)
            player.walking = False
            directioned = False
            hits.clear()
            
            if player.health <= 0 or player.dead:
                if player.death_state == 0:
                    player.death_state = 1
                    chat.add("Player was slain")
                
                if player.death_state == 1:
                    player.frame = 0
                    player.animation_tick = 0
                    player.death_state += 1
                    
                player.die(window, sprites)
                if player.death_state == 3:
                    player.frame = 0
                    player.animation_tick = 0
                    player.death_state = 1
                    screen = 4
            
            #pygame.draw.rect(window, RED, player.hitbox, 1)
            #pygame.draw.rect(window, RED, player.collision_hitbox, 1)
    
            #pygame.draw.rect(window, RED, (0,0,border.right,border.bottom), 1)
            #pygame.draw.line(window, RED, (501, 0), (501, 500), 1)
            pygame.display.update()
      
        if screen == 2:
            
            keys = pygame.key.get_pressed()
            
            mouse_press = pygame.mouse.get_pressed()
                        
            if mouse_press[0]:
                player.click_flag += 1
                if player.click_flag == 1:
                    pos = pygame.mouse.get_pos()
                    call = craft_menu.check_buttons(pos, window, labels)
                    
                    if call == "Craft":
                        craft_menu.craft(player, labels[0])
                        
                    if call == "Close":
                        screen = 1
                        labels[0] = ""
                        call = ""
                            
            else:
                player.click_flag = 0
                
            if keys[pygame.K_c]:
                c_flag += 1
                if c_flag == 1:
                    c_flag += 1
                    screen = 1
                    labels[0] = ""
                    call = ""
            else:
                c_flag = 0
                
           
            item_label = font_20_bold.render(labels[0], True, BLACK)
            window.blit(sprites.crafting_menu, (0,0))
            craft_menu.display_info(player, labels, window,
                                    font_30, font_20, font_20_bold)
            window.blit(item_label, (325, 105))
            craft_menu.draw(window)
            pygame.display.update()
            
        if screen == 3:
            
            keys = pygame.key.get_pressed()
            
            mouse_press = pygame.mouse.get_pressed()
            
            if keys[pygame.K_LSHIFT]:
                shift = True
                
            else:
                shift = False
            
            if mouse_press[0]:
                player.click_flag += 1
                if player.click_flag == 1 and not shift:
                    pos = pygame.mouse.get_pos()
                    checks = inventory.check_slot(pos)
                    if checks[0]:
                        slots.append(checks[1])
                        slot = slots[0]
                    
                    if len(slots) == 2:
                        inventory.swap_slots_fixed(player, slots)
                        checks = [False, -1]
                        slots = []
                        slot = -1
                    #inventory.choose_slot(pos)
                elif player.click_flag == 1 and shift:
                    pos = pygame.mouse.get_pos()
                    inventory.quick_move(player, pos)
                    
            else:
                player.click_flag = 0
            
            if keys[pygame.K_r]:
                r_flag += 1
                if r_flag == 1:
                    r_flag += 1
                    screen = 1
                    slot = 0
                    slots = []
                    checks = [False, -1]
                    
            else:
                r_flag = 0
            
            window.fill(BLACK)
            window.blit(sprites.grass4, (0,0))
            inventory.display(sprites, player, font_20, window)
            
            if checks[0]:
                if slot < 24:
                    window.blit(sprites.chosen_slot,
                            (inventory.slots[slot].hitbox[0] - 2,
                             inventory.slots[slot].hitbox[1] - 2))
                else:
                    window.blit(sprites.chosen_slot,
                            (inventory.hotbar[slot - 24].hitbox[0] - 2,
                             inventory.hotbar[slot - 24].hitbox[1] - 2))
                
            pygame.display.update()
            
        if screen == 4:
            
            mouse_press = pygame.mouse.get_pressed()
            
            if mouse_press[0]:
                player.click_flag += 1
                if player.click_flag == 1:
                    pos = pygame.mouse.get_pos()
                    #print(pos)
                    if bm.containspoint(pos, respawn.hitbox):
                        player.reset_death()
                        score.score = 0
                        screen = 1
                        for slime in slimes:
                            slime.reset()
                            
                    if bm.containspoint(pos, quit_button.hitbox):
                        run = False
                    
            else:
                player.click_flag = 0
            
            for slime in slimes:
                slime.move(border)
            
            window.fill(BLACK)
            window.blit(sprites.grass4, (0, 0))
            
            for slime in slimes:
                window.blit(sprites.slime, (slime.x, slime.y))
                
            window.blit(sprites.black_screen, (0, 0))
            window.blit(sprites.chainlink, (200, -47))
            window.blit(sprites.chainlink, (200, 44))
            window.blit(sprites.chainlink, (200, 135))
            window.blit(sprites.chainlink, (530, -47))
            window.blit(sprites.chainlink, (530, 44))
            window.blit(sprites.chainlink, (530, 135))
            window.blit(sprites.big_label, (175, 200))
            you_died = font_30.render("You Obtained Deceasement", True, BLACK)
            window.blit(you_died, (int(border.right / 2) - 190,
                                   int(border.bottom / 2) - 47))
            
            window.blit(sprites.green_button, (275, 255))
            window.blit(sprites.red_button, (305, 305))
            respawn_label = font_30.render(respawn.name, True, BLACK)
            quit_label = font_30.render(quit_button.name, True, BLACK)
            window.blit(respawn_label, respawn.pos)
            
            window.blit(quit_label, quit_button.pos)
            #pygame.draw.rect(window, RED, (respawn.hitbox), 1)
            #pygame.draw.rect(window, RED, (quit_button.hitbox), 1)
            
            pygame.display.update()
            
        
    pygame.quit()   

if __name__ == '__main__': #Run Program
    Game()
