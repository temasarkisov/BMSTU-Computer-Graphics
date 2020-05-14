from tkinter import *
import tkinter.ttk as ttk
from functools import partial
from menu_operation import *
from ui import *


sizeTuple = (1280, 800)
positionTuple = (100, 50)
# [center, scale, angel, single...]
dataOptions = {
    "center": (0.0, 1.0), 
    "scale": [1.0, 1.0], 
    "sumScale": [1.0, 1.0], 
    "angle": 90, 
    "singlePiece": 350.0
}
listPoints = []
returnData = []

# create window and canvas for screen
window = createRootWindow(sizeTuple, positionTuple)

placeGraph = Canvas(window, width=800, height=800, bg="white")

labelM = Label(text="Изменение масштаба:", width=19, font=("Helvetica", 18), bg="#D8D8D8")
labelP = Label(text="Перемещение:", width=12, font=("Helvetica", 18), bg="#D8D8D8")
labelA = Label(text="Поворот:", width=8, font=("Helvetica", 18), bg="#D8D8D8")

label1 = Label(text="kx:", width=3, font=("Helvetica", 16), bg="#D8D8D8")
label2 = Label(text="ky:", width=3, font=("Helvetica", 16), bg="#D8D8D8")
label3 = Label(text="центер:", width=7, font=("Helvetica", 16), bg="#D8D8D8")

label4 = Label(text="dx:", width=3, font=("Helvetica", 16), bg="#D8D8D8")
label5 = Label(text="dy:", width=3, font=("Helvetica", 16), bg="#D8D8D8")

label6 = Label(text="центер:", width=7, font=("Helvetica", 16), bg="#D8D8D8")
label7 = Label(text="угол:", width=5, font=("Helvetica", 16), bg="#D8D8D8")

entryScaleX = Entry(width=7, bg="white")
entryScaleY = Entry(width=7, bg="white")
entryScaleCenter = Entry(width=11, bg="white")

entryRotateCenter = Entry(width=7, bg="white")
entryRotateAngel = Entry(width=7, bg="white")

entryTransposeX = Entry(width=7, bg="white")
entryTransposeY = Entry(width=7, bg="white")

widgets = {
    "entryScaleX": entryScaleX,
    "entryScaleY": entryScaleY,
    "entryScaleCenter": entryScaleCenter,
    "entryTransposeX": entryTransposeX,
    "entryTransposeY": entryTransposeY,
    "entryRotateCenter": entryRotateCenter,
    "entryRotateAngel": entryRotateAngel,
    "listPoints": listPoints,
    "returnData": returnData
}

buttonClear = createButton(window, "Установить первоначальные\nзначения", (25, 3), 
    partial(paintStartPick, placeGraph, listPoints, returnData, dataOptions))
buttonBack = createButton(window, "Назад", (15, 3), 
    partial(setUndo, placeGraph, widgets, dataOptions))
buttonScale = createButton(window, "Изменить масштаб", (20, 1), 
    partial(zoomOut, placeGraph, widgets, dataOptions))
buttonTranspose = createButton(window, "Перенести", (20, 1), 
    partial(changePosition, placeGraph, widgets, dataOptions))
buttonRotate = createButton(window, "Повернуть", (20, 1), 
    partial(changeIncline, placeGraph, widgets, dataOptions))



# set location
placeGraph.pack(side=RIGHT)

entryScaleX.place(x=140, y=130)
entryScaleY.place(x=350, y=130)
entryScaleCenter.place(x=140, y=180)
entryTransposeX.place(x=140, y=280)
entryTransposeY.place(x=350, y=280)
entryRotateCenter.place(x=140, y=430)
entryRotateAngel.place(x=350, y=430)

labelM.place(x=0, y=100)
labelP.place(x=5, y=250)
labelA.place(x=5, y=400)
buttonClear.place(x=5, y=30, anchor="nw")
buttonBack.place(x=300, y=30)
label1.place(x=100, y=130)
label2.place(x=310, y=130)
label3.place(x=65, y=180)
label4.place(x=100, y=280)
label5.place(x=310, y=280)
label6.place(x=65, y=430)
label7.place(x=292, y=430)

buttonScale.place(x=280, y=185)
buttonTranspose.place(x=280, y=325)
buttonRotate.place(x=280, y=475)

paintStartPick(placeGraph, listPoints, returnData, dataOptions)

window.mainloop()
