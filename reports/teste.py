import matplotlib.pyplot as plt
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

fig = plt.figure(figsize=(4, 3))
plt.plot([1,2,3,4])
plt.ylabel('some numbers')

imgdata = BytesIO()
fig.savefig(imgdata, format='svg')
imgdata.seek(0)  # rewind the data

drawing=svg2rlg(imgdata)

c = canvas.Canvas('test2.pdf')
renderPDF.draw(drawing,c, 10, 40)
c.drawString(10, 300, "So nice it works")
c.showPage()
c.save()