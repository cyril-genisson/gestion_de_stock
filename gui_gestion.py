#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: gui_gestion.py
@created: 01/02/2024

@project: 
@licence: GPLv3
"""
from gestion import Gestion
import customtkinter as ctk


class GuiGestion(Gestion):
    def __init__(self, root):
        super().__init__(root)
        root.title("Gestion de stock")
        main_frame = ttk.Frame(root, padding="3 3 12 12")
        main_frame.grid(column=0, row=0, sticky="")
        root.geometry("800x600")
        root.resizable()
        self.root.protocol("WM_DELETE_WINDOW", self)

    def start(self):
        self.root.mainloop()




if __name__ == '__main__':
    pass
