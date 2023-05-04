# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import working_functions as wf
    

file_name = "example.txt"


max_weight = wf.get_weight_input()

items = wf.get_items(file_name)

item_amount = len(items)

items = list(map(lambda i: i.add_link_to_item(items), items))

groups = wf.group_items(items)

print(groups)