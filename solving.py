# -*- coding: utf-8 -*-
"""
Created on Thu May  4 14:55:59 2023

@author: romas
"""

import binarytree as bt


def calculate_u_b(value: float, max_weight: float, weight: float, group_next: list, index: int) -> float:
    
    
    try:
        
        u_next = group_next[1][index]
        
        return value + (max_weight-weight)*u_next
        
    except TypeError:

        return value

def build_vertex_including(groups_sort: list, group: list, weight: float, value: float) -> tuple[float]:
    
    group_parameters = group[1]
    
    weight_node = weight+group_parameters[1]
    
    value_node = value+group_parameters[2]
        
    return weight_node, value_node

def move_up_level(root_node: bt.Node, active_node: bt.Node) -> int:
     
    k = 0
    
    while k < len(root_node.levels):
        

        
        for node_temp in root_node.levels[k]:
            
            if node_temp == active_node:
                
                return k-1

        k += 1
            
    

def build_tree(index: int, max_weight: float, u_b: float, groups_sort: list, item_amount: int) -> tuple:
    
    i = 0
    
    root = bt.Node(f"group={groups_sort[i][0]}, w={0},v={0},u_b={u_b}")
    
    nodes_hanging = []
    
    active_node = root
            
    res_vector = [0 for i in range(0, item_amount)]

    while i < len(groups_sort):
   
        group = groups_sort[i]
        
        try:
        
            next_group = groups_sort[i+1]
            
        except IndexError:
        
            next_group = [None]
        
        node_values = active_node.value.split(",")
        
        active_weight = float(node_values[1].split("=")[1])
        
        active_value = float(node_values[2].split("=")[1])
        
        
        weight_left, value_left = build_vertex_including(groups_sort, group, active_weight, active_value)
        
        try:
            
            u_b_left = calculate_u_b(value_left, max_weight, weight_left, groups_sort[i+1], index)
            
        except IndexError:
            
            u_b_left = calculate_u_b(value_left, max_weight, weight_left, 0, index)
        
        if weight_left > max_weight:
            
            new_node_left = bt.Node(f"group={next_group[0]},w={weight_left}")
            
        else:
            
            res_vector_temp = res_vector.copy()
        
            for item in group[1][0]:

                res_vector_temp[int(item.num)-1] = 1
                
            res_vector_temp = ' '.join(map(str, res_vector_temp))
            
            
            new_node_left = bt.Node(f"group={next_group[0]},w={weight_left},v={value_left},u_b={u_b_left},res={str(res_vector_temp)}")
            
        try:
            
            u_b_right = calculate_u_b(active_value, max_weight, active_weight, groups_sort[i+1], index)
            
        except IndexError:
            
            u_b_right = active_value
            
        res_vector = ' '.join(map(str, res_vector))
        
        new_node_right = bt.Node(f"group={next_group[0]},w={active_weight},v={active_value},u_b={u_b_right},res={res_vector}")
        
        active_node.left = new_node_left
        
        active_node.right = new_node_right
        
        nodes_hanging = [node for node in root.leaves if len(node.value.split(",")) > 2]
        
        nodes_hanging_dict = {node:float(node.value.split("=")[4].split(",")[0]) for node in nodes_hanging}
        
        nodes_hanging_dict_sorted = sorted(nodes_hanging_dict.items(), key = lambda x: x[1], reverse = True)
        
        active_node = nodes_hanging_dict_sorted[0][0]
        
        node_values = active_node.value.split(",")
        
        
        group_active = node_values[0].split("=")[1]
        
        if TypeError or int(group_active) != int(next_group[0]):
 
            i = move_up_level(root, active_node)
                
        res_vector = list(node_values[4].split("=")[1])
        
        j = 0
        
        while j < len(res_vector):
            
            try:
            
                res_vector[j] = int(res_vector[j])
            
                j += 1
                
            except ValueError:
                
                res_vector.pop(j)
    
        active_weight = float(node_values[1].split("=")[1])
        
        active_value = float(node_values[2].split("=")[1])
        
        i += 1
        
    return root, res_vector, active_weight, active_value
   
def solve(groups_with_u: dict, parameter: str, max_weight: float, item_amount: int) -> tuple:
    
    parms = {"u_1": 3, "u_2": 4}
    
    index = parms.get(parameter)
    
    groups_sort = sorted(groups_with_u.items(), key = lambda x: x[1][index], reverse = True)

    u_b = calculate_u_b(0, max_weight, 0, groups_sort[0], index)
    
    root, res_vector, weight, value = build_tree(index, max_weight, u_b, groups_sort, item_amount)

    return root, res_vector, weight, value