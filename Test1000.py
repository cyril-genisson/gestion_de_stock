# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON
@file: $(filename)

@project: Colibri
@licence: GPLv3
"""
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from gestion import *


class AddCategory(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Add Category")
        self.label.pack(padx=20, pady=20)


class AddProduct(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.label = ctk.CTkLabel(self, text="Add Product")
        self.label.pack(padx=20, pady=20)


class ModProduct(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.label = ctk.CTkLabel(self, text="Update Product")
        self.label.pack(padx=20, pady=20)


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gestion = Gestion()
        self.geometry("1024x768")
        self.title("Inventory Management")

        self.frame_command = ctk.CTkFrame(self)
        self.frame_command.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_command = ctk.CTkLabel(self.frame_command, text="Operations")
        self.label_command.pack(side="top", padx=10, pady=10)
        self.button_category_add = ctk.CTkButton(self.frame_command, text="Add Category", command=self.add_category)
        self.button_category_add.pack(side="top", padx=20, pady=5)

        self.button_category_add = ctk.CTkButton(self.frame_command, text="Update Category",
                                                 command=self.update_category)
        self.button_category_add.pack(side="top", padx=20, pady=5)

        self.button_category_add = ctk.CTkButton(self.frame_command, text="Delete Category", command=self.add_category)
        self.button_category_add.pack(side="top", padx=20, pady=5)

        self.button_product_add = ctk.CTkButton(self.frame_command, text="Add Product", command=self.add_product)
        self.button_product_add.pack(side="top", padx=20, pady=5)

        self.button_product_add = ctk.CTkButton(self.frame_command, text="Update Product", command=self.update_product)
        self.button_product_add.pack(side="top", padx=20, pady=5)

        self.button_category_add = ctk.CTkButton(self.frame_command, text="Delete Product", command=self.add_category)
        self.button_category_add.pack(side="top", padx=20, pady=5)

        self.frame_products = ctk.CTkFrame(self, width=800, height=800)
        self.frame_products.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.label_products = ctk.CTkLabel(self.frame_products, text="Products")
        self.label_products.pack(side="top", padx=10, pady=10, fill="both")

        self.treeview_scrollbar_y = ctk.CTkScrollbar(self.frame_products, width=15)
        self.treeview_scrollbar_y.pack(side='right', fill='y')

        self.treeview = ttk.Treeview(self.frame_products, yscrollcommand=self.treeview_scrollbar_y)
        self.treeview['columns'] = ('Id', 'Name', 'Category', 'Price', 'Quantity', 'Description')
        self.treeview.column("#0", width=0, stretch=tk.NO)
        self.treeview.column("Id", anchor=tk.CENTER, width=80)
        self.treeview.column("Name", anchor=tk.W, width=200)
        self.treeview.column('Category', anchor=tk.W, width=200)
        self.treeview.column('Price', anchor=tk.CENTER, width=200)
        self.treeview.column('Quantity', anchor=tk.CENTER, width=200)
        self.treeview.column('Description', anchor=tk.W, width=200)

        self.treeview.heading("#0", text="Label", anchor=tk.W)
        self.treeview.heading("Id", text="ID", anchor=tk.CENTER)
        self.treeview.heading("Name", text="Name", anchor=tk.CENTER)
        self.treeview.heading("Category", text="Category", anchor=tk.CENTER)
        self.treeview.heading("Price", text="Price", anchor=tk.CENTER)
        self.treeview.heading("Quantity", text="Quantity", anchor=tk.CENTER)
        self.treeview.heading("Description", text="Description", anchor=tk.W)
        self.treeview.pack(side="top", padx=10, pady=10)
        self.refresh_view()

        self.toplevel_window = None

    def refresh_view(self):
        cpt = 0
        if self.treeview.get_children() is not None:
            for item in self.treeview.get_children():
                self.treeview.delete(item)
        for row in self.gestion.see_product():
            self.treeview.insert(parent='', index=cpt, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
            cpt += 1

    def add_category(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AddCategory(self)
        else:
            self.toplevel_window.focus()

    def update_category(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ModProduct(self)
        else:
            self.toplevel_window.focus()

    def add_product(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AddProduct(self)
        else:
            self.toplevel_window.focus()

    def update_product(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ModProduct(self)
        else:
            self.toplevel_window.focus()


if __name__ == "__main__":
    app = App()
    app.mainloop()
