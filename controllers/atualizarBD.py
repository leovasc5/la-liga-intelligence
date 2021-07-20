import pandas as pd
from pathlib import Path
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from database.conexao import *

def update():
    p = Path(os.getcwd())
    ct = list(range(0,20))

    df = pd.read_csv(str(p)+"\\database\\dados.csv", encoding="UTF-8", sep=";")
    id = [df.loc[0:20]["ID"]]
    nome = list([df.loc[0:20]["nome"]])
    pontos = list([df.loc[0:20]["pontos"]])
    vitorias = list([df.loc[0:20]["vitorias"]])
    empates = list([df.loc[0:20]["empates"]])
    derrotas = list([df.loc[0:20]["derrotas"]])
    partidas = list([df.loc[0:20]["partidas"]])
    posicao = list([df.loc[0:20]["posicao"]])
    golsPro = list([df.loc[0:20]["golsPro"]])
    golsContra = list([df.loc[0:20]["golsContra"]])
    saldo = list([df.loc[0:20]["saldo"]])
    cartoesA = list([df.loc[0:20]["cartoesA"]])
    cartoesV = list([df.loc[0:20]["cartoesV"]])

    for i in ct:
        try:
            dml("""UPDATE times SET nome='"""+nome[0][i]+"""', pontos= '"""+str(pontos[0][i])+"""', vitorias='"""+str(vitorias[0][i])+"""', 
            empates='"""+str(empates[0][i])+"""', derrotas='"""+str(derrotas[0][i])+"""', partidas='"""+str(partidas[0][i])+"""', posicao='"""+str(posicao[0][i])+"""', golsPro='"""+str(golsPro[0][i])+"""', 
            golsContra='"""+str(golsContra[0][i])+"""', saldo='"""+str(saldo[0][i])+"""', cartoesA='"""+str(cartoesA[0][i])+"""', cartoesV='"""+str(cartoesV[0][i])+"""'
            WHERE ID='"""+str(id[0][i])+"""'""")
        except:
            print("Erro")
        
    

update()