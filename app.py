from models.campeonato import Cpt
from models.times import Time
# from views.intro import *
from views.home import App
from tkinter import *
from controllers.atualizarBD import update
from pathlib import Path
import os

p = Path(os.getcwd())
update()
a = Cpt()
timesID = a.getTimes()
timeID = []; timeNome = []; timePosicao = []; timePontos = []; timeVitorias = []; timeEmpates = []; timeDerrotas = []
timePartidas = []; timeGolsPro = []; timeGolsContra = []; timeSaldo = []; timeCartoesA = []; timeCartoesV = []

for times in timesID:
    for id in times:
        timeID.append(Time(id))
        
for times in timeID:
    timeNome.append(times.getNome())
    timePosicao.append(times.getPosicao())
    timePontos.append(times.getPontos())
    timeVitorias.append(times.getVitorias())
    timeEmpates.append(times.getEmpates())
    timeDerrotas.append(times.getDerrotas())
    timePartidas.append(times.getPartidas())
    timeGolsPro.append(times.getGolsPro())
    timeGolsContra.append(times.getGolsContra())
    timeSaldo.append(times.getSaldo())
    timeCartoesA.append(times.getCartoesA())
    timeCartoesV.append(times.getCartoesV())

root = Tk()
root.title("La Liga Intelligence")
root.state("zoomed")
root.iconbitmap(str(p)+"\\assets\\img\\icon.ico")
app = App(root, timePosicao, timeNome, timePontos, timePartidas, timeVitorias, timeEmpates, timeDerrotas, timeGolsPro, timeGolsContra, timeSaldo, timeCartoesA, timeCartoesV)