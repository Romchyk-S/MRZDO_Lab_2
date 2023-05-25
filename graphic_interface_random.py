# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:55:17 2023

@author: romas
"""

import customtkinter as ctk

import graphic_interface as gi

import RangeSlider.RangeSlider as rs

    
def main_work(parms: list[str]) -> dict:
    
    root = ctk.CTk()
    
    ctk.set_appearance_mode("System")

    ctk.set_default_color_theme("dark-blue")

    root.title("Введення даних для випадкової генерації")

    root.geometry('700x700')
    

    working_parms = gi.Program_parameters()
    
    var_inside_0, var_inside_1, var_inside_2, var_inside_3, var_inside_4, var_inside_5 = ctk.IntVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar(), ctk.DoubleVar()
    
    variables = [var_inside_0, var_inside_1, var_inside_2, var_inside_3, var_inside_4, var_inside_5]
    
    pack_conditions(root, variables)
    
    
    gi.submit_parms(root, working_parms, parms, variables)
    
    gi.end_window(root)
    
    root.mainloop()
    
    return working_parms.parms_dict
    
    
def pack_conditions(root: ctk.windows.ctk_tk.CTk, variables: list):
    
    def show(value):
        
        label.configure(text = f"{int(value)}")
      
    label = ctk.CTkLabel(root, text = "5")
    
    label.pack()
    
    label_1 = ctk.CTkLabel(root, text = "Оберіть кількість предметів")
    
    label_1.pack()
    
    slider_1 = ctk.CTkSlider(root, variable = variables[0], command = show, from_ = 5, to = 100)
    
    slider_1.pack()
    
    
    label_2 = ctk.CTkLabel(root, text = "Оберіть проміжок ваг предметів")
    
    label_2.pack()
    
    slider_2 = rs.RangeSliderH(root, variables = variables[1:3], padX = 20, min_val = 1, max_val = 20)
    
    slider_2.pack()
    
    
    
    label_3 = ctk.CTkLabel(root, text = "Оберіть проміжок вартостей предметів")
    
    label_3.pack()
    
    slider_3 = rs.RangeSliderH(root, variables[3:5], padX = 20, min_val = 1, max_val = 100)
    
    slider_3.pack()
    
    
    def show_1(value):
        
        label_4.configure(text = f"{value}")

    label_4 = ctk.CTkLabel(root, text = "0")
    
    label_4.pack()
    
    label_5 = ctk.CTkLabel(root, text = "Оберіть імовірність упорядкування предметів")
    
    label_5.pack()
    
    slider_4 = ctk.CTkSlider(root, variable = variables[5], command = show_1)
    
    slider_4.pack()