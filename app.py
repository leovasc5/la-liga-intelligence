from classes.campeonato import Cpt
from classes.times import Time
from view.intro import *
from view.home import App
import time

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

root = App(timePosicao, timeNome, timePontos, timePartidas, timeVitorias, timeEmpates, timeDerrotas, timeGolsPro, timeGolsContra, timeSaldo, a.getRodadas())