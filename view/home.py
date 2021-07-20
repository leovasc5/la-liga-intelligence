import os
from pathlib import Path
from tkinter import *
from tkinter import ttk
import numpy as np

p = Path(os.getcwd())

class App:
    def __init__(self, root, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo):
        logo = PhotoImage(file=str(p)+"\\assets\\img\\logo.png")
        lbl1 = Label(root, image=logo)
        lbl1.place(x=30, y=30)

        tv = ttk.Treeview(root, columns=("posicao", "time", "pontos", "partidas", "vitorias", "empates", "derrotas", "golsPro", "golsContra", "saldo"), show="headings", height=20)

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

        tv.grid(column=0, row=4, columnspan=3, padx=30, pady=120)

        c = np.arange(0, 20, 1)
        for i in c:
            tv.insert("", "end",values=(str(posicao[i]), nome[i], str(pontos[i]), str(partidas[i]), str(vitorias[i]), str(empates[i]), str(derrotas[i]), str(gp[i]), str(gc[i]), str(saldo[i])))

        root.mainloop()

    # def reiniciar(self):
    #     lbl2 = Label(self.root, text="TESTE")
    #     lbl2.pack()