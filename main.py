# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import graphic_interface as gi

import graphic_interface_random as gir

import item_creation as ic

import item_groupping as ig

import solving as solve




criterions = ["u_1", "u_2"]

parms = ["max_weight", "choice"]

random_parms = ["item_amount", "lower_weight", "upper_weight", "lower_value", "upper_value", "ordering_probability"]



parms_dict = gi.main_work(parms)

print("Задано параметри")

print(parms_dict)

print()

max_weight = abs(parms_dict.get(parms[0], 7.0))

if "example.txt" in parms_dict.get(parms[1]):

    items = ic.get_items_from_file("example.txt")
    
    item_amount = len(items)
    
elif "example_1.txt" in parms_dict.get(parms[1]):

    items = ic.get_items_from_file("example_1.txt")
    
    item_amount = len(items)

else:  
    
    random_parms_dict = gir.main_work(random_parms)
    
    print("Параметри випадкової генерації предметів")
    
    print(random_parms_dict)
    
    print()
    
    item_amount = int(random_parms_dict.get(random_parms[0], 10))
    
    lower_weight, upper_weight = round(random_parms_dict.get(random_parms[1]), 2), round(random_parms_dict.get(random_parms[2]), 2)
    
    lower_value, upper_value = round(random_parms_dict.get(random_parms[3]), 2), round(random_parms_dict.get(random_parms[4]), 2)
    
    ordering_probability = random_parms_dict.get(random_parms[5])
    
    items = ic.create_items(item_amount, lower_weight, upper_weight, lower_value, upper_value, ordering_probability)


items = list(map(lambda i: i.add_link_to_item(items), items))

print("Предмети")

ig.print_items_to_table(items)



groups = ig.group_items(items)

group_table, group_table_with_weight_limits, group_table_with_u, groups_with_u, added_rows = ig.form_table(groups, max_weight)

ig.print_tables(group_table, group_table_with_weight_limits, group_table_with_u, added_rows)



total_weight, total_value = 0, 0

for item in items:
    
    total_weight += item.weight
    
    total_value += item.value
    
print()

print("Сформовано груп:")

print(len(groups_with_u))

print()

if len(groups_with_u) == 0:
    
    print("Рюкзак заповнити неможливо.")
    
elif total_weight <= max_weight:
    
    print("Вага рюкзака >= вазі всіх предметів.")
    
    res_vector = [1 for i in range(0, item_amount)]
    
    print(f"Результат: {res_vector}")
    
    print(f"W = {round(total_weight, 2)}")
    
    print(f"V = {round(total_value, 2)}")
    
    print()
    
else:
    
    for c in criterions:
        
        print(f"Розв'язок для критерію {c}")
        
        root, res_vector, weight, value = solve.solve(groups_with_u, c, max_weight, item_amount)

        with open(f"{c}.txt", "w", encoding = "UTF-8") as f:
            
            f.write("Бінарне дерево:")
            
            f.write(f"{root}")

        print(f"Результат: {res_vector}")
        
        print(f"W = {round(weight, 2)}")
        
        print(f"V = {round(value, 2)}")
        
        print()