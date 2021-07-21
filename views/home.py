import os, sys, inspect
from pathlib import Path
from tkinter import *
from tkinter import ttk

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from graphics.main import *
p = Path(os.getcwd())

class App:
    def __init__(self, root, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv):
        logo = PhotoImage(file=str(p)+"\\assets\\img\\logo.png")
        lbl1 = Label(root, image=logo, bg="#FFFFFF")
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

        framePontuacao = LabelFrame(root, text="Gráficos da Pontuação", padx=10, pady=10, font="Helvetica 16 bold", bg="#FFFFFF")
        framePontuacao.place(x=30, y=600, width=915)

        btn2 = Button(framePontuacao, text="Barras", command=lambda: self.call("pt_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn2.pack(side="left", padx=10, pady=10)

        btn3 = Button(framePontuacao, text="Pizza", command=lambda: self.call("pt_pi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn3.pack(side="left", padx=10, pady=10)

        btn4 = Button(framePontuacao, text="Histograma", command=lambda: self.call("pt_hi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn4.pack(side="left", padx=10, pady=10)

        btn4 = Button(framePontuacao, text="Plot", command=lambda: self.call("pt_pl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn4.pack(side="left", padx=10, pady=10)

        btn5 = Button(framePontuacao, text="ScatterPlot", command=lambda: self.call("pt_sp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn5.pack(side="left", padx=10, pady=10)
        
        # btn6 = Button(framePontuacao, text="Gols (Pizza)")
        # btn6.pack(side="left", padx=10, pady=10)

        # btn4 = Button(framePontuacao, text="Gols (Histograma)")
        # btn4.pack(side="left", padx=10, pady=10)

        root.mainloop()

    def call(self, modo, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv):
        pt_ba(nome, pontos) if modo == "pt_ba" else None
        pt_pi(nome, pontos) if modo == "pt_pi" else None
        pt_hi(pontos) if modo == "pt_hi" else None
        pt_pl(nome, pontos) if modo == "pt_pl" else None
        pt_sp(nome, pontos) if modo == "pt_sp" else None

