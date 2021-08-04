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
    
    p = Path(os.getcwd())
    caminho = str(p)+"\\assets\\dataFiles\\"
    cnv = canvas.Canvas(caminho+"LaLigaGols.pdf", pagesize=A4)
    cnv.drawImage(str(p)+"\\assets\\img\\logo.png", x=50, y=750, width=150, height=50, mask="auto")

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(260, 75, "Desenvolvido por: ")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(370, 75, "Leonardo Vasconcelos Paulino")
    cnv.setTitle("La Liga - Relatório de Pontuação")

    cnv.setFont('Helvetica-Bold', 24)
    cnv.drawString(160,690, "Relatório de Pontuação")

    cnv.rect(170, 195, 250, 420, stroke=1, fill=0)
    cnv.rect(170, 195, 55, 420, stroke=1, fill=0)
    cnv.rect(170, 195, 200, 420, stroke=1, fill=0)
    cnv.rect(170, 195, 250, 400, stroke=1, fill=0)
    
    p1 = 580
    p2 = 175
    p3 = 235
    p4 = 375
    j = 0

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(175, 600, "Posição")
    cnv.drawString(235, 600, "Time")
    cnv.drawString(375, 600, "Pontos")
    cnv.setFont('Helvetica', 12)
    for i in posicao:
        cnv.drawString(p2,p1, (str(posicao[j])+"º"))
        cnv.drawString(p3,p1, str(nome[j]))
        cnv.drawString(p4,p1, str(pontos[j]))
        j+=1
        p1=p1-20
        
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

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(50, 680, "Maior Pontuador:")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(155, 680, nome[0] + " ("+str(pontos[0])+")")

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(50, 660, "Menor Pontuador:")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(160, 660, nome[19] + " ("+str(pontos[19])+")")

    somatoria = 0
    for i in pontos:
        somatoria += i
    media = somatoria / len(pontos)
    moda = statistics.mode(pontos)

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(50, 640, "Pontuação Média:")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(160, 640, str(media))

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(50, 620, "Moda:")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(95, 620, str(moda))

    cnv.setFont('Helvetica-Bold', 12)
    cnv.drawString(50, 600, "Somatória:")
    cnv.setFont('Helvetica', 12)
    cnv.drawString(120, 600, str(somatoria))

    plt.rcParams.update({'font.size': 3})
    fig = plt.figure(figsize=(7, 4))
    plt.title("La Liga Intelligence - Gráfico da Pontuação (Barras)")
    plt.bar(nome, pontos, label='Pontos', width=0.5, align=CENTER)

    imgdata = BytesIO()
    fig.savefig(imgdata, format='svg', dpi=199)
    imgdata.seek(0)

    drawing=svg2rlg(imgdata)

    renderPDF.draw(drawing, cnv, -15, 190)

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
    cnv.setTitle("La Liga - Relatório de Pontuação")

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

    renderPDF.draw(drawing, cnv, 30, 250)

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