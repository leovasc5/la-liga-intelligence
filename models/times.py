import os, sys, inspect
from tkinter import messagebox

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from database.conexao import *

class Time:
    def __init__(self, id):
        self.id = self.setId(id)
        self.nome = self.setNome(id)
        self.pontos = self.setPontos(id)
        self.vitorias = self.setVitorias(id)
        self.empates = self.setEmpates(id)
        self.derrotas = self.setDerrotas(id)
        self.partidas = self.setPartidas(id)
        self.posicao = self.setPosicao(id)
        self.golsPro = self.setGolsPro(id)
        self.golsContra = self.setGolsContra(id)
        self.saldo = self.setSaldo(id)
        self.cartoesA = self.setCartoesA(id)
        self.cartoesV = self.setCartoesV(id)

    def setId(self, id): 
        self.id = id

    def getId(self):
        return self.id

    def setNome(self, id):
        try:
            res = dql("SELECT nome FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getNome(self):
        return self.nome

    def setPontos(self, id):
        try:
            res = dql("SELECT pontos FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")
    
    def getPontos(self):
        return self.pontos

    def setVitorias(self, id):
        try:
            res = dql("SELECT vitorias FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getVitorias(self):
        return self.vitorias

    def setEmpates(self, id):
        try:
            res = dql("SELECT empates FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getEmpates(self):
        return self.empates

    def setDerrotas(self, id):
        try:
            res = dql("SELECT derrotas FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getDerrotas(self):
        return self.derrotas

    def setPartidas(self, id):
        try:
            res = dql("SELECT partidas FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getPartidas(self):
        return self.partidas

    def setPosicao(self, id):
        try:
            res = dql("SELECT posicao FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getPosicao(self):
        return self.posicao

    def setGolsPro(self, id):
        try:
            res = dql("SELECT golsPro FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getGolsPro(self):
        return self.golsPro

    def setGolsContra(self, id):
        try:
            res = dql("SELECT golsContra FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getGolsContra(self):
        return self.golsContra

    def setSaldo(self, id):
        try:
            res = dql("SELECT saldo FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getSaldo(self):
        return self.saldo

    def setCartoesA(self, id):
        try:
            res = dql("SELECT cartoesA FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getCartoesA(self):
        return self.cartoesA

    def setCartoesV(self, id):
        try:
            res = dql("SELECT cartoesV FROM times WHERE ID = '"+str(id)+"'")
            return res[0][0]
        except:
            messagebox.showerror(title="Erro", message="A comunicação com o Banco de Dados não foi estabelecida")

    def getCartoesV(self, ):
        return self.cartoesV
 
