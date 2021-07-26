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
        framePontuacao.place(x=30, y=575, width=915)

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

        btn6 = Button(framePontuacao, text="Pontuação-Gols Pró", command=lambda: self.call("pt_gp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn6.pack(side="left", padx=10, pady=10)

        btn6 = Button(framePontuacao, text="Relação Pontuação-Gols Contra", command=lambda: self.call("pt_gc", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn6.pack(side="left", padx=10, pady=10)
        
        btn7 = Button(framePontuacao, text="Relação Pontuação-Saldo", command=lambda: self.call("pt_sl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn7.pack(side="left", padx=10, pady=10)

        frameGols = LabelFrame(root, text="Gráficos dos Gols", padx=10, pady=10, font="Helvetica 16 bold", bg="#FFFFFF")
        frameGols.place(x=30, y=700, width=915, height=150)

        btn7 = Button(frameGols, text="Relação de Gols", command=lambda: self.call("gp_gc", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn7.place(x=10, y=10)

        btn8 = Button(frameGols, text="Barras (Gols Pró)", command=lambda: self.call("gp_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn8.place(x=120, y=10)

        btn9 = Button(frameGols, text="Barras (Gols Sofridos)", command=lambda: self.call("gs_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn9.place(x=230, y=10)

        btn10 = Button(frameGols, text="Pizza (Gols Pró)", command=lambda: self.call("gp_pi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn10.place(x=365, y=10)

        btn11 = Button(frameGols, text="Pizza (Gols Sofridos)", command=lambda: self.call("gs_pi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn11.place(x=470, y=10)

        btn12 = Button(frameGols, text="Histograma (Gols Pró)", command=lambda: self.call("gp_hi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn12.place(x=600, y=10)

        btn13 = Button(frameGols, text="Histograma (Gols Sofridos)", command=lambda: self.call("gc_hi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn13.place(x=10, y=50)

        btn14 = Button(frameGols, text="Plot (Gols Pró)", command=lambda: self.call("gp_pl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn14.place(x=750, y=10)

        btn15 = Button(frameGols, text="Plot (Gols Sofridos)", command=lambda: self.call("gc_pl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn15.place(x=180, y=50)

        btn16 = Button(frameGols, text="ScatterPlot (Gols Pró)", command=lambda: self.call("gp_sp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn16.place(x=300, y=50)

        btn17 = Button(frameGols, text="ScatterPlot (Gols Sofridos)", command=lambda: self.call("gc_sp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn17.place(x=430, y=50)

        btn18 = Button(frameGols, text="Relação Gols Pró - Gols Sofridos (Gols Sofridos)", command=lambda: self.call("r_gpc", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn18.place(x=595, y=50)

        frameResultados = LabelFrame(root, text="Gráficos das Vitórias, Empates e Derrotas", padx=10, pady=10, font="Helvetica 16 bold", bg="#FFFFFF")
        frameResultados.place(x=30, y=875, width=915, height=150)

        btn19 = Button(frameResultados, text="Relação de Resultados", command=lambda: self.call("re_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn19.place(x=10, y=10)

        btn20 = Button(frameResultados, text="Barras (Vitórias)", command=lambda: self.call("vi_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn20.place(x=143, y=10)

        btn21 = Button(frameResultados, text="Barras (Derrotas)", command=lambda: self.call("de_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn21.place(x=241, y=10)

        btn22 = Button(frameResultados, text="Barras (Empates)", command=lambda: self.call("em_ba", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn22.place(x=344, y=10)

        btn23 = Button(frameResultados, text="Pizza (Vitórias)", command=lambda: self.call("vi_pi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn23.place(x=447, y=10)

        btn24 = Button(frameResultados, text="Pizza (Derrotas)", command=lambda: self.call("de_pi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn24.place(x=535, y=10)

        btn25 = Button(frameResultados, text="Pizza (Empates)", command=lambda: self.call("em_pi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn25.place(x=630, y=10)

        btn26 = Button(frameResultados, text="Plot (Vitórias)", command=lambda: self.call("vi_pl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn26.place(x=725, y=10)

        btn27 = Button(frameResultados, text="Plot (Derrotas)", command=lambda: self.call("de_pl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn27.place(x=810, y=10)

        btn28 = Button(frameResultados, text="Plot (Empates)", command=lambda: self.call("em_pl", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn28.place(x=10, y=50)

        btn29 = Button(frameResultados, text="Histograma (Vitórias)", command=lambda: self.call("vi_hi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn29.place(x=110, y=50)

        btn30 = Button(frameResultados, text="Histograma (Derrotas)", command=lambda: self.call("de_hi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn30.place(x=240, y=50)

        btn31 = Button(frameResultados, text="Histograma (Empates)", command=lambda: self.call("em_hi", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn31.place(x=375, y=50)

        btn32 = Button(frameResultados, text="ScatterPlot (Vitórias)", command=lambda: self.call("vi_sp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn32.place(x=510, y=50)

        btn33 = Button(frameResultados, text="ScatterPlot (Derrotas)", command=lambda: self.call("de_sp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn33.place(x=640, y=50)

        btn34 = Button(frameResultados, text="ScatterPlot (Empates)", command=lambda: self.call("em_sp", 
        posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv))
        btn34.place(x=772, y=50)

        root.mainloop()

    def call(self, modo, posicao, nome, pontos, partidas, vitorias, empates, derrotas, gp, gc, saldo, ca, cv):
        pt_ba(nome, pontos) if modo == "pt_ba" else None
        pt_pi(nome, pontos) if modo == "pt_pi" else None
        pt_hi(pontos) if modo == "pt_hi" else None
        pt_pl(nome, pontos) if modo == "pt_pl" else None
        pt_sp(nome, pontos) if modo == "pt_sp" else None
        pt_gp(pontos, gp) if modo == "pt_gp" else None
        pt_gc(pontos, gc) if modo == "pt_gc" else None
        pt_sl(pontos, saldo) if modo == "pt_sl" else None
        gp_gc(gp, gc, nome) if modo == "gp_gc" else None 
        gp_ba(nome, gp) if modo == "gp_ba" else None
        gs_ba(nome, gc) if modo == "gs_ba" else None
        gp_pi(nome, gp) if modo == "gp_pi" else None
        gs_pi(nome, gc) if modo == "gs_pi" else None
        gp_hi(gp) if modo == "gp_hi" else None
        gc_hi(gc) if modo == "gc_hi" else None 
        gp_pl(nome, gp) if modo == "gp_pl" else None
        gc_pl(nome, gc) if modo == "gc_pl" else None
        gp_sp(nome, gp) if modo == "gp_sp" else None
        gc_sp(nome, gc) if modo == "gc_sp" else None
        r_gpc(nome, gp, gc) if modo == "r_gpc" else None
        re_ba(nome, vitorias, empates, derrotas) if modo == "re_ba" else None
        vi_ba(nome, vitorias) if modo == "vi_ba" else None
        de_ba(nome, derrotas) if modo == "de_ba" else None
        em_ba(nome, empates) if modo == "em_ba" else None
        vi_pi(nome, vitorias) if modo == "vi_pi" else None
        de_pi(nome, derrotas) if modo == "de_pi" else None
        em_pi(nome, empates) if modo == "em_pi" else None
        vi_pl(nome, vitorias) if modo == "vi_pl" else None
        de_pl(nome, derrotas) if modo == "de_pl" else None
        em_pl(nome, empates) if modo == "em_pl" else None
        vi_hi(vitorias) if modo == "vi_hi" else None
        de_hi(derrotas) if modo == "de_hi" else None
        em_hi(empates) if modo == "em_hi" else None
        vi_sp(nome, vitorias) if modo == "vi_sp" else None
        de_sp(nome, derrotas) if modo == "de_sp" else None
        em_sp(nome, empates) if modo == "em_sp" else None



#Relação Vitorias - ca - cv