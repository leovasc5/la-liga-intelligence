import os, sys, inspect
from pathlib import Path
from reportlab import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import statistics
import matplotlib.pyplot as plt
from tkinter.constants import CENTER
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
import seaborn as sns

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from models.times import getDados

def criarPDF_gols():
    dados = getDados()
    posicao = dados["posicao"]
    nome = dados["nome"]
    pontos = dados["pontos"]
    saldo = dados["saldo"]
    gp = dados["gp"]
    gc = dados["gc"]
    
    p = Path(os.getcwd())
    caminho = str(p)+"\\assets\\dataFiles\\"
    cnv = canvas.Canvas(caminho+"LaLigaGols.pdf", pagesize=A4)
    cnv.drawImage(str(p)+"\\assets\\img\\logo.png", x=50, y=750, width=150, height=50, mask="auto")

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 75, "Desenvolvido por: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(370, 75, "Leonardo Vasconcelos Paulino")
    cnv.setTitle("La Liga - Relatório de Gols")

    cnv.setFont('Helvetica-Bold', 24)
    cnv.drawString(200,690, "Relatório de Gols")

    cnv.rect(95, 195, 55, 420, stroke=1, fill=0)
    cnv.rect(95, 195, 200, 420, stroke=1, fill=0)
    cnv.rect(95, 195, 260, 420, stroke=1, fill=0)
    cnv.rect(95, 195, 320, 420, stroke=1, fill=0)
    cnv.rect(95, 195, 380, 420, stroke=1, fill=0)
    cnv.rect(95, 195, 440, 420, stroke=1, fill=0)

    cnv.rect(95, 195, 260, 400, stroke=1, fill=0)
    cnv.rect(95, 195, 320, 400, stroke=1, fill=0)
    cnv.rect(95, 195, 380, 400, stroke=1, fill=0)
    cnv.rect(95, 195, 440, 400, stroke=1, fill=0)
    
    p1 = 580
    p2 = 100
    p3 = 160
    p4 = 300
    p5 = 360
    p6 = 420
    p7 = 480
    j = 0

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(100, 600, "Posição")
    cnv.drawString(160, 600, "Time")
    cnv.drawString(300, 600, "Pontos")
    cnv.drawString(360, 600, "Gols +")
    cnv.drawString(420, 600, "Gols -")
    cnv.drawString(480, 600, "Saldo")
    cnv.setFont('Helvetica', 12)
    for i in posicao:
        cnv.drawString(p2,p1, (str(posicao[j])+"º"))
        cnv.drawString(p3,p1, str(nome[j]))
        cnv.drawString(p4,p1, str(pontos[j]))
        cnv.drawString(p5,p1, str(gp[j]))
        cnv.drawString(p6,p1, str(gc[j]))
        cnv.drawString(p7,p1, str(saldo[j]))
        j+=1
        p1=p1-20
        
    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 50, "GitHub: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(308, 50, "www.github.com/leovasc5")
    cnv.linkURL("https://github.com/leovasc5",(300,50))

    cnv.showPage()

    cnv.drawImage(str(p)+"\\assets\\img\\logo.png", x=50, y=750, width=150, height=50, mask="auto")

    plt.close()
    fig = plt.figure(figsize=(7, 4))
    plt.subplots_adjust(bottom=0.18, top=0.88)
    tickvalues = range(0,len(nome))
    plt.xticks(ticks=tickvalues, labels=nome, rotation='vertical')
    plt.plot(gp)
    plt.plot(gc)
    plt.ylabel('Gols')
    plt.legend(("Gols Pró", "Gols Sofridos"))

    imgdata = BytesIO()
    fig.savefig(imgdata, format='svg', dpi=199)
    imgdata.seek(0)

    drawing=svg2rlg(imgdata)

    renderPDF.draw(drawing, cnv, -5, 270)

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 50, "GitHub: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(308, 50, "www.github.com/leovasc5")
    cnv.linkURL("https://github.com/leovasc5",(300,50))

    cnv.showPage()

    cnv.drawImage(str(p)+"\\assets\\img\\logo.png", x=50, y=750, width=150, height=50, mask="auto")

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 75, "Desenvolvido por: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(370, 75, "Leonardo Vasconcelos Paulino")
    cnv.setTitle("La Liga - Relatório de Pontuação")

    plt.close()
    fig = plt.figure(figsize=(7, 4))
    plt.pie(pontos, labels=nome, startangle=90, explode=[0 for i in range(20)])
    plt.rcParams.update({'font.size': 10})

    plt.title("La Liga Intelligence - Gráfico da Pontuação (Pizza)")
    plt.legend(bbox_to_anchor=(0, 0.5))

    imgdata = BytesIO()
    fig.savefig(imgdata, format='svg', dpi=199)
    imgdata.seek(0)

    drawing=svg2rlg(imgdata)

    renderPDF.draw(drawing, cnv, 30, 350)

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 50, "GitHub: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(308, 50, "www.github.com/leovasc5")
    cnv.linkURL("https://github.com/leovasc5",(300,50))

    cnv.showPage()

    cnv.drawImage(str(p)+"\\assets\\img\\logo.png", x=50, y=750, width=150, height=50, mask="auto")

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 75, "Desenvolvido por: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(370, 75, "Leonardo Vasconcelos Paulino")
    cnv.setTitle("La Liga - Relatório de Gols")

    plt.close()
    fig = plt.figure(figsize=(7, 4))
    sns.set_style("whitegrid")
    blue, = sns.color_palette("muted", 1)
    fig, ax = plt.subplots()
    ax.plot(pontos, saldo, color=blue, lw=2)
    ax.fill_between(pontos, 0, saldo, alpha=.3)
    ax.set(xlim=(min(pontos), max(pontos)), ylim=(-50, 60), xticks=pontos)
    plt.xlabel("Pontos")
    plt.ylabel("Saldo")
    plt.title("Area Chart")
    plt.legend()

    plt.title("La Liga Intelligence - Gráfico da Pontuação (Pizza)")
    plt.legend(bbox_to_anchor=(0, 0.5))

    imgdata = BytesIO()
    fig.savefig(imgdata, format='svg', dpi=199)
    imgdata.seek(0)

    drawing=svg2rlg(imgdata)

    renderPDF.draw(drawing, cnv, 0, 10)

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 50, "GitHub: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(308, 50, "www.github.com/leovasc5")
    cnv.linkURL("https://github.com/leovasc5",(300,50))

    cnv.showPage()

    cnv.save()
    print("PDF Criado")



    # plt.close()
    # sns.set_style("whitegrid")
    # blue, = sns.color_palette("muted", 1)
    # fig, ax = plt.subplots()
    # ax.plot(pontos, saldo, color=blue, lw=2)
    # ax.fill_between(pontos, 0, saldo, alpha=.3)
    # ax.set(xlim=(min(pontos), max(pontos)), ylim=(-50, 60), xticks=pontos)
    # plt.xlabel("Pontos")
    # plt.ylabel("Saldo")
    # plt.title("Area Chart")
    # plt.legend()