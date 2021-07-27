from reportlab import *
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table

doc = SimpleDocTemplate(os.path.dirname(__file__)+"\\contatos.pdf", pagesize=A4)