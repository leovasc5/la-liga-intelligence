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
