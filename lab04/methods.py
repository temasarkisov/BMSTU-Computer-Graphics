from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QGraphicsView, QLineEdit, QGraphicsScene
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap, QRgba64
from PyQt5.QtCore import Qt
from math import sqrt, pi, cos, sin

import style as style

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def circle_canon(window, cx, cy, r):
    for x in range(0, r + 1, 1):
        y = round(sqrt(r ** 2 - x ** 2))
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)

    for y in range(0, r + 1, 1):
        x = round(sqrt(r ** 2 - y ** 2))

        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)
    
    window.update()

def circle_param(window, cx, cy, r):
    l = round(pi * r / 2 )  # длина четврети окружности
    for i in range(0, l + 1, 1):
        x = round(r * cos(i / r))
        y = round(r * sin(i / r))
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)
    
    window.update()

def circle_brez(window, cx, cy, r):
    x = 0   # задание начальных значений
    y = r
    d = 2 - 2 * r   # значение D(x,y)  при (0,R)
    while y >= 0:
        # высвечивание текущего пиксела
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)

        if d < 0:  # пиксель лежит внутри окружности
            buf = 2 * d + 2 * y - 1
            x += 1

            if buf <= 0:  # горизонтальный шаг
                d = d + 2 * x + 1
            else:  # диагональный шаг
                y -= 1
                d = d + 2 * x - 2 * y + 2

            continue

        if d > 0:  # пиксель лежит вне окружности
            buf = 2 * d - 2 * x - 1
            y -= 1

            if buf > 0:  # вертикальный шаг
                d = d - 2 * y + 1
            else:  # диагональный шаг
                x += 1
                d = d + 2 * x - 2 * y + 2

            continue

        if d == 0.0:  # пиксель лежит на окружности
            x += 1   # диагональный шаг
            y -= 1
            d = d + 2 * x - 2 * y + 2
        
    window.update()

def circle_middle(window, cx, cy, r):
    x = 0  # начальные значения
    y = r
    p = 5 / 4 - r  # (x + 1)^2 + (y - 1/2)^2 - r^2
    while True:
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy - y)
        window.painter.drawPoint(cx + x, cy + y)

        window.painter.drawPoint(cx - y, cy + x)
        window.painter.drawPoint(cx + y, cy - x)
        window.painter.drawPoint(cx - y, cy - x)
        window.painter.drawPoint(cx + y, cy + x)

        x += 1

        if p < 0:  # средняя точка внутри окружности, ближе верхний пиксел, горизонтальный шаг
            p += 2 * x + 1
        else:   # средняя точка вне окружности, ближе диагональный пиксел, диагональный шаг
            p += 2 * x - 2 * y + 5
            y -= 1

        if x > y:
            break
    
    window.update()

def ellips_canon(window, cx, cy, a, b):
    for x in range(0, a + 1, 1):
        y = round(b * sqrt(1.0 - x ** 2 / a / a))
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)

    for y in range(0, b + 1, 1):
        x = round(a * sqrt(1.0 - y ** 2 / b / b))
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)

    window.update()

def ellips_param(window, cx, cy, a, b):
    m = max(a, b)
    l = round(pi * m / 2)
    for i in range(0, l + 1, 1):
        x = round(a * cos(i / m))
        y = round(b * sin(i / m))
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)

    window.update()

def ellips_brez(window, cx, cy, a, b):
    x = 0  # начальные значения
    y = b
    a = a ** 2
    d = round(b * b / 2 - a * b * 2 + a / 2)
    b = b ** 2
    while y >= 0:
        window.painter.drawPoint(cx + x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx - x, cy - y)
        if d < 0:  # пиксель лежит внутри эллипса
            buf = 2 * d + 2 * a * y - a
            x += 1
            if buf <= 0:  # горизотальный шаг
                d = d + 2 * b * x + b
            else:  # диагональный шаг
                y -= 1
                d = d + 2 * b * x - 2 * a * y + a + b

            continue

        if d > 0:  # пиксель лежит вне эллипса
            buf = 2 * d - 2 * b * x - b
            y -= 1

            if buf > 0:  # вертикальный шаг
                d = d - 2 * y * a + a
            else:  # диагональный шаг
                x += 1
                d = d + 2 * x * b - 2 * y * a + a + b

            continue

        if d == 0.0:  # пиксель лежит на окружности
            x += 1  # диагональный шаг
            y -= 1
            d = d + 2 * x * b - 2 * y * a + a + b

    window.update()

def ellips_middle(window, cx, cy, a, b):
    x = 0   # начальные положения
    y = b
    p = b * b - a * a * b + 0.25 * a * a   # начальное значение параметра принятия решения в области tg<1
    while 2 * (b ** 2) * x < 2 * a * a * y:  # пока тангенс угла наклона меньше 1
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy - y)
        window.painter.drawPoint(cx + x, cy + y)

        x += 1

        if p < 0:  # средняя точка внутри эллипса, ближе верхний пиксел, горизонтальный шаг
            p += 2 * b * b * x + b * b
        else:   # средняя точка вне эллипса, ближе диагональный пиксел, диагональный шаг
            y -= 1
            p += 2 * b * b * x - 2 * a * a * y + b * b

    p = b * b * (x + 0.5) * (x + 0.5) + a * a * (y - 1) * (y - 1) - a * a * b * b
    # начальное значение параметра принятия решения в области tg>1 в точке (х + 0.5, y - 1) полседнего положения

    while y >= 0:
        window.painter.drawPoint(cx - x, cy + y)
        window.painter.drawPoint(cx + x, cy - y)
        window.painter.drawPoint(cx - x, cy - y)
        window.painter.drawPoint(cx + x, cy + y)

        y -= 1

        if p > 0:
            p -= 2 * a * a * y + a * a
        else:
            x += 1
            p += 2 * b * b * x - 2 * a * a * y + a * a
    
    window.update()

def drawShape(window):
    x = float(window.lineEditCenterX.text())
    y = float(window.lineEditCenterY.text())

    window.color = QColor(window.buttonColorID[4], window.buttonColorID[5], window.buttonColorID[6], 255)    
    window.painter.setPen(window.color)

    if window.shapeID == window.buttonShapeCircle:
        r = int(window.lineEditCircleRadius.text())

        if window.methodID == window.buttonMethodCanonicalEquation:
            circle_canon(window, x, y, r)
        
        if window.methodID == window.buttonMethodParametricEquation:
            circle_param(window, x, y, r)

        if window.methodID == window.buttonMethodBresenham:
            circle_brez(window, x, y, r)

        if window.methodID == window.buttonMethodMeanPoint:
            circle_middle(window, x, y, r)

        #if window.methodID == window.buttonMethodLibrary:

    if window.shapeID == window.buttonShapeOval:
        a = int(window.lineEditOvalA.text())
        b = int(window.lineEditOvalB.text())

        if window.methodID == window.buttonMethodCanonicalEquation:
            ellips_canon(window, x, y, a, b)

        if window.methodID == window.buttonMethodParametricEquation:
            ellips_param(window, x, y, a, b)
        
        if window.methodID == window.buttonMethodBresenham:
            ellips_brez(window, x, y, a, b)
        
        if window.methodID == window.buttonMethodMeanPoint:
            ellips_middle(window, x, y, a, b)
        
        #if window.methodID == window.buttonMethodLibrary:
    
def drawConcentrator(window):
    x = float(window.lineEditCenterX.text())
    y = float(window.lineEditCenterY.text())
    d = int(window.lineEditStep.text())
    c = int(window.lineEditNumber.text())

    window.color = QColor(window.buttonColorID[4], window.buttonColorID[5], window.buttonColorID[6], 255)    
    window.painter.setPen(window.color)

    if window.shapeID == window.buttonShapeCircle:
        for i in range(d, d * c + d, d):
            if window.methodID == window.buttonMethodCanonicalEquation:
                circle_canon(window, x, y, i)
            
            if window.methodID == window.buttonMethodParametricEquation:
                circle_param(window, x, y, i)

            if window.methodID == window.buttonMethodBresenham:
                circle_brez(window, x, y, i)

            if window.methodID == window.buttonMethodMeanPoint:
                circle_middle(window, x, y, i)

            #if window.methodID == window.buttonMethodLibrary:
    
    if window.shapeID == window.buttonShapeOval:
        for i in range(d, d * c + d, d):
            if window.methodID == window.buttonMethodCanonicalEquation:
                ellips_canon(window, x, y, i * 2, i)

            if window.methodID == window.buttonMethodParametricEquation:
                ellips_param(window, x, y, i * 2, i)
            
            if window.methodID == window.buttonMethodBresenham:
                ellips_brez(window, x, y, i * 2, i)
            
            if window.methodID == window.buttonMethodMeanPoint:
                ellips_middle(window, x, y, i * 2, i)
            
            #if window.methodID == window.buttonMethodLibrary:


        

