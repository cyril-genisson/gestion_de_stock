#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: gestion.py
@created: 01/02/2024

@project: 
@licence: GPLv3
"""
import pandas as pd
from db import *

class Gestion(Db):
    def __init__(self):
        super().__init__()

    def add_t(self, table, **kwargs):
        match table:
            case "product":
                if "name" not in kwargs:
                    print("Le nom du produit est requis")
                    return 1
            case "category":
                if "name" not in kwargs:
                    print("Le nom de la catégorie est requis")
                    return 1
            case _:
                print("Table inexistante")
                return 1

        arg_k, arg_v = "", ""
        for key, value in kwargs.items():
            arg_k += f"{key},"
            arg_v += f"\'{value}\',"
        arg_k = arg_k[:-1]
        arg_v = arg_v[:-1]
        req = f"INSERT INTO {table}({arg_k}) VALUES ({arg_v})"
        res = self.query(req, modif=True)

    def update_t(self, table, **kwargs):
        argv = ""
        for key, value in kwargs.items():
            argv += f"{key}=\'{value}\', "
        argv = argv[:-2]
        req = f"UPDATE {table} SET {argv} WHERE id = {id_t}"
        res = self.query(req, modif=True)
        print(res)

    def remove(self, table, id_t):
        if isinstance(id_t, int):
            req = f"DELETE FROM {table} WHERE id = {id_t}"
            res = self.query(req, modif=True)
            print(res)
    
    def see_category(self):
        req = f"SELECT * FROM category"
        res = self.query(req)
        print(res)
        return res

    def see_product(self, id_cat=None):
        if id_cat:
            req = f"SELECT product.name, description, price, quantity, category.name FROM product JOIN category WHERE product.id_category = category.id AND product.id_category = {id_cat}"
            res = self.query(req)
        else:
            req = f"SELECT product.name, description, price, quantity, category.name FROM product JOIN category WHERE product.id_category = category.id"
            res = self.query(req)
        print(res)
        return res

    def save_csv(self, id_cat=None, filename='save.csv'):
        data = self.see_product(id_cat)
        df = pd.DataFrame(data, columns=['Name', 'Description', 'Price', 'Quantity', 'Category'])
        csv_filename = filename
        df.to_csv(csv_filename, index=False)


if __name__ == "__main__":
    pass

