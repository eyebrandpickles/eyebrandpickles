##import os
##import img2pdf
##with open("out.pdf", "wb") as file:
##  file.write(img2pdf.convert([i for i in os.listdir('Path of              image_Directory') if i.endswith(".jpg")]))

from fpdf import FPDF
Pdf = FPDF()
list_of_images = ["IMG_3279.jpg"]
for i in list_of_images:
   Pdf.add_page()
   Pdf.image(i)
   Pdf.output("out.pdf", "F")