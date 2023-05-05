# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:41:32 2023

@author: Lionguy7
"""

class BoxMeta():
    
    def collideright(agr, res, a = 0):
        right = False
        
        if (agr[1] < res[1] + res[3]) and (agr[1]  + agr[3] > res[1]):
            if (agr[0] + agr[2] > res[0]) and (agr[0] <=  res[0] + res[2]):
                right = True
        
        return right
    
    def collideleft(agr, res, a = 0):
        left = False
        if (agr[1] < res[1] + res[3]) and (agr[1]  + agr[3] > res[1]):
            if ((agr[0] + agr[2]) >= res[0]) and (agr[0] <  res[0] + res[2]):
                left = True
                
        return left
    
    def collidetop(agr, res, a = 0):
        top = False
        
        if ((agr[1] + agr[3]) >= res[1]) and (agr[1] < res[1] + res[3]):
            if (agr[0] + agr[2] > res[0]) and (agr[0]  < res[0] + res[2]):
                top = True
                
        return top
    
    def collidebottom(agr, res, a = 0):
        bottom = False
        
        if (agr[1] <= res[1] + res[3]) and (agr[1]  + agr[3] > res[1]):
            if (agr[0] + agr[2] > res[0]) and (agr[0] <  res[0] + res[2]):
                bottom = True

        return bottom
        
    def collisions(agr, res, a = 0):
        flag = False
        if (BoxMeta.collideleft(agr, res, a)
            or BoxMeta.collideright(agr, res, a)
            or BoxMeta.collidetop(agr, res, a)
            or BoxMeta.collidebottom(agr, res, a)):
            flag = True
            
        return flag
    
    
    def resolve(agr, res, blocked):
        #Blocked = [LEFT, RIGHT, UP, DOWN]
        to_right = 0
        to_left = 0
        to_top = 0
        to_bottom = 0
        
        diffx = 0
        diffy = 0
        
        if blocked[0]:
            to_right = (agr[0] + agr[2]) - res[0]
            
        if blocked[1]:
            to_left = res[0] + res[2] - agr[0]
            
        if blocked[3]:
            to_bottom = res[1] + res[3] - agr[1]
        
        if blocked[2]:
            to_top = (agr[1] + agr[3]) - res[1]
        
        
        if (to_right < to_left
            and to_right < to_top
            and to_right < to_bottom):
            diffx = -to_right
            
        elif (to_left < to_right
            and to_left < to_top
            and to_left < to_bottom):
            diffx = to_left
            
        elif (to_top < to_right
            and to_top < to_left
            and to_top < to_bottom):
            diffy = -to_top
            
        elif (to_bottom < to_right
            and to_bottom < to_left
            and to_bottom < to_top):
            diffy = to_bottom
            
        else:
            if to_right < to_left:
                x = to_right
                
            else:
                x = to_left
                
            if to_top < to_bottom:
                y = to_top
                
            else:
                y = to_bottom
                
            if x < y:
                diffx = x
                diffy = 0
                
            else:
                diffx = 0
                diffy = y
            
            
        #print("Top: {}, Bottom: {}, Left: {}, Right: {}".format(
        #        to_bottom,to_top, to_left, to_right))
            
        return diffx, diffy
    
    def absolute_resolve(agr, res, blocked):
        #Blocked = [LEFT, RIGHT, UP, DOWN]
        to_right = 0
        to_left = 0
        to_top = 0
        to_bottom = 0
        
        diffx = 0
        diffy = 0
        
        if blocked[0]:
            to_right = (agr[0] + agr[2]) - res[0]
            
        if blocked[1]:
            to_left = res[0] + res[2] - agr[0]
            
        if blocked[2]:
            to_bottom = res[1] + res[3] - agr[1]
        
        if blocked[3]:
            to_top = (agr[1] + agr[3]) - res[1]
        
        if (to_right < to_left
            and to_right < to_top
            and to_right < to_bottom):
            diffx = -to_right
            
        else:
            diffx = to_left
            
        if (to_top < to_right
            and to_top < to_left
            and to_top < to_bottom):
            diffy = -to_top
            
        else:
            diffy = to_bottom
            
        return diffx, diffy
    
    def containspoint(point, hitbox):
        state = False
        
        if (point[0] >= hitbox[0]
        and point[0] <= hitbox[0] + hitbox[2]):
                    
            if (point[1] >= hitbox[1]
            and point[1] <= hitbox[1] + hitbox[3]):
                state = True
                
        return state
    
    
    def occupied(first, second):
        state = False
        if first[2] > second[2]:
            agr = first
            res = second
            
        else:
            agr = second
            res = first
        
        if BoxMeta.collisions(agr, res):
            state = True
            
        return state
            
            
            
            

            
            
            
            
