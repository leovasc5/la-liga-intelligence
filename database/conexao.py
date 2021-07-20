import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import os

caminho = str(os.path.dirname(__file__)) + "\\appDB.db"
print(caminho)

def ConexaoBanco():
    con = None
    try:
        con = sqlite3.connect(caminho)
    except Error:
        print(Error)
    return con

def dql(query): #select
    con = ConexaoBanco()
    c = con.cursor()
    c.execute(query)
    res = c.fetchall()
    con.close()
    return res

def dml(query): #insert, update, delete
    try:
        con = ConexaoBanco()
        c = con.cursor()
        c.execute(query)
        con.commit()
        con.close()
    except Error:
        messagebox.showerror(title="Erro", message="Erro - Reporte ao desenvolvedor")