# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 12:40:51 2023

@author: alexe
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
            if ((agr[0] + agr[2] + 1) > res[0]) and (agr[0] <  res[0] + res[2]):
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
        