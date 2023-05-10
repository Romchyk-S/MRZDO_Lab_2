# -*- coding: utf-8 -*-
"""
Created on Wed May 10 11:15:30 2023

@author: romas
"""

import customtkinter as ctk

import dataclasses as dc

@dc.dataclass()
class Program_parameters:
    
    parms_dict: dict

    @property
    def parms_dict(self) -> dict:
        
        return self._parms_dict
    
    @parms_dict.setter
    def parms_dict(self, dictionary: dict) -> None:
        
        self._parms_dict = dictionary

def main_work(parms: list[str]) -> dict:
    
    root = ctk.CTk()
    
    ctk.set_appearance_mode("System")

    ctk.set_default_color_theme("dark-blue")

    root.title("Введення даних")

    root.geometry('700x700')
    
    
    
    working_parms = Program_parameters()
    
    var_inside_1 = ctk.DoubleVar(value = 1.0)
    
    var_inside_2 = ctk.StringVar()
    
    variables = [var_inside_1, var_inside_2]
    
    
    
    pack_main_parms(root, variables[0:2])
    
    submit_parms(root, working_parms, parms, variables)
    
    end_window(root)
    
    root.mainloop()
    
    return working_parms.parms_dict

def pack_main_parms(root: ctk.windows.ctk_tk.CTk, variables: list):
    
    label_1 = ctk.CTkLabel(root, text = "Введіть максимальну вагу рюкзака")
    
    label_1.pack()

    
    textbox_1 = ctk.CTkEntry(root, textvariable = variables[0])
    
    textbox_1.pack()
    
    
    label_2 = ctk.CTkLabel(root, text = "Оберіть метод отримання предметів")
    
    label_2.pack()
    
    textbox_2 = ctk.CTkOptionMenu(root, variable = variables[1], values = ["З файлу example.txt", "Випадковим чином"])
    
    textbox_2.pack()


def submit_parms(root: ctk.windows.ctk_tk.CTk, working_parms: Program_parameters, parms: list, variables: list):
    
    def button(working_parms: Program_parameters) -> None:

        working_parms.parms_dict = {p:v.get() for p, v in zip(parms, variables)}
    
    submit_button = ctk.CTkButton(root, text = 'Записати параметри', command = lambda: button(working_parms))
    
    submit_button.pack()
    
def end_window(root: ctk.windows.ctk_tk.CTk) -> None:
    
    start_label = ctk.CTkLabel(root, text="Завершуємо роботу з вікном?")
    start_label.pack()

    def button():

        root.destroy()

    submit_button = ctk.CTkButton(root, text = 'Так', command = lambda: button())
    submit_button.pack()