from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def create_pdf(nume, prenume, output_path="output.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Nume: {nume}")
    c.drawString(100, 730, f"Prenume: {prenume}")
    c.save()
    return output_path