# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:47:09 2023

@author: romas
"""

import prettytable as pt


def print_items_to_table(items: list) -> None:
    
    table = pt.PrettyTable()
    
    fields = ["№", "Вага", "Цінність", "Попередник"]
    
    table.field_names = fields
    
    for i in items:
        
        table.add_row([i.num, i.weight, i.value, i.previous_item])

    print(table)
    
    print()

def group_items(items: list) -> dict:
    
    groups = {}
    
    next_group = 1
    
    for i in items:
        
        i.add_to_group(next_group)
        
        try:
            
            groups[i.group].append(i)
            
        except KeyError:
            
            groups[i.group] = [i]
            
            next_group += 1  
        
    order_items_in_groups(groups)
    
    return groups   

def order_items_in_groups(groups: dict) -> None:
    
    for g in groups:
  
        if len(groups[g]) > 1:
            
            new_list = []
            
            for h in groups[g]:
                
                is_previous = False
                
                for j in groups[g]:
                    
                    if j.previous_item == h:
                        
                        is_previous = True
                        
                        break
                    
                if not(is_previous):
                    
                    new_list.append(h)
            
            item = new_list[0]
            
            while item.previous_item != None:
                
                item = item.previous_item
                
                new_list.append(item)
            
            groups[g] = new_list[::-1]

def form_table(groups: dict, weight_limit: float) -> tuple:
    
    added_rows = 0
    
    group_table = pt.PrettyTable()
    
    group_table_with_weight_limits = pt.PrettyTable()
    
    group_table_with_u = pt.PrettyTable()
    
    groups_copy = {}
    
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
            
            weight += round(item.weight, 2)
            
            value += round(item.value, 2)
            
            value_weight_ratio = item.value/item.weight
            
            if value_weight_ratio > max_value_over_weight:
                
                max_value_over_weight = round(value_weight_ratio, 2)
                
        weight = round(weight, 2)
        
        value = round(value, 2)
        
        group_table.add_row([k, v, weight, value])
        
        if weight <= weight_limit:
            
            value_weight_ratio = round(value/weight, 2)
        
            group_table_with_weight_limits.add_row([k, v, weight, value])
            
            group_table_with_u.add_row([k, v, weight, value, value_weight_ratio, max_value_over_weight])
            
            groups_copy[k] = [v, weight, value, value_weight_ratio, max_value_over_weight]
            
            added_rows += 1
        
    return group_table, group_table_with_weight_limits, group_table_with_u, groups_copy, added_rows

def print_tables(table_1: pt.PrettyTable(), table_2: pt.PrettyTable(), table_3: pt.PrettyTable(), added_rows: int) -> None:
    
    print("Таблиця груп")

    print(table_1)

    print()

    print("Таблиця груп без надто важких")

    print(table_2)

    print()
    
    if added_rows != 0:

        print("Таблиця груп із відносною цінністю")
    
        print(table_3)
    
        print()
    
        print("Таблиця груп, сортована за u_1")
        
        print(table_3.get_string(sortby="u_1", reversesort=True))
        
        print()
        
        print("Таблиця груп, сортована за u_2")
    
        print(table_3.get_string(sortby="u_2", reversesort=True))