import os
from tkinter.constants import NONE
import conexao
rodada = 1
jogos = [1,2,3,4,5,6,7,8,9,10]
null = str(None)

while rodada <= 38:
    for i in jogos:
        print("\n===================\nRodada "+str(rodada)+": Jogo "+str(i))
        timex = input("\nTime Casa: ")
        timey = input("Time Fora: ")
        res = conexao.dml("INSERT INTO rodadas VALUES('"+timex+"', '"+timey+"', '"+NONE+"', '"+NONE+"', '"+str(0)+"', '"+str(rodada)+"')")
    rodada+=1
    os.system("cls")