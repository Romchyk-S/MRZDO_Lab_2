# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:55:59 2023

@author: romas
"""

import item_class as ic

import prettytable as pt
    

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
    
    next_group = 1
    
    for i in items:
        
        i.add_to_group(next_group)
        
        try:
            
            groups[i.group].append(i)
            
        except KeyError:
            
            groups[i.group] = [i]
            
        next_group = i.group+1   
    
    return groups   

def form_table(groups: dict, weight_limit = float) -> tuple:
    
    group_table = pt.PrettyTable()
    
    group_table_with_weight_limits = pt.PrettyTable()
    
    group_table_with_u = pt.PrettyTable()
    
    fields = ["№", "Предмети", "Вага", "Цінність"]
    
    fields_with_u = ["№", "Предмети", "Вага", "Цінність", "u_1", "u_2"]
    
    group_table.field_names = fields
    
    group_table_with_weight_limits.field_names = fields
    
    group_table_with_u.field_names = fields_with_u
    
    for k in groups.keys():
        
        v = groups.get(k)
        
        weight, value = 0, 0
        
        max_value_over_weight = 0
        
        for item in v:
            
            weight += item.weight
            
            value += item.value
            
            value_weight_ratio = item.value/item.weight
            
            if value_weight_ratio > max_value_over_weight:
                
                max_value_over_weight = value_weight_ratio
        
        group_table.add_row([k, v, weight, value])
        
        if weight <= weight_limit:
        
            group_table_with_weight_limits.add_row([k, v, weight, value])
            
            group_table_with_u.add_row([k, v, weight, value, value/weight, max_value_over_weight])
        
    return group_table, group_table_with_weight_limits, group_table_with_u