import os, sys, inspect
from tkinter import messagebox

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from database.conexao import *

class Cpt:
    def __init__(self):
        self.nome = self.setNome()
        #self.times = self.setTimes() #Implementar quando o BD tiver a tabela Times
        self.gols = self.setGols()
        self.assistencias = self.setAssistencias()
        self.clean_sheets = self.setCleanSheets()
        self.cartoes_a = self.setCartoesA()
        self.cartoes_v = self.setCartoesV()
        self.rodadas = self.setRodadas()
        self.times = self.setTimes()

    def setNome(self):
        try:
            res = dql("SELECT nome FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")


    def getNome(self):
        return self.nome

    def setGols(self):
        try:
            res = dql("SELECT gols FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")
    
    def getGols(self):
        return self.gols

    def setAssistencias(self):
        try:
            res = dql("SELECT assistencias FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getAssistencias(self):
        return self.assistencias

    def setCleanSheets(self):
        try:
            res = dql("SELECT cls FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getCleanSheets(self):
        return self.clean_sheets

    def setCartoesA(self):
        try:
            res = dql("SELECT cartoes_amarelos FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getCartoesA(self):
        return self.cartoes_a

    def setCartoesV(self):
        try:
            res = dql("SELECT cartoes_vermelhos FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getCartoesV(self):
        return self.cartoes_v

    def setRodadas(self):
        try:
            res = dql("SELECT rodadas FROM campeonato")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getRodadas(self):
        return self.rodadas

    def setTimes(self):
        try:
            res = dql("SELECT ID FROM times ORDER BY posicao")
            return res
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getTimes(self):
        return self.times