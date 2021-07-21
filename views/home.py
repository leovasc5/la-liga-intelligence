import os
from pathlib import Path
from tkinter import *
from tkinter import ttk
import numpy as np
from tkinter import messagebox

p = Path(os.getcwd())

class App:
    def __init__(self, root, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv):
        logo = PhotoImage(file=str(p)+"\\assets\\img\\logo.png")
        lbl1 = Label(root, image=logo)
        lbl1.place(x=30, y=30)

        tv = ttk.Treeview(root, columns=("posicao", "time", "pontos", "partidas", "vitorias", "empates", "derrotas", "golsPro", "golsContra", "saldo", "ca", "cv"), show="headings", height=20)
        tv.column("posicao", minwidth=0, width=50)
        tv.column("time", minwidth=0, width=150)
        tv.column("pontos", minwidth=0, width=50)
        tv.column("partidas", minwidth=0, width=100)
        tv.column("vitorias", minwidth=0, width=70)
        tv.column("empates", minwidth=0, width=70)
        tv.column("derrotas", minwidth=0, width=70)
        tv.column("golsPro", minwidth=0, width=70)
        tv.column("golsContra", minwidth=0, width=70)
        tv.column("saldo", minwidth=0, width=70)    
        tv.column("ca", minwidth=0, width=70)
        tv.column("cv", minwidth=0, width=70)   
        tv.heading("posicao", text="Posição")
        tv.heading("time", text="Time")
        tv.heading("pontos", text="Pontos")
        tv.heading("partidas", text="Partidas Jogadas")
        tv.heading("vitorias", text="Vitórias")
        tv.heading("empates", text="Empates")
        tv.heading("derrotas", text="Derrotas")
        tv.heading("golsPro", text="Gols Pró")
        tv.heading("golsContra", text="Gols Sofridos")
        tv.heading("saldo", text="Saldo de Gols")
        tv.heading("ca", text="CA")
        tv.heading("cv", text="CV")
        tv.grid(column=0, row=4, columnspan=3, padx=30, pady=120)

        for i in posicao:
            tv.insert("", "end",values=(str(posicao[i-1]), nome[i-1], str(pontos[i-1]), str(partidas[i-1]), str(vitorias[i-1]), str(empates[i-1]), str(derrotas[i-1]), 
            str(gp[i-1]), str(gc[i-1]), str(saldo[i-1]), str(ca[i-1]), str(cv[i-1])))

        frameGraficos = LabelFrame(root, text="Gráficos")
        frameGraficos.place(x=30, y=575)

        lbl2 = Label(frameGraficos, text="Telefone: ", padx=10, pady=10)
        lbl2.pack(side="left")
        tlf = Entry(frameGraficos)
        tlf.pack(side="left", padx=10)

        btn1 = Button(frameGraficos, text="Gráfico da pontuação")
        btn1.place(x=400, y=400)

        root.mainloop()