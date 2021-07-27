from tkinter.constants import CENTER, RIGHT
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import os, sys, inspect
from pathlib import Path
import seaborn as sns

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

p = Path(os.getcwd())
icon = str(p)+"\\assets\\img\\icon.ico"

def pt_ba(nome, pontos):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Barras)")
    plt.bar(nome, pontos, label='Pontos', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def pt_pi(nome, pontos):
    plt.close()
    plt.pie(pontos, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def pt_hi(pontos):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(pontos) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Pontuação')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def pt_pl(nome, pontos):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.plot(nome, pontos)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def pt_sp(nome, pontos):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, pontos, label='Pontos', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def pt_gp(pontos, gp):
    plt.close()
    sns.set_style("whitegrid")
    blue, = sns.color_palette("muted", 1)
    fig, ax = plt.subplots()
    ax.plot(pontos, gp, color=blue, lw=2)
    ax.fill_between(pontos, 0, gp, alpha=.3)
    ax.set(xlim=(min(pontos), max(pontos)), ylim=(0, 100), xticks=pontos)
    plt.xlabel("Pontos")
    plt.ylabel("Saldo")
    plt.title("Area Chart")
    plt.legend()

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def pt_gc(pontos, gc):
    plt.close()
    sns.set_style("whitegrid")
    blue, = sns.color_palette("muted", 1)
    fig, ax = plt.subplots()
    ax.plot(pontos, gc, color=blue, lw=2)
    ax.fill_between(pontos, 0, gc, alpha=.3)
    ax.set(xlim=(min(pontos), max(pontos)), ylim=(0, 100), xticks=pontos)
    plt.xlabel("Pontos")
    plt.ylabel("Saldo")
    plt.title("Area Chart")
    plt.legend()

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def pt_sl(pontos, saldo):
    plt.close()
    sns.set_style("whitegrid")
    blue, = sns.color_palette("muted", 1)
    fig, ax = plt.subplots()
    ax.plot(pontos, saldo, color=blue, lw=2)
    ax.fill_between(pontos, 0, saldo, alpha=.3)
    ax.set(xlim=(min(pontos), max(pontos)), ylim=(-50, 60), xticks=pontos)
    plt.xlabel("Pontos")
    plt.ylabel("Saldo")
    plt.title("Area Chart")
    plt.legend()

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()
    
def gp_gc(gp, gc, nome):
    plt.close()
    y_pos=np.arange(len(nome))
    plt.bar(y_pos + 0, gp, width=0.2, color='limegreen', label='Gols Pró')
    plt.bar(y_pos + 0.2, gc, width=0.2, color='red', label='Gols Sofridos')

    plt.xticks(np.arange(0,20), nome, rotation="vertical")
    plt.legend(("Gols Pró", "Gols Sofridos"))
    plt.ylabel("Gols")
    plt.xlabel("Times")
    plt.title("Relação: Gols Pró - Gols Sofridos")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gp_gc(gp, gc, nome):
    plt.close()
    y_pos=np.arange(len(nome))
    plt.bar(y_pos + 0, gp, width=0.2, color='limegreen', label='Gols Pró')
    plt.bar(y_pos + 0.2, gc, width=0.2, color='red', label='Gols Sofridos')

    plt.xticks(np.arange(0,20), nome, rotation="vertical")
    plt.legend(("Gols Pró", "Gols Sofridos"))
    plt.ylabel("Gols")
    plt.xlabel("Times")
    plt.title("Relação: Gols Pró - Gols Sofridos")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gp_ba(nome, gp):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Barras)")
    plt.bar(nome, gp, label='Pontos', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def gs_ba(nome, gc):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Barras)")
    plt.bar(nome, gc, label='Pontos', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def gp_pi(nome, gp):
    plt.close()
    plt.pie(gp, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def gs_pi(nome, gc):
    plt.close()
    plt.pie(gc, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def gp_hi(gp):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(gp) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Gols')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gc_hi(gc):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(gc) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Gols')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gp_pl(nome, gp):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, gp)
    plt.ylabel('Gols')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Gols Pró (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gc_pl(nome, gc):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, gc)
    plt.ylabel('Gols')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Gols Sofridos (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gp_sp(nome, gp):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, gp, label='Gols', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Gols (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def gc_sp(nome, gc):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, gc, label='Gols', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Gols Sofridos (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def r_gpc(nome, gp, gc):
    plt.close()
    plt.subplots_adjust(bottom=0.18, top=0.88)
    tickvalues = range(0,len(nome))
    plt.xticks(ticks=tickvalues, labels=nome, rotation='vertical')
    plt.plot(gp)
    plt.plot(gc)
    plt.ylabel('Gols')
    plt.legend(("Gols Pró", "Gols Sofridos"))

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def re_ba(nome, vitorias, empates, derrotas):
    plt.close()
    y_pos=np.arange(len(nome))
    plt.bar(y_pos + 0, vitorias, width=0.2, color='limegreen', label='Gols Pró')
    plt.bar(y_pos + 0.2, derrotas, width=0.2, color='red', label='Gols Sofridos')
    plt.bar(y_pos + 0.4, empates, width=0.2, color='grey', label='Gols Sofridos')

    plt.xticks(np.arange(0,20), nome, rotation="vertical")
    plt.legend(("Vitórias", "Derrotas", "Empates"))
    plt.title("Relação de Resultados")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def vi_ba(nome, vitorias):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Barras)")
    plt.bar(nome, vitorias, label='Vitórias', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def de_ba(nome, derrotas):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Derrotas (Barras)")
    plt.bar(nome, derrotas, label='Vitórias', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def em_ba(nome, empates):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Empates (Barras)")
    plt.bar(nome, empates, label='Empates', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def vi_pi(nome, vitorias):
    plt.close()
    plt.pie(vitorias, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def de_pi(nome, derrotas):
    plt.close()
    plt.pie(derrotas, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def em_pi(nome, empates):
    plt.close()
    plt.pie(empates, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def vi_pl(nome, vitorias):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, vitorias)
    plt.ylabel('Vitórias')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def de_pl(nome, derrotas):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, derrotas)
    plt.ylabel('Vitórias')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def em_pl(nome, empates):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, empates)
    plt.ylabel('Vitórias')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Vitórias (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def vi_hi(vitorias):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(vitorias) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Vitórias')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def de_hi(derrotas):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(derrotas) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Derrotas')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def em_hi(empates):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(empates) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Empates')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def vi_sp(nome, vitorias):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, vitorias, label='Vitórias', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Vitórias (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def de_sp(nome, derrotas):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, derrotas, label='Derrotas', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Derrotas (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def em_sp(nome, empates):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, empates, label='Empates', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Empates (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def ca_cv(nome, ca, cv):
    plt.close()
    y_pos=np.arange(len(nome))
    plt.bar(y_pos + 0, ca, width=0.2, color='yellow', label='Cartões Amarelos')
    plt.bar(y_pos + 0.2, cv, width=0.2, color='red', label='Cartões Vermelhos')

    plt.xticks(np.arange(0,20), nome, rotation="vertical")
    plt.legend(("Cartões Amarelos","Cartões Vermelhos"))
    plt.ylabel("Cartões Amarelos")
    plt.xlabel("Cartões Vermelhos")
    plt.title("Relação: Cartões Amarelos - Cartões Vermelhos")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def ca_ba(nome, ca):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Cartões Amarelos (Barras)")
    plt.bar(nome, ca, label='Cartões Amarelos', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def cv_ba(nome, cv):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Cartões Vermelhos (Barras)")
    plt.bar(nome, cv, label='Cartões Vermelhos', width=0.5, align=CENTER)
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend()
    plt.show()

def ca_pi(nome, ca):
    plt.close()
    plt.pie(ca, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico de Cartões Amarelos (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def cv_pi(nome, cv):
    plt.close()
    plt.pie(cv, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.title("La Liga Intelligence - Gráfico de Cartões Vermelhos (Pizza)")
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.legend(bbox_to_anchor=(0, 0.5))
    plt.show()

def ca_hi(ca):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(ca) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Cartões Amarelos')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def cv_hi(cv):
    plt.close()
    plt.rcParams.update({'font.size': 10})
    plt.hist(cv) 
    plt.ylabel('Nº de Times')
    plt.xlabel('Cartões Vermelhos')
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def ca_pl(nome, ca):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, ca)
    plt.ylabel('Cartões Amarelos')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Cartões Amarelos (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def cv_pl(nome, cv):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.plot(nome, cv)
    plt.ylabel('Cartões Vermelhos')
    plt.subplots_adjust(left=0.02, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Cartões Vermelhos (Plot)")
    
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def ca_sp(nome, ca):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, ca, label='Cartões Amarelos', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Cartões Amarelos (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()

def cv_sp(nome, cv):
    plt.close()
    plt.rcParams.update({'font.size': 8})
    plt.scatter(nome, cv, label='Cartões Vermelhos', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico de Cartões Vermelhos (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()