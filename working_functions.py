# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:55:59 2023

@author: romas
"""

import item_class as ic

import prettytable as pt

import binarytree as bt

import random as r
    
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
            
        next_group = i.group+1   
    
    return groups   

def form_table(groups: dict, weight_limit: float) -> tuple:
    
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
        
    return group_table, group_table_with_weight_limits, group_table_with_u, groups_copy

def print_tables(table_1: pt.PrettyTable(), table_2: pt.PrettyTable(), table_3: pt.PrettyTable()) -> None:
    
    print("Таблиця груп")

    print(table_1)

    print()

    print("Таблиця груп без надто важких")

    print(table_2)

    print()

    print("Таблиця груп із відносною цінністю")

    print(table_3)

    print()

    print("Таблиця груп, сортована за u_1")
    
    print(table_3.get_string(sortby="u_1", reversesort=True))
    
    print()
    
    print("Таблиця груп, сортована за u_2")

    print(table_3.get_string(sortby="u_2", reversesort=True))

def calculate_u_b(value: float, max_weight: float, weight: float, group_next: list, index: int) -> float:
    
    u_next = group_next[1][index]

    return value + (max_weight-weight)*u_next

def build_vertex_including(groups_sort: list, group: list, weight: float, value: float) -> tuple[float]:
    
    group_parameters = group[1]
    
    weight_node = weight+group_parameters[1]
    
    value_node = value+group_parameters[2]
        
    return weight_node, value_node

def build_tree(index: int, max_weight: float, weight: float, value: float, u_b: float, groups_sort: list, item_amount: int) -> tuple:
    
    res_vector = [0 for i in range(0,item_amount)]
    
    i = 0
    
    root = bt.Node(f"w={weight},v={value},u_b={u_b}")
    
    active_node = root

    while i < len(groups_sort):
        
        group = groups_sort[i]
        
        weight_left, value_left = build_vertex_including(groups_sort, group, weight, value)
        
        try:
            
            u_b_left = calculate_u_b(value_left, max_weight, weight_left, groups_sort[i+1], index)
            
        except IndexError:
            
            u_b_left = value
        
        if weight_left > max_weight:
            
            new_node_left = bt.Node(f"w={weight_left}")
            
        else:
            
            new_node_left = bt.Node(f"w={weight_left},v={value_left},u_b={u_b_left}")
            
        try:
            
            u_b_right = calculate_u_b(value, max_weight, weight, groups_sort[i+1], index)
            
        except IndexError:
            
            u_b_right = value
        

        new_node_right = bt.Node(f"w={weight},v={value},u_b={u_b_right}")
        
        active_node.left = new_node_left
        
        active_node.right = new_node_right
        
        if weight_left > max_weight or u_b_right > u_b_left:
            
            # choosing the right node, group is not added.
        
            active_node = active_node.right
            
        elif u_b_right < u_b_left or value_left > value:
            
            # choosing the left node, group is added.
            
            active_node = active_node.left
            
            weight += weight_left
            
            value += value_left
            
            for j in group[1][0]:
                
                res_vector[j.num-1] = 1
    
        i += 1
        
    return root, res_vector, weight, value
   
def solve(groups_with_u: dict, parameter: str, max_weight: float, item_amount: int) -> tuple:
    
    parms = {"u_1": 3, "u_2": 4}
    
    weight, value = 0, 0
    
    index = parms.get(parameter)
    
    groups_sort = sorted(groups_with_u.items(), key = lambda x: x[1][index], reverse = True)

    u_b = calculate_u_b(value, max_weight, weight, groups_sort[0], index)
    
    root, res_vector, weight, value = build_tree(index, max_weight, weight, value, u_b, groups_sort, item_amount)

    return root, res_vector, weight, value