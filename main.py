# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import working_functions as wf

import graphic_interface as gi

import graphic_interface_random as gir


file_name = "example.txt"

criterions = ["u_1", "u_2"]

parms = ["max_weight", "choice"]

random_parms = ["item_amount", "lower_weight", "upper_weight", "lower_value", "upper_value", "ordering_probability"]




parms_dict = gi.main_work(parms)

print("Задано параметри")

print(parms_dict)

print()

max_weight = abs(parms_dict.get(parms[0], 7.0))

if ".txt" in parms_dict.get(parms[1]):

    items = wf.get_items_from_file(file_name)
    
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
    
    items = wf.create_items(item_amount, lower_weight, upper_weight, lower_value, upper_value, ordering_probability)


items = list(map(lambda i: i.add_link_to_item(items), items))

print("Предмети")

wf.print_items_to_table(items)



groups = wf.group_items(items)

group_table, group_table_with_weight_limits, group_table_with_u, groups_with_u = wf.form_table(groups, max_weight)

wf.print_tables(group_table, group_table_with_weight_limits, group_table_with_u)


print()

if len(groups_with_u) == 0:
    
    print("Рюкзак заповнити неможливо")
    
else:
    
    for c in criterions:
        
        print(f"Розв'язок для критерію {c}")
        
        root, res_vector, weight, value = wf.solve(groups_with_u, c, max_weight, item_amount)

        with open(f"{c}.txt", "w", encoding = "UTF-8") as f:
            
            f.write("Бінарне дерево:")
            
            f.write(f"{root}")

        print(f"Результат: {res_vector}")
        
        print(f"W = {round(weight, 2)}")
        
        print(f"V = {round(value, 2)}")
        
        print()