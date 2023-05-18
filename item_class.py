# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:55:24 2023

@author: romas
"""

from __future__ import annotations 

import dataclasses as dc

print()

@dc.dataclass
class Item:
    
    num: int
    
    weight: float
    
    value: float
    
    group: int
    
    
    def __init__(self, parms: list) -> None:
        
        self.num = int(parms[0])
        
        self.weight = float(parms[1])
        
        self.value = float(parms[2])
        
        self.group = 0
        
        try:
            
            self.previous_item = int(parms[3])
            
        except:
            
            self.previous_item = None
            
    def __repr__(self) -> str:
        
        return f"{self.num}"
    
    @property
    def num(self) -> int:
        
        return self._num
    
    @num.setter
    def num(self, num: int) -> None:
        
        self._num = num
        
    @property
    def weight(self) -> float:
        
        return self._weight
    
    @weight.setter
    def weight(self, weight: float) -> None:
        
        self._weight = weight
  
    @property
    def value(self) -> float:
        
        return self._value
    
    @value.setter
    def value(self, value: float) -> None:
        
        self._value = value
        
    @property
    def group(self) -> int:
        
        return self._group
    
    @group.setter
    def group(self, group: int) -> None:
        
        self._group = group
               
    @property
    def previous_item(self) -> int|Item:
        
        return self._previous_item
    
    @previous_item.setter
    def previous_item(self, previous_item: int|Item) -> None:
        
        self._previous_item = previous_item     
        
    def add_link_to_item(self, items: list) -> Item:
        
        if self.previous_item != None:
            
            self.previous_item = items[self.previous_item-1]
            
        return self
        
    
    def add_to_group(self, next_group: int):
        
        if self.group == 0:
        
            if self.previous_item == None:
                
                self.group = next_group
                
            else:
                
                if self.previous_item.group != 0:
                
                    self.group = self.previous_item.group
                    
                else:
                    
                    self.previous_item.add_to_group(next_group)
                    
                    self.group = self.previous_item.group