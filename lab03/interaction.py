import style as style

def methodIDDDA(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodDDA
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDBresenhamI(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodBresenhamInt
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDBresehamF(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodBresenhamFloat
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDBresenhamStg(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodBresenhamStg
    window.methodID.setStyleSheet(style.buttonMethodActiveStyleSheet)

def methodIDWU(window):
    window.methodID.setStyleSheet(style.buttonMethodStyleSheet)
    window.methodID = window.buttonMethodWU
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