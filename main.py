# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import working_functions as wf


file_name = "example.txt"

lower_weight = 1.0

upper_weight = 10.0

lower_value = 1.0

upper_value = 10.0

ordering_probability = 0.2

criterions = ["u_1", "u_2"]


max_weight = wf.get_weight_input()

choice = wf.get_option()



items, item_amount = wf.get_items(choice, file_name, lower_weight, upper_weight, lower_value, upper_value, ordering_probability)

while item_amount > 100:
    
    print("Зменшіть кільксть предметів")
    
    items, item_amount = wf.get_items(choice, file_name, lower_weight, upper_weight, lower_value, upper_value, ordering_probability)
    

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

        with open(f"{c}.txt", "w") as f:
            
            f.write("Бінарне дерево:")
            
            f.write(f"{root}")

        print(f"Результат: {res_vector}")
        
        print(f"W = {weight}")
        
        print(f"V = {value}")
        
        print()