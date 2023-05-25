# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:45:51 2023

@author: romas
"""

import random as r

import item_class as ic


def create_items(item_amount: int, lower_weight: float, upper_weight: float, lower_value: float, upper_value: float, probability: float) -> list:
    
    items = []
    
    previous_order = [i for i in range(1, item_amount+1)]
    
    i = 0
    
    while i < item_amount:
        
        num = r.uniform(0.0, 1.0)
        
        item_weight = round(r.uniform(lower_weight, upper_weight), 2)
        
        item_value = round(r.uniform(lower_value, upper_value), 2)
        
        if num <= probability:
            
            previous_item = r.choice(previous_order)
            
            while previous_item == i+1:
                
                previous_item = r.choice(previous_order)
        
            new_item = ic.Item([i+1, item_weight, item_value, previous_item])
            
            previous_order.remove(previous_item)
        
        else:
            
            new_item = ic.Item([i+1, item_weight, item_value])
            
        items.append(new_item)
        
        i += 1
        
    return items

def get_items_from_file(file_name: str) -> list:
    
    items = []
    
    with open(file_name) as file:
        
        for line in file:
            
            formatted_line = line.strip().split(" ")
            
            new_item = ic.Item(formatted_line)
            
            items.append(new_item)

    return items
