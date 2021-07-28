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
print(p)
cnv = canvas.Canvas(caminho+"relatorio_pontuacao.pdf", pagesize=A4)
cnv.drawImage(str(p)+"\\assets\\img\\logo.png", x=50, y=750, width=150, height=50, mask="auto")

cnv.setFont('Helvetica-Bold', 12)
cnv.drawString(260, 75, "Desenvolvido por: ")
cnv.setFont('Helvetica', 12)
cnv.drawString(370, 75, "Leonardo Vasconcelos Paulino")
cnv.setTitle("Relatório de Pontuação da La Liga")

cnv.setFont('Helvetica-Bold', 12)
cnv.drawString(260, 50, "GitHub: ")
cnv.setFont('Helvetica', 12)
cnv.drawString(308, 50, "www.github.com/leovasc5")
cnv.linkURL("https://github.com/leovasc5",(300,50))



# cnv.setTitle("Relatório de Pontuação da La Liga")

cnv.save()
cnv.showPage()
print("PDF Criado")