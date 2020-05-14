from tkinter import ttk
from tkinter import *
import math

root = Tk()
root.geometry("800x640+100+100")

canvas_width = 550
canvas_height = 550

pointsList = []



def paintOnePoint(canvas, x, y):
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")
    
    #pointCoordinatesString = "(" + str(xOriginal) + ";" + str(yOriginal) + ")"
    #canvas.create_text(x + 5, y + 10, text=pointCoordinatesString, justify=CENTER, font="Verdana 7", fill="grey")

def removePoint(canvas, pointsList):
    select = list(listbox.curselection())
    select.reverse()
    for i in select:
        listbox.delete(i)
    
    #pointsList.pop(len(pointsList) - select[0] - 1)
    
    pointsList = []
    for point in listbox.get(0, END):
        pointsList.append([float(point[0]), float(point[1]), float(point[0]), float(point[1])])
    
    if (pointsList != []):
        pointsList = pointsListFormation(pointsList)
    
    canvas.delete("all")

    print("pointsList in removePoint :", pointsList)

    if (pointsList != []):
        showPoints(canvas, pointsList)

def addPoint(canvas, pointsList):
    pointsString = pointsEntry.get()
    coordList = list(map(float, pointsString.split()))
    pointsList = []

    for i in range (0, len(coordList), 2): 
        listbox.insert(0, [coordList[i], coordList[i + 1]])

    for point in listbox.get(0, END):
        pointsList.append([float(point[0]), float(point[1]), float(point[0]), float(point[1])])

    pointsList = pointsListFormation(pointsList)

    canvas.delete("all")
    if (pointsList != []):
        showPoints(canvas, pointsList)

    return pointsList

def maxXYDef(pointsList):
    minX, maxX = pointsList[0][0], pointsList[0][0]
    minY, maxY = pointsList[0][1], pointsList[0][1]

    for i in range (len(pointsList)):
        if (pointsList[i][0] <= minX):
            minX = pointsList[i][0]
        if (pointsList[i][0] >= maxX):
            maxX = pointsList[i][0]
        if (pointsList[i][1] <= minY):
            minY = pointsList[i][1]
        if (pointsList[i][1] >= maxY):
            maxY = pointsList[i][1]

    maxXY = max(minX, maxX, minY, maxY)
    minXY = min(minX, maxX, minY, maxY)

    return maxXY, minXY

def pointsListFormation(pointsList):
    if (pointsList == []):
        listbox.delete(0, END)

        pointsString = pointsEntry.get()
        coordList = list(map(float, pointsString.split()))

        for i in range (0, len(coordList), 2): 
            pointsList.append([coordList[i], coordList[i + 1], coordList[i], coordList[i + 1]])
            listbox.insert(0, [coordList[i], coordList[i + 1]])

    maxXY, minXY = maxXYDef(pointsList)

    if (minXY < 0):
        for i in range(len(pointsList)):
            pointsList[i][0] += (abs(minXY))
            pointsList[i][1] += (abs(minXY))

    maxXY, minXY = maxXYDef(pointsList)
    singleSegment = 500 / abs(maxXY)

    for i in range(len(pointsList)):
        pointsList[i][0] *= singleSegment
        pointsList[i][1] *= singleSegment
        pointsList[i][1] -= 550
        pointsList[i][1] *= -1
        pointsList[i][0] += 25
        pointsList[i][1] -= 25

    print("pointsList in pointsListFormation:", pointsList)

    return pointsList

def showPoints(canvas, pointsList):
    if (pointsList == []):
        pointsList = pointsListFormation(pointsList)

    for point in pointsList:    
        paintOnePoint(canvas, point[0], point[1], point[2], point[3])

    return pointsList

def sidesLengthDef(trianglePoints):
    sidesLength = []

    for ind in range(len(trianglePoints)):
        sidesLength.append(math.sqrt(
            (trianglePoints[ind][0] - trianglePoints[ind - 1][0]) * 
            (trianglePoints[ind][0] - trianglePoints[ind - 1][0]) + 
            (trianglePoints[ind][1] - trianglePoints[ind - 1][1]) * 
            (trianglePoints[ind][1] - trianglePoints[ind - 1][1])))

    sidesLength[0], sidesLength[1] = sidesLength[1], sidesLength[0]
    sidesLength[0], sidesLength[2] = sidesLength[2], sidesLength[0]

    return sidesLength    

def radiusCirclesDef(sidesLength):
    semiperimeter = 0.0

    semiperimeter = (sidesLength[0] + sidesLength[1] + sidesLength[2]) / 2
    sidesProduct = sidesLength[0] * sidesLength[1] * sidesLength[2]
    radiusCircum = sidesProduct / (4 * math.sqrt(semiperimeter * 
                                    (semiperimeter - sidesLength[0]) * 
                                    (semiperimeter - sidesLength[1]) * 
                                    (semiperimeter - sidesLength[2])))

    radiusInscribed = math.sqrt((semiperimeter - sidesLength[0]) * 
                                (semiperimeter - sidesLength[1]) * 
                                (semiperimeter - sidesLength[2]) / semiperimeter)

    return radiusCircum, radiusInscribed

def interPointsInscribedDef(trianglePoints, sidesLength):
    interPointInscribedX = (trianglePoints[0][0] * sidesLength[0] + 
                           trianglePoints[1][0] * sidesLength[1] + 
                           trianglePoints[2][0] * sidesLength[2]) / (sidesLength[0] + sidesLength[1] + sidesLength[2])
    
    interPointInscribedY = (trianglePoints[0][1] * sidesLength[0] + 
                           trianglePoints[1][1] * sidesLength[1] + 
                           trianglePoints[2][1] * sidesLength[2]) / (sidesLength[0] + sidesLength[1] + sidesLength[2])

    return interPointInscribedX, interPointInscribedY

def paintCircle(canvas, x, y, r):
    canvas.create_oval(x - r, y - r, x + r, y + r)

def paintTriangle(canvas, trianglePoints):
    for ind in range(len(trianglePoints)):
        canvas.create_line(trianglePoints[ind][0], trianglePoints[ind][1], 
                           trianglePoints[ind - 1][0], trianglePoints[ind - 1][1])

def isPointsCollinear(trianglePoints):
    if (abs(((trianglePoints[2][1] - trianglePoints[0][1]) * (trianglePoints[1][0] - trianglePoints[0][0])) -
        ((trianglePoints[2][0] - trianglePoints[0][0]) * (trianglePoints[1][1] - trianglePoints[0][1]))) < 0.0001):
        return True
    
    return False

def matrixDetDef(matrix):
    A = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    B = matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    C = matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    detMatrix = A - B + C
    
    return detMatrix

def interPointsCircumDef(trianglePoints):
    matrixXOne = [
              [trianglePoints[0][0] * trianglePoints[0][0] + trianglePoints[0][1] * trianglePoints[0][1], trianglePoints[0][1], 1.0],
              [trianglePoints[1][0] * trianglePoints[1][0] + trianglePoints[1][1] * trianglePoints[1][1], trianglePoints[1][1], 1.0],
              [trianglePoints[2][0] * trianglePoints[2][0] + trianglePoints[2][1] * trianglePoints[2][1], trianglePoints[2][1], 1.0]
              ]

    matrixYOne = [
              [trianglePoints[0][0], trianglePoints[0][0] * trianglePoints[0][0] + trianglePoints[0][1] * trianglePoints[0][1], 1.0],
              [trianglePoints[1][0], trianglePoints[1][0] * trianglePoints[1][0] + trianglePoints[1][1] * trianglePoints[1][1], 1.0],
              [trianglePoints[2][0], trianglePoints[2][0] * trianglePoints[2][0] + trianglePoints[2][1] * trianglePoints[2][1], 1.0]
              ]

    matrixXYTwo = [
              [trianglePoints[0][0], trianglePoints[0][1], 1.0],
              [trianglePoints[1][0], trianglePoints[1][1], 1.0],
              [trianglePoints[2][0], trianglePoints[2][1], 1.0]
              ] 

    interPointCircumX = matrixDetDef(matrixXOne) / (2 * matrixDetDef(matrixXYTwo))
    interPointCircumY = matrixDetDef(matrixYOne) / (2 * matrixDetDef(matrixXYTwo))

    return interPointCircumX, interPointCircumY

def showTriangle(canvas, pointsList):
    pointsList = []
    for point in listbox.get(0, END):
        pointsList.append([float(point[0]), float(point[1])])

    pointsList = pointsListFormation(pointsList)
    
    print("pointsList in showTriangle :", pointsList)
    if (len(pointsList) < 3):
        return False

    trianglePoints = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]
    sidesLength = [0.0, 0.0, 0.0]
    maxRadiusDiff = 0.0
    triangleReqPoints = [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]]

    for pointOneInd in range(len(pointsList) - 2):
        for pointTwoInd in range(pointOneInd + 1, len(pointsList) - 1):
            for pointThreeInd in range(pointTwoInd + 1, len(pointsList)):
                trianglePoints[0] = pointsList[pointOneInd]
                trianglePoints[1] = pointsList[pointTwoInd]
                trianglePoints[2] = pointsList[pointThreeInd]
                
                if (isPointsCollinear(trianglePoints) == False):
                    #print(trianglePoints)
                    sidesLength = sidesLengthDef(trianglePoints)
                    radiusCircum, radiusInscribed = radiusCirclesDef(sidesLength)
                    #print(radiusCircum, radiusInscribed)

                    if (radiusCircum - radiusInscribed >= maxRadiusDiff):
                        triangleReqPoints[0] = trianglePoints[0]
                        triangleReqPoints[1] = trianglePoints[1]
                        triangleReqPoints[2] = trianglePoints[2]
                        #print(triangleReqPoints)
                        maxRadiusDiff = radiusCircum - radiusInscribed
    
    if (maxRadiusDiff != 0.0):
        sidesLength = sidesLengthDef(triangleReqPoints)
        radiusCircum, radiusInscribed = radiusCirclesDef(sidesLength)
        print("triangleReqPoints =", triangleReqPoints)
        print("sidesLength =", sidesLength)
        interPointInscribedX, interPointInscribedY = interPointsInscribedDef(triangleReqPoints, sidesLength)
        print("interPointInscribedX, interPointInscribedY =", interPointInscribedX, interPointInscribedY)
        print("radiusInscribed =", radiusInscribed)
        interPointCircumX, interPointCircumY = interPointsCircumDef(triangleReqPoints)
        print("interPointInscribedX, interPointInscribedY =", interPointInscribedX, interPointInscribedY)
        print("radiusCircum =", radiusCircum)
        paintTriangle(canvas, triangleReqPoints)
        paintCircle(canvas, interPointInscribedX, interPointInscribedY, radiusInscribed)
        paintCircle(canvas, interPointCircumX, interPointCircumY, radiusCircum) 




def functionCircle(x, r, a, b):
    y = math.sqrt(r * r - (x - a) * (x - a)) + b

    return y

def functionParabola(x, c, d):
    y = c - (x - d) * (x - d) 

    return y

def ShowFigure(canvas):
    r = float(EntryR.get())
    a = float(EntryA.get())
    b = float(EntryB.get())
    c = float(EntryC.get())
    d = float(EntryD.get())

    xCur = 0
    while (functionCircle(xCur, r, a, b) < functionParabola(xCur, c, d)):
        paintOnePoint(canvas, xCur, functionCircle(xCur, r, a, b))
        xCur += 0.1

    




canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="#ffcccc")
canvas.place(x=220, y=55)   

#Label(root, text="X -").place(x=20, y=48)
#EntryX = StringVar(root)
#Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=50, y=48)

#Label(root, text="Y -").place(x=90, y=48)
#EntryY = StringVar(root)
#Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=120, y=48)

Label(root, text="R -").place(x=20, y=78)
EntryR = StringVar(root)
Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=50, y=78)

Label(root, text="A -").place(x=20, y=108)
EntryA = StringVar(root)
Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=50, y=108)

Label(root, text="B -").place(x=90, y=108)
EntryB = StringVar(root)
Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=120, y=108)

Label(root, text="C -").place(x=20, y=158)
EntryC = StringVar(root)
Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=50, y=158)

Label(root, text="D -").place(x=90, y=158)
EntryD = StringVar(root)
Entry = ttk.Entry(root, width = 2, textvariable=StringVar).place(x=120, y=158)

ShowPointsButton = Button(root, text="Show points", command= lambda: showPoints(canvas, pointsList)).place(x=20, y=300)
ShowFigure = Button(root, text="Show", command= lambda: ShowFigure(canvas)).place(x=120, y=300)



#AddPointButton = Button(root, text="Add point", command= lambda: addPoint(canvas, pointsList)).place(x=20, y=380)
#RemovePointButton = Button(root, text="Remove point", command= lambda: removePoint(canvas, pointsList)).place(x=120, y=380)
#ttk.Button(root, text="Edit points").place(x=60, y=260)

#listbox = Listbox(root)
#listbox.place(x=20, y=200)
#scroll = Scrollbar(command=listbox.yview)
#scroll.place(x=205, y=200)
#listbox.config(yscrollcommand=scroll.set)

root.mainloop()
