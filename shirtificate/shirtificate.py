from fpdf import FPDF

pdf = FPDF(orientation = "P", unit = "mm", format = "A4")

pdf.add_page()

pdf.image('shirtificate.png', 10, 80, 190)

pdf.set_font('helvetica', 'B', 65)

pdf.set_text_color(0,0,0)

pdf.cell(210, 40, txt = 'CS50 Shirtificate', ln = True)

pdf.set_font('helvetica', 'B', 20)

pdf.set_text_color(255,255,255)

name = input('Name: ')

pdf.cell(190, 160,txt = f'{name} took CS50', align = 'C')

pdf.output("shirtificate.pdf")
