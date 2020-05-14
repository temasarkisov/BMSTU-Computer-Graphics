import style as style

def shapeIDCircle(window):
    window.shapeID.setStyleSheet(style.buttonMethodStyleSheet)
    window.shapeID = window.buttonShapeCircle
    window.shapeID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def shapeIDOval(window):
    window.shapeID.setStyleSheet(style.buttonMethodStyleSheet)
    window.shapeID = window.buttonShapeOval
    window.shapeID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDCanonicalEquation(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodCanonicalEquation
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDParametricEquation(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodParametricEquation
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDBreseham(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodBresenham
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDMeanPoint(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodMeanPoint
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDLib(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodLibrary
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def colorIDGreen(window):
    window.buttonColorID[0].setStyleSheet(style.buttonColorStyleSheet + window.buttonColorID[1])
    window.buttonColorID = window.buttonColorInfoArray[0]
    window.buttonColorID[0].setStyleSheet(window.buttonColorID[1] + style.buttonColorActiveStyleSheet)

def colorIDBlue(window):
    window.buttonColorID[0].setStyleSheet(style.buttonColorStyleSheet + window.buttonColorID[1])
    window.buttonColorID = window.buttonColorInfoArray[1]
    window.buttonColorID[0].setStyleSheet(window.buttonColorID[1] + style.buttonColorActiveStyleSheet)

def colorIDRed(window):
    window.buttonColorID[0].setStyleSheet(style.buttonColorStyleSheet + window.buttonColorID[1])
    window.buttonColorID = window.buttonColorInfoArray[2]
    window.buttonColorID[0].setStyleSheet(window.buttonColorID[1] + style.buttonColorActiveStyleSheet)

def colorIDBlack(window):
    window.buttonColorID[0].setStyleSheet(style.buttonColorStyleSheet + window.buttonColorID[1])
    window.buttonColorID = window.buttonColorInfoArray[3]
    window.buttonColorID[0].setStyleSheet(window.buttonColorID[1] + style.buttonColorActiveStyleSheet)

def colorIDWhite(window):
    window.buttonColorID[0].setStyleSheet(style.buttonColorStyleSheet + window.buttonColorID[1])
    window.buttonColorID = window.buttonColorInfoArray[4]
    window.buttonColorID[0].setStyleSheet(window.buttonColorID[1] + style.buttonColorActiveStyleSheet)

def clear(window):
    window.painter.fillRect(0, 0, 730, 590, window.colorBackground)
    window.update()