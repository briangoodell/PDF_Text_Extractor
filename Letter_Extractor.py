# The end goal is for it to show you a letter and you select some examples of it on the page.
# Then those are added to a folder with other training material for the eventual neural net

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from PIL import Image, ImageTk
from tkinter import *  

## Turns PDF into image to display
images = convert_from_path('Source.pdf',poppler_path = r"C:\Users\brian\Documents\GitHub\PDF_Text_Extractor\poppler-21.02.0\Library\bin", first_page=1, last_page=2, fmt='JPEG')
#images = convert_from_bytes(open('Source.pdf', 'rb').read())

img = images[1]
#img.show()

## Creates a Tkinter instance where you can choose the corners of the letter
root = Tk()      
canvas = Canvas(root, width = 10000, height = 10000)      
canvas.pack()
tkimg = ImageTk.PhotoImage(img)
canvas.create_image(10,10, anchor=NW, image=tkimg)

# Determine the origin by clicking
def firstcorner(eventorigin):
    global x0,y0
    x0 = eventorigin.x
    y0 = eventorigin.y
    print(x0,y0)
    w.bind("<Button 1>",secondcorner)

# Determine the origin by clicking
def secondcorner(eventorigin):
    global x1,y1
    x1 = eventorigin.x
    y1 = eventorigin.y
    print(x0,y0)
    #w.bind("<Button 1>",getextentx)

#Cuts the selected section of the image
def cutimage():
    
    
#mouseclick event
root.bind("<Button 1>",firstcorner)

root.mainloop() 