from tkinter import *
from tkinter import ttk


root = Tk()
tree = ttk.Treeview(root, columns=("size", "modified"))
tree["columns"] = ("date", "time", "loc")

def selectItem(a):
    curItem = tree.focus()
    b = tree.item(curItem)
    b = list(b.values())
    nome = b[2][0]
    pontos = b[2][1]
    posicao = b[2][2]
    vequipe.set(nome)
    vpontos.set(str(pontos))

tree.column("date", width=65)
tree.column("time", width=40)
tree.column("loc", width=100)

tree.heading("date", text="Time")
tree.heading("time", text="Pontos")
tree.heading("loc", text="Posicao")
tree.bind('<ButtonRelease-1>', selectItem)

nome = ["Atletico de Madrid", "Real Madrid", "Barcelona"]

vequipe = StringVar()
select = ttk.Combobox(root, values=nome, textvariable=vequipe)
select.set("Equipe")
select.place(x=10, y=150)

vpontos = StringVar()
en1 = Entry(root, width=10, textvariable=vpontos)
en1.place(x=10, y=185)

tree.insert("","end",text = "Name",values = ("Atletico de Madrid",86,1))
tree.insert("","end",text = "Name",values = ("Real Madrid",84,2))
tree.insert("","end",text = "Name",values = ("Barcelona",87,3))

tree.grid()
root.mainloop()

import tkinter as tk


class TkinterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.configure(background='orange')

        self.text = tk.StringVar()
        self.text.set('Hello')

        display_frame = tk.Frame(self, background='cyan')
        ButtonsFrame = tk.Frame(self, background='green')
        display_frame.rowconfigure(0, weight=1)
        display_frame.columnconfigure(0, weight=1)
        ButtonsFrame.rowconfigure(0, weight=1)
        ButtonsFrame.columnconfigure(0, weight=1)
        ButtonsFrame.columnconfigure(1, weight=1)

        display_frame.grid(row=0, column=0, pady=5, padx=5, sticky='nsew')
        ButtonsFrame.grid(row=1, column=0, pady=5, padx=5, sticky='nsew')

        tk.Label(display_frame, textvariable=self.text, font=15,
                 bg="#bebebe", relief="groove", bd=5).grid(row=0, column=0, sticky='nsew')

        tk.Button(ButtonsFrame, text='A',
                  command=lambda: self.update_text('A')).grid(row=0, column=0, padx=15, sticky='nsew')
        tk.Button(ButtonsFrame, text='B',
                  command=lambda: self.update_text('B')).grid(row=0, column=1, padx=15, sticky='nsew')

    def update_text(self, value):
        self.text.set(value)

TkinterWindow().mainloop()