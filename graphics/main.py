from tkinter.constants import CENTER, RIGHT
import matplotlib.pyplot as plt

def pt_ba(nome, pontos):
    plt.rcParams.update({'font.size': 8})
    plt.subplots_adjust(left=0.02, bottom=0.11, right=0.98, top=0.88, wspace=0.2, hspace=0.82)
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Barras)")
    plt.bar(nome, pontos, label='Pontos', width=0.5, align=CENTER, )
 
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.legend()
    plt.show()

def pt_pi(nome, pontos):
    plt.pie(pontos, labels=nome, startangle = 90, shadow = True, explode=[0.1 for i in range(20)])
    
    plt.show()

print([0.1 for i in range(20)])