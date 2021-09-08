# import nltk
# nltk.download('punkt')
# import nltk
# nltk.download('stopwords')
# import calendar
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4
# from reportlab.lib.units import inch

# myCanvas = canvas.Canvas('myfile.pdf', pagesize=letter, bottomup = 0)
# width, height = letter #keep for later
# print(width,height)
# myCanvas.drawString(0.5*inch, 0.5*inch, "(2.5,1) in inches")

# textobject = myCanvas.beginText(10, 20)
# myCanvas.drawText(textobject)
# myCanvas.showPage()
# myCanvas.save()

# def hello(c):
#     # move the origin up and to the left
#     # c.translate(inch,inch)
#     # define a large font
#     # c.setFont("Helvetica", 14)

#     c.drawString(10,20,"Hello World")

# # cal = calendar.month(2021, 8)
# # print("Here is the calendar:")
# # print(cal)

# def main():
#     print("Start")
#     c = canvas.Canvas("hello.pdf", bottomup = 0)
#     hello(c)
#     c.showPage()
#     c.save()

# if(__name__ == "__main__"):
#     main()

# import goslate
# gs = goslate.Goslate()
# print(gs.translate('free', 'bn'))
"# -*- coding: utf-8 -*-"
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config
import os

file = "bangla_sample.pdf"
# file_path = os.path.expanduser("~") +"/Documents/" + file

pdfmetrics.registerFont(TTFont("SolaimanLipi", r"D:\PythonProject\dictionary_project\fonts\SolaimanLipi.ttf")) #os.path.expanduser("~") +"/.local/share/fonts/SolaimanLipi_Bold_10-03-12.ttf"))

rl_config._SAVED['canvas_basefontname'] = 'SolaimanLipi'
rl_config._startUp()

page = canvas.Canvas(file, pagesize=portrait(A4))

page.setFont("SolaimanLipi", 20)

page.drawString(200, 300, "স্যাভলন হ্যান্ডওয়াশ ওসেন ব্লু ১০০০ মিলিঃ!")
page.drawCentredString(200, 200, "গণপ্রজাতন্ত্রী বাংলাদেশ!")
page.drawRightString(200, 100, "Hello World! 123")

page.save()

# import bangla
# bangla_date = bangla.get_date() # date, month, year
# print(bangla_date)

# Paragraph(
# 'caseSensitive': 1
# 'encoding': 'utf8'
# 'text': 'of<br/>এর'
# 'frags': [ParaFrag(__tag__='para', bold=1, fontName='AmarBangla', fontSize=12, greek=0, italic=1, link=[], rise=0, text='of', textColor=Color(0,0,0,1), us_lines=[]), 
# ParaFrag(__tag__='br', bold=1, fontName='AmarBangla', fontSize=12, greek=0, italic=1, lineBreak=True, link=[], rise=0, text='', textColor=Color(0,0,0,1), 
# us_lines=[]), 
# ParaFrag(__tag__='para', bold=1, fontName='AmarBangla', fontSize=12, greek=0, italic=1, link=[], rise=0, text='এর', textColor=Color(0,0,0,1), us_lines=[])]
# 'style': <ParagraphStyle 'AmarBangla'>
# 'bulletText': None
# 'debug': 0
# )

# coding=utf-8
from bnbphoneticparser import BengaliToBanglish


bengali2banglish = BengaliToBanglish()
bengali_text = "আমি বাংলাদেশি"
print(bengali2banglish.parse(bengali_text.strip()))

# aMi BAngLAdESi

# coding=utf-8
from bnbphoneticparser import BanglishToBengali


banglish2bengali = BanglishToBengali()
banglish_text = "ami banglay gan gai"
print(banglish2bengali.parse(banglish_text.strip()))

# আমি বাংলায় গান গাই

from bijoy2unicode import converter

test = converter.Unicode()
bijoy_text = 'Dfq cv‡k av‡bi kx‡l †ewóZ cvwb‡Z fvmgvb RvZxq dzj kvcjv| Zvi gv_vq cvUMv‡Qi ci¯úi mshy³ wZbwU cvZv Ges Dfh cv‡k `ywU K‡i ZviKv|'
name_text = 'Kyš—j Kvwš— `vm.'
print(bijoy_text)
another_text = ""
toPrint=test.convertBijoyToUnicode(name_text)
print(toPrint)
# উভয় পাশে ধানের শীষে বেষ্টিত পানিতে ভাসমান জাতীয় ফুল শাপলা। তার মাথায় পাটগাছের পরস্পর সংযুক্ত তিনটি পাতা এবং উভয পাশে দুটি করে তারকা।

toPrint=test.convertUnicodeToBijoy(another_text)
print(toPrint)