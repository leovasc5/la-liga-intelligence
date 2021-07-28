import pandas as pd
from pathlib import Path
import os, sys, inspect
from tkinter import messagebox

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
            empates='"""+str(empates[0][i])+"""', derrotas='"""+str(derrotas[0][i])+"""', partidas='"""+str(partidas[0][i])+"""', posicao='"""+str(posicao[0][i])+"""', 
            golsPro='"""+str(golsPro[0][i])+"""', golsContra='"""+str(golsContra[0][i])+"""', saldo='"""+str(saldo[0][i])+"""', cartoesA='"""+str(cartoesA[0][i])+"""', 
            cartoesV='"""+str(cartoesV[0][i])+"""'WHERE ID='"""+str(id[0][i])+"""'""")
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

def updateEquipe(n_equipe, n_pontos, n_partidas, n_vitorias, n_empates, n_derrotas, n_gp, n_gc, n_ca, n_cv):
    p = Path(os.getcwd())
    
    df = pd.read_csv(str(p)+"\\database\\dados.csv", encoding="UTF-8", sep=";")
    dados = df.to_dict()
    # index = None

    for a in dados["nome"]:
        if dados["nome"][a] == n_equipe:


    # dados["pontos"] = 
    # dados["vitorias"] =
    # dados["empates"] =
    # dados["derrotas"] =
    # dados["partidas"] =
    # dados["posicao"] =
    # dados["golsPro"] =
    # dados["golsContra"] =
    # dados["saldo"] =
    # dados["cartoesA"] =
    # dados["cartoesV"] =

    # print("\n")
    # print(n_equipe)
    # print(n_partidas)
    # print(n_pontos)
    # print(n_vitorias)
    # print(n_empates)
    # print(n_derrotas)
    # print(n_gp)
    # print(n_gc)
    # print(n_ca)
    # print(n_cv)

updateEquipe("Real Madrid", 87, 39, 26, 9, 4, 70, 28, 57, 4)