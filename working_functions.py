# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:55:59 2023

@author: romas
"""

import item_class as ic

def get_weight_input() -> float:
    
    try:

        max_weight = float(input("Введіть максимальну вагу рюкзака: "))
        
    except ValueError:
        
        print("Потрібно ввести число")
        
        print()
        
        max_weight = get_weight_input()
        
    return max_weight 

def get_items(file_name: str) -> list:
    
    items = []
    
    with open(file_name) as file:
        
        for line in file:
            
            formatted_line = line.strip().split(" ")
            
            new_item = ic.Item(formatted_line)
            
            items.append(new_item)

    return items


def group_items(items: list) -> dict:
    
    groups = {}
    
    for i in items:
        
        i.add_to_group()
        
        try:
            
            groups[i.group].append(i)
            
        except KeyError:
            
            groups[i.group] = [i]
    
    return groups            