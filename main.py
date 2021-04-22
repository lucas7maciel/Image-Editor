import tkinter
from tkinter import Frame, Canvas, Scale
from commands import Comm

C = Comm()

#Create Window and Frames
master = tkinter.Tk()
master.title("Image Editor")
master.geometry("720x500")

imF = Frame(master, bg = "#daeef7")
reF = Frame(master, bg = "#daeef7")
roF = Frame(master, bg = "#daeef7")
efF = Frame(master, bg = "#daeef7")
buF = Frame(master, bg = "#daeef7")

C.fList = [buF, efF, reF, roF]

#Image frame
C.can = Canvas(imF, bg="pink", width=680, height=320)
C.can.pack(fill='both', expand=1, padx=20, pady=(15, 0))
C.imgCan = C.can.create_image(680 / 2, 320 / 2, anchor='center')

C.warningLabel=tkinter.Label(imF, text="You can drag and drop the image using the cursor")
C.warningLabel.pack()

C.can.bind('<B1-Motion>', C.Move)
imF.pack(fill='both', expand=1)

#Buttons frame
remBu=tkinter.Button(buF, text="Remove", width=10, command = lambda : C.UpdateIm(0))
remBu.grid(row=0, column=1, padx=10, pady=15)

upBu=tkinter.Button(buF, text="Upload", width=10, command = lambda : C.UpdateIm(1))
upBu.grid(row=0, column=2, padx=10, pady=15)

efBu=tkinter.Button(buF, text="Effects", width=20, command = lambda : C.Change("10"))
efBu.grid(row=1, column=0, padx=15, pady=25)

reBu=tkinter.Button(buF, text="Resize", width=20, command = lambda : C.Change("20"))
reBu.grid(row=1, column=1, padx=15, pady=25)

roBu=tkinter.Button(buF, text="Rotate", width=20, command = lambda : C.Change("30"))
roBu.grid(row=1, column=2, padx=15, pady=25)

saBu=tkinter.Button(buF, text="Save", width=20, command = C.Save)
saBu.grid(row=1, column=3, padx=15, pady=25)

buF.pack(fill = 'both', expand=1)

#Resize frame
wiLa=tkinter.Label(reF, text="Width", bg="white")
wiLa.grid(row=0, column=0, padx=10)
wiEn=tkinter.Entry(reF, bg="white")
wiEn.grid(row=1, column=0, padx=10, pady=10)

heLa=tkinter.Label(reF, text="Height", bg="white")
heLa.grid(row=0, column=1, padx=10)
heEn=tkinter.Entry(reF, bg="white")
heEn.grid(row=1, column=1, padx=10, pady=15)

okRe=tkinter.Button(reF, text="Ok", width=8, command = lambda : C.Resize(eList))
okRe.grid(row=2, column=1, pady=5)

backRe=tkinter.Button(reF, text="Back", command = lambda : C.Change("02"))
backRe.grid(row=2, column=0, padx=5)

eList = [wiEn, heEn]

#Rotate frame
roLa=tkinter.Label(roF, text="Rotate", bg="white")
roLa.grid(row=0, column=1, pady=10)

roSc=Scale(roF, from_=0, to=359, orient="horizontal")
roSc.grid(row=1, column=1, padx=5)

okRo=tkinter.Button(roF, text="Ok", width=8, command = lambda : C.Rotate(roSc.get()))
okRo.grid(row=1, column=2, padx=5)

backRo=tkinter.Button(roF, text="Back", command = lambda : C.Change("03"))
backRo.grid(row=1, column=0, padx=5)

#Effects frame
efNBu=tkinter.Button(efF, text="Negative", command = lambda : C.Effects(0))
efNBu.grid(row = 0, column = 0, padx = 15, pady = 15)

efGBu=tkinter.Button(efF, text="Gray", command = lambda : C.Effects(1))
efGBu.grid(row=0, column=1, padx=15, pady=15)

efSBu=tkinter.Button(efF, text="Solarize", command = lambda : C.Effects(2))
efSBu.grid(row=0, column=2, padx=15, pady=15)

backEf=tkinter.Button(efF, text="Back", command = lambda : C.Change("01"))
backEf.grid(row=1, column=1, padx=15, pady=15)

for a in C.fList:
	a.grid_columnconfigure('all', weight=1)
	a.grid_rowconfigure('all', weight=1)

master.mainloop()