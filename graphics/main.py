from tkinter.constants import CENTER, RIGHT
import matplotlib.pyplot as plt
import os, sys, inspect
from pathlib import Path

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

p = Path(os.getcwd())
icon = str(p)+"\\assets\\img\\icon.ico"

def pt_ba(nome, pontos):
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
    plt.scatter(nome, pontos, label='Pontos', marker = 'o', s=100)
    plt.ylabel('Pontuação')
    plt.subplots_adjust(left=0.03, bottom=0.3, right=0.99, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (ScatterPlot)")

    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    wm.window.wm_iconbitmap(icon)
    plt.get_current_fig_manager().canvas.set_window_title('La Liga Intelligence')
    plt.show()