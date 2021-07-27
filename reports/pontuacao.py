import os, sys, inspect
from pathlib import Path
from reportlab import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

p = Path(os.getcwd())
caminho = str(p)+"\\assets\\dataFiles\\"
print(type(caminho))
cnv = canvas.Canvas(caminho+"relatorio_pontuacao.pdf", pagesize=A4)
cnv.drawString(50, 50, "Leonardo Vasconcelos")
cnv.setTitle("Relatório de Pontuação da La Liga")
cnv.save()
cnv.showPage()
print("PDF Criado")
# doc.build()