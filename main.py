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

group_table, group_table_with_weight_limits, group_table_with_u = wf.form_table(groups, max_weight)

print("Таблиця груп")

print(group_table)

print()

print("Таблиця груп без надто важких")

print(group_table_with_weight_limits)

print()

print("Таблиця груп із відносною цінністю")

print(group_table_with_u)

print()

print("Таблиця груп, сортована за u_1")

print(group_table_with_u.get_string(sortby="u_1", reversesort=True))

# get column order, create a dictionary group_no: [weight, value, u_1], build binary tree.

print()

print("Таблиця груп, сортована за u_2")

print(group_table_with_u.get_string(sortby="u_2", reversesort=True))

# get column order, create a dictionary group_no: [weight, value, u_2], build binary tree.