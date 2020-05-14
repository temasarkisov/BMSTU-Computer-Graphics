from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QGraphicsView, QLineEdit, QGraphicsScene
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap, QRgba64
from PyQt5.QtCore import Qt
from math import cos, sin, pi, radians, copysign, fabs

import numpy as np
from time import time

import style as style

def buttonClicked():
    print("Button clicked")

def sign(x):
    if x == 0:
        return 0
    else:
        return x/abs(x)

def sectionDDA(window, p1, p2):
    deltaX = abs(p1[0] - p2[0])
    deltaY = abs(p1[1] - p2[1])

    length = max(deltaX, deltaY)

    if length == 0:
        window.painter.drawPoint(p1[0], p1[1])
        window.update()
        return

    dX = (p2[0] - p1[0]) / length
    dY = (p2[1] - p1[1]) / length

    x = p1[0] + 0.5 * sign(dX)
    y = p1[1] + 0.5 * sign(dY)

    while length > 0:
        print(x, y)
        window.painter.drawPoint(x, y)
        x += dX
        y += dY
        length -= 1

    window.update()

def sectionBrasenhamI(window, p1, p2):
    if p1 == p2:
        window.painter.drawPoint(p1[0], p1[1])
        window.update()
        return

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    change = False

    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        change = True

    e = 2 * dy - dx
    i = 1
    while i <= dx:
        window.painter.drawPoint(x, y)
        if e >= 0:
            if change == 0:
                y += sy
            else:
                x += sx
            e -= 2 * dx

        if e < 0:
            if change == 0:
                x += sx
            else:
                y += sy
            e += (2 * dy)
        i += 1

    window.update()

def sectionBrasenhamF(window, p1, p2):
    if p1 == p2:
        window.painter.drawPoint(p1[0], p1[1])
        window.update()
        return

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True

    h = dy / dx

    e = h - 0.5
    i = 1
    while i <= dx:
        window.painter.drawPoint(x, y)
        if e >= 0:
            if change is False:
                y += sy
            else:
                x += sx
            e -= 1

        if e < 0:
            if change is False:
                x += sx
            else:
                y += sy
            e += h
        i+=1

    window.update()

def sectionBrasenhamStg(window, p1, p2):
    if p1 == p2:
        window.painter.drawPoint(p1[0], p1[1])
        return

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    try:
        h = dy / dx
    except ZeroDivisionError:
        h = 0

    i_max = 256

    change = False

    if dy > dx:
        dx, dy = dy, dx
        change = True
        if h:
            h = 1 / h

    h *= i_max
    e = i_max/2
    w = i_max - h
    i = 1
    while i <= dx:
        window.painter.drawPoint(x, y)
        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += h
        else:
            x += sx
            y += sy
            e -= w
        i += 1

    window.update()

def sectionWU(window, p1, p2):
    if p1 == p2:
        window.painter.drawPoint(p1[0], p1[1])
        window.update()
        return

    xb = p1[0]
    yb = p1[1]
    xe = p2[0]
    ye = p2[1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    i_max = 256

    change = abs(dx) < abs(dy)

    if change:
        xb, yb, xe, ye, dx, dy = yb, xb, ye, xe, dy, dx

    if xe < xb:
        xb, xe, yb, ye = xe, xb, ye, yb

    grad = 0
    if dy != 0:
        grad = dy / dx

    y = yb
    x = xb

    while x <= xe:
        if change:
            s = sign(y)
            window.painter.drawPoint(y, x)

            if dy and dx:
                window.painter.drawPoint(y, x)

            window.painter.drawPoint(y + s, x)

        else:
            s = sign(y)
            window.painter.drawPoint(x, y)

            if dy and dx:
                window.painter.drawPoint(x, y)

            window.painter.drawPoint(x, y + s)
        y += grad
        x += 1

    window.update()

def sectionLibrary(window, p1, p2):
    window.painter.drawLine(p1[0], p1[1], p2[0], p2[1])
    window.update()

def drawSection(window):
    xs = float(window.lineEditXS.text())
    ys = float(window.lineEditYS.text())
    xe = float(window.lineEditXE.text())
    ye = float(window.lineEditYE.text())

    window.color = QColor(window.buttonColorID[4], window.buttonColorID[5], window.buttonColorID[6], 255)    
    window.painter.setPen(window.color)

    if window.methodID == window.buttonMethodDDA:
        print("DDA method confirm.")
        start = time()
        sectionDDA(window, [xs, ys], [xe, ye])
        end = time()
    
    if window.methodID == window.buttonMethodBresenhamInt:
        print("Bresenham int method confirm.")
        start = time()
        sectionBrasenhamI(window, [xs, ys], [xe, ye])
        end = time()

    if window.methodID == window.buttonMethodBresenhamFloat:
        print("Bresenham float method confirm.")
        start = time()
        sectionBrasenhamF(window, [xs, ys], [xe, ye])
        end = time()

    if window.methodID == window.buttonMethodBresenhamStg:
        print("Bresenham stg method confirm.")
        start = time()
        sectionBrasenhamStg(window, [xs, ys], [xe, ye])
        end = time()

    if window.methodID == window.buttonMethodWU:
        print("Bresenham stg method confirm.")
        start = time()
        sectionWU(window, [xs, ys], [xe, ye])
        end = time()

    if window.methodID == window.buttonMethodLibrary:
        start = time()
        sectionLibrary(window, [xs, ys], [xe, ye])
        end = time()

    window.labelTime.setText("{0:.3f} msc".format((end - start) * 1000))

def drawBeam(window):
    r = float(window.lineEditBeamRadius.text())
    spin = float(window.lineEditBeamAngle.text())
    
    xs = 365
    ys = 295
    
    window.color = QColor(window.buttonColorID[4], window.buttonColorID[5], window.buttonColorID[6], 255)    
    window.painter.setPen(window.color)

    for i in np.arange(0, 360, spin):
        xe = cos(radians(i)) * 2 * r + 255
        ye = sin(radians(i)) * 2 * r + 255

        if window.methodID == window.buttonMethodDDA:
            print("DDA method confirm.")
            start = time()
            sectionDDA(window, [xs, ys], [xe, ye])
            end = time()
        
        if window.methodID == window.buttonMethodBresenhamInt:
            print("Bresenham int method confirm.")
            start = time()
            sectionBrasenhamI(window, [xs, ys], [xe, ye])
            end = time()

        if window.methodID == window.buttonMethodBresenhamFloat:
            print("Bresenham float method confirm.")
            start = time()
            sectionBrasenhamF(window, [xs, ys], [xe, ye])
            end = time()

        if window.methodID == window.buttonMethodBresenhamStg:
            print("Bresenham stg method confirm.")
            start = time()
            sectionBrasenhamStg(window, [xs, ys], [xe, ye])
            end = time()

        if window.methodID == window.buttonMethodWU:
            print("WU method confirm.")
            start = time()
            sectionWU(window, [xs, ys], [xe, ye])
            end = time()

        if window.methodID == window.buttonMethodLibrary:
            print("Library method confirm.")
            start = time()
            sectionLibrary(window, [xs, ys], [xe, ye])
            end = time()
    
    window.labelTime.setText("{0:.3f} msc".format((end - start) * 1000))