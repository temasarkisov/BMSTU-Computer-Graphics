def window():
    app = QApplication(sys.argv)
    widget = QWidget()
   
    graphicsViewBorder = QGraphicsView(widget)
    graphicsView = QGraphicsView(widget)
    scene = QGraphicsScene(400, 30, 730, 590, widget)
    image = QImage(511, 511, QImage.Format_ARGB32_Premultiplied)

    labelBorder = QLabel(widget)
    label = QLabel(widget)

    labelMethod = QLabel(widget)
    buttonMethodDDA = QPushButton(widget)
    buttonMethodBresenhamInt = QPushButton(widget)
    buttonMethodBresenhamFloat = QPushButton(widget) 
    buttonMethodBresenhamStg = QPushButton(widget) 
    buttonMethodWU = QPushButton(widget) 
    buttonMethodLibrary = QPushButton(widget)
    buttonMethodInfoArray = [[buttonMethodDDA, "DDA", 80, 90, methods.buttonMethodCDA_clicked], 
                        [buttonMethodBresenhamInt, "BRESENHAM (I)", 230, 90, methods.buttonMethodCDA_clicked], 
                        [buttonMethodBresenhamFloat, "BRESENHAM (F)", 230, 130, methods.buttonMethodCDA_clicked], 
                        [buttonMethodBresenhamStg, "BRESENHAM (STG)", 80, 130, methods.buttonMethodCDA_clicked], 
                        [buttonMethodWU, "WU", 80, 170, methods.buttonMethodCDA_clicked], 
                        [buttonMethodLibrary, "LIBRARY", 230, 170, methods.buttonMethodCDA_clicked]]
    
    labelColor = QLabel(widget)
    buttonColorGreen = QPushButton(widget)
    buttonColorBlue = QPushButton(widget)
    buttonColorRed = QPushButton(widget)
    buttonColorBlack = QPushButton(widget)
    buttonColorWhite = QPushButton(widget)
    buttonColorInfoArray = [[buttonColorGreen, "QPushButton { background-color: #86df83; }", 80, 270, methods.buttonMethodCDA_clicked],
                            [buttonColorBlue, "QPushButton { background-color: #5e67c1; }", 120, 270, methods.buttonMethodCDA_clicked],
                            [buttonColorRed, "QPushButton { background-color: #ab2b3f; }", 160, 270, methods.buttonMethodCDA_clicked],
                            [buttonColorBlack, "QPushButton { background-color: #231f20; }", 200, 270, methods.buttonMethodCDA_clicked],
                            [buttonColorWhite, "QPushButton { background-color: white; }\n" + "QPushButton { border-color: #aaaaaa; }", 240, 270, methods.buttonMethodCDA_clicked]]

    
    labelPointsCoordinates = QLabel(widget)
    lineEditXN = QLineEdit(widget)
    lineEditYN = QLineEdit(widget)
    lineEditXK = QLineEdit(widget)
    lineEditYK = QLineEdit(widget)
    lineEditXYInfoArray = [[lineEditXN, 80, 370], 
                       [lineEditYN, 130, 370],
                       [lineEditXK, 180, 370],
                       [lineEditYK, 230, 370]]
    buttonDrawSection = QPushButton(widget)

    labelBeam = QLabel(widget)
    lineEditBeamRadius = QLineEdit(widget)
    lineEditBeamAngle = QLineEdit(widget)
    lineEditBeamInfoArray = [[lineEditBeamRadius, 80 , 470],
                             [lineEditBeamAngle, 180, 470]]
    buttonDrawBeam = QPushButton(widget)

    buttonCompare = QPushButton(widget)
    buttonClean = QPushButton(widget)


    label.setStyleSheet("background-color: #fcfcf2;"
                        "border-radius: 25px;"
                        "padding: 6px;")
    label.setGeometry(70, 30, 300, 610)
    
    labelBorder.setStyleSheet("border-image: url(/Users/temasarkisov/BMSTU/labsCG/lab_03/labelBorder1.jpeg) 3 10 3 10;"
                        "border-radius: 27px;"
                        "padding: 6px;")
    labelBorder.setGeometry(67, 27, 306, 616)

    

    labelMethod.setStyleSheet(style.labelStyleSheet)
    labelMethod.setText("METHOD")
    labelMethod.setGeometry(80, 50, 150, 35)

    labelColor.setStyleSheet(style.labelStyleSheet)
    labelColor.setText("COLOR")
    labelColor.setGeometry(80, 230, 150, 35)

    labelPointsCoordinates.setStyleSheet(style.labelStyleSheet)
    labelPointsCoordinates.setText("POINT'S COORDINATES")
    labelPointsCoordinates.setGeometry(80, 330, 170, 35)

    labelBeam.setStyleSheet(style.labelStyleSheet)
    labelBeam.setText("BEAM   (RADIUS, ANGLE)")
    labelBeam.setGeometry(80, 430, 180, 35)



    for buttonMethodInfo in buttonMethodInfoArray:
        buttonMethodInfo[0].setStyleSheet(style.buttonMethodStyleSheet)
        buttonMethodInfo[0].setText(buttonMethodInfo[1])
        buttonMethodInfo[0].clicked.connect(buttonMethodInfo[4])
        buttonMethodInfo[0].setGeometry(buttonMethodInfo[2], buttonMethodInfo[3], 130, 35)
    
    for buttonColorInfo in buttonColorInfoArray:
        buttonColorInfo[0].setStyleSheet(buttonColorInfo[1] + style.buttonColorStyleSheet)
        buttonColorInfo[0].clicked.connect(buttonColorInfo[4])
        buttonColorInfo[0].setGeometry(buttonColorInfo[2], buttonColorInfo[3], 35, 35)
    
    for lineEditXYInfo in lineEditXYInfoArray:
        lineEditXYInfo[0].setStyleSheet(style.lineEditStyleSheet)
        lineEditXYInfo[0].setGeometry(lineEditXYInfo[1], lineEditXYInfo[2], 40, 35)

    for lineEditBeamInfo in lineEditBeamInfoArray:
        lineEditBeamInfo[0].setStyleSheet(style.lineEditStyleSheet)
        lineEditBeamInfo[0].setGeometry(lineEditBeamInfo[1], lineEditBeamInfo[2], 90, 35)

    buttonDrawSection.setStyleSheet(style.buttonActionStyleSheet)
    buttonDrawSection.setText("DRAW")
    buttonDrawSection.clicked.connect(methods.buttonMethodCDA_clicked)
    buttonDrawSection.setGeometry(285, 370, 70, 35)

    buttonDrawBeam.setStyleSheet(style.buttonActionStyleSheet)
    buttonDrawBeam.setText("DRAW")
    buttonDrawBeam.clicked.connect(methods.buttonMethodCDA_clicked)
    buttonDrawBeam.setGeometry(285, 470, 70, 35)

    buttonCompare.setStyleSheet(style.buttonActionStyleSheet)
    buttonCompare.setText("COMPARE METHODS")
    buttonCompare.clicked.connect(methods.buttonMethodCDA_clicked)
    buttonCompare.setGeometry(80, 550, 200, 35)

    buttonClean.setStyleSheet(style.buttonActionStyleSheet)
    buttonClean.setText("CLEAN")
    buttonClean.clicked.connect(methods.buttonMethodCDA_clicked)
    buttonClean.setGeometry(80, 590, 100, 35)



    graphicsViewBorder.setStyleSheet("border-image: url(/Users/temasarkisov/BMSTU/labsCG/lab_03/viewBorder.jpeg);"
                        "border-radius: 27px;"
                        "padding: 6px;")
    graphicsViewBorder.setGeometry(397, 27, 756, 616)

    graphicsView.setStyleSheet("background-color: #fcfcf2;"
                    "border-radius: 25px;"
                    "padding: 6px;")    
    graphicsView.setGeometry(400, 30, 750, 610)
    graphicsView.setScene(scene)


    widget.setGeometry(50, 50, 1200, 700)
    widget.setWindowTitle("2D view")
    widget.setStyleSheet("background-color: white")
    widget.show()
    sys.exit(app.exec_())
   
if __name__ == '__main__':
    window()
