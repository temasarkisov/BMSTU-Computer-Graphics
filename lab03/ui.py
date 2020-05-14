import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel, QRadioButton, QGraphicsView, QLineEdit, QGraphicsScene
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPen, QPainter, QColor, QBrush, QImage, QPixmap, QRgba64
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *

import style as style
import methods as methods
import interaction as interaction

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Beam Viewer")
        self.setStyleSheet("background-color: white")

        self._createPickerPannel()
        self._createLabels()
        self._createButtonsMethod()
        self._createButtonsColor()
        self._createLineEditXY()
        self._createLineEditBeam()
        self._createButtonsAction()
        self._createGraphics()

    def _createPickerPannel(self):
        self.pickerPannelBorder = QLabel(self)
        self.pickerPannel = QLabel(self)
        
        self.pickerPannel.setStyleSheet("background-color: #fcfcf2;"
                            "border-radius: 25px;"
                            "padding: 6px;")
        self.pickerPannel.setGeometry(70, 30, 300, 610)
        
        self.pickerPannelBorder.setStyleSheet("border-image: url(/Users/temasarkisov/BMSTU/labsCG/lab_03/auxiliary/labelBorder1.jpeg) 3 10 3 10;"
                            "border-radius: 27px;"
                            "padding: 6px;")
        self.pickerPannelBorder.setGeometry(67, 27, 306, 616)

    def _createLabels(self):
        self.labelMethod = QLabel(self)
        self.labelColor = QLabel(self)
        self.labelPointsCoordinates = QLabel(self)
        self.labelBeam = QLabel(self)
        self.labelTimeTaking = QLabel(self)
        self.labelTime = QLabel(self)

        self.labelMethod.setStyleSheet(style.labelStyleSheet)
        self.labelMethod.setText("METHOD")
        self.labelMethod.setGeometry(80, 50, 150, 35)

        self.labelColor.setStyleSheet(style.labelStyleSheet)
        self.labelColor.setText("COLOR")
        self.labelColor.setGeometry(80, 230, 150, 35)

        self.labelPointsCoordinates.setStyleSheet(style.labelStyleSheet)
        self.labelPointsCoordinates.setText("POINT'S COORDINATES")
        self.labelPointsCoordinates.setGeometry(80, 330, 170, 35)

        self.labelBeam.setStyleSheet(style.labelStyleSheet)
        self.labelBeam.setText("BEAM   (RADIUS, ANGLE)")
        self.labelBeam.setGeometry(80, 430, 180, 35)

        self.labelTimeTaking.setStyleSheet(style.labelStyleSheet)
        self.labelTimeTaking.setText("TIME TAKING")
        self.labelTimeTaking.setGeometry(80, 550, 105, 35)

        self.labelTime.setStyleSheet(style.lineEditStyleSheet)
        self.labelTime.setText("0.0 msc")
        self.labelTime.setGeometry(190, 550, 150, 35)

    def _createButtonsMethod(self):
        self.methodID = QPushButton()
        self.buttonMethodDDA = QPushButton(self)
        self.buttonMethodBresenhamInt = QPushButton(self)
        self.buttonMethodBresenhamFloat = QPushButton(self) 
        self.buttonMethodBresenhamStg = QPushButton(self) 
        self.buttonMethodWU = QPushButton(self) 
        self.buttonMethodLibrary = QPushButton(self)
        self.buttonMethodInfoArray = [[self.buttonMethodDDA, "DDA", 80, 90], 
                                      [self.buttonMethodBresenhamInt, "BRESENHAM (I)", 230, 90], 
                                      [self.buttonMethodBresenhamFloat, "BRESENHAM (F)", 230, 130], 
                                      [self.buttonMethodBresenhamStg, "BRESENHAM (STG)", 80, 130], 
                                      [self.buttonMethodWU, "WU", 80, 170], 
                                      [self.buttonMethodLibrary, "LIBRARY", 230, 170]]

        for buttonMethodInfo in self.buttonMethodInfoArray:
            buttonMethodInfo[0].setStyleSheet(style.buttonMethodStyleSheet)
            buttonMethodInfo[0].setText(buttonMethodInfo[1])
            buttonMethodInfo[0].setGeometry(buttonMethodInfo[2], buttonMethodInfo[3], 130, 35)
        
        self.buttonMethodDDA.clicked.connect(lambda: interaction.methodIDDDA(self))
        self.buttonMethodBresenhamInt.clicked.connect(lambda: interaction.methodIDBresenhamI(self))
        self.buttonMethodBresenhamFloat.clicked.connect(lambda: interaction.methodIDBresehamF(self))
        self.buttonMethodBresenhamStg.clicked.connect(lambda: interaction.methodIDBresenhamStg(self))
        self.buttonMethodWU.clicked.connect(lambda: interaction.methodIDWU(self))
        self.buttonMethodLibrary.clicked.connect(lambda: interaction.methodIDLib(self))

    def _createButtonsColor(self):
        self.buttonColorID = [QPushButton(), "", 0, 0, 0, 0, 0]
        self.buttonColorGreen = QPushButton(self)
        self.buttonColorBlue = QPushButton(self)
        self.buttonColorRed = QPushButton(self)
        self.buttonColorBlack = QPushButton(self)
        self.buttonColorWhite = QPushButton(self)
        self.buttonColorInfoArray = [[self.buttonColorGreen, "QPushButton { background-color: #86df83; }", 80, 270, 134, 223, 131],
                                     [self.buttonColorBlue, "QPushButton { background-color: #5e67c1; }", 120, 270, 94, 103, 193],
                                     [self.buttonColorRed, "QPushButton { background-color: #ab2b3f; }", 160, 270, 171, 43, 63],
                                     [self.buttonColorBlack, "QPushButton { background-color: #231f20; }", 200, 270, 35, 31, 32],
                                     [self.buttonColorWhite, "QPushButton { background-color: white; }\n" + "QPushButton { border-color: #aaaaaa; }", 240, 270, 255, 255, 255]]
                
        for buttonColorInfo in self.buttonColorInfoArray:
            buttonColorInfo[0].setStyleSheet(buttonColorInfo[1] + style.buttonColorStyleSheet)
            buttonColorInfo[0].setGeometry(buttonColorInfo[2], buttonColorInfo[3], 35, 35)

        self.buttonColorGreen.clicked.connect(lambda: interaction.colorIDGreen(self))
        self.buttonColorBlue.clicked.connect(lambda: interaction.colorIDBlue(self))
        self.buttonColorRed.clicked.connect(lambda: interaction.colorIDRed(self))
        self.buttonColorBlack.clicked.connect(lambda: interaction.colorIDBlack(self))
        self.buttonColorWhite.clicked.connect(lambda: interaction.colorIDWhite(self))

    def _createLineEditXY(self):
        self.lineEditXS = QLineEdit(self)
        self.lineEditYS = QLineEdit(self)
        self.lineEditXE = QLineEdit(self)
        self.lineEditYE = QLineEdit(self)
        self.lineEditXYInfoArray = [[self.lineEditXS, 80, 370], 
                        [self.lineEditYS, 130, 370],
                        [self.lineEditXE, 180, 370],
                        [self.lineEditYE, 230, 370]]
            
        for lineEditXYInfo in self.lineEditXYInfoArray:
            lineEditXYInfo[0].setStyleSheet(style.lineEditStyleSheet)
            lineEditXYInfo[0].setGeometry(lineEditXYInfo[1], lineEditXYInfo[2], 45, 35)

    def _createLineEditBeam(self):
        self.lineEditBeamRadius = QLineEdit(self)
        self.lineEditBeamAngle = QLineEdit(self)
        self.lineEditBeamInfoArray = [[self.lineEditBeamRadius, 80 , 470],
                                      [self.lineEditBeamAngle, 180, 470]]

        for lineEditBeamInfo in self.lineEditBeamInfoArray:
            lineEditBeamInfo[0].setStyleSheet(style.lineEditStyleSheet)
            lineEditBeamInfo[0].setGeometry(lineEditBeamInfo[1], lineEditBeamInfo[2], 90, 35)

    def _createButtonsAction(self):
        self.buttonDrawSection = QPushButton(self)
        self.buttonDrawBeam = QPushButton(self)
        self.buttonClear = QPushButton(self)

        self.buttonDrawSection.setStyleSheet(style.buttonActionStyleSheet)
        self.buttonDrawSection.setText("DRAW")
        self.buttonDrawSection.clicked.connect(lambda: methods.drawSection(self))
        self.buttonDrawSection.setGeometry(285, 370, 70, 35)

        self.buttonDrawBeam.setStyleSheet(style.buttonActionStyleSheet)
        self.buttonDrawBeam.setText("DRAW")
        self.buttonDrawBeam.clicked.connect(lambda: methods.drawBeam(self))
        self.buttonDrawBeam.setGeometry(285, 470, 70, 35)

        self.buttonClear.setStyleSheet(style.buttonActionStyleSheet)
        self.buttonClear.setText("CLEAR")
        self.buttonClear.clicked.connect(lambda: interaction.clear(self))
        self.buttonClear.setGeometry(80, 590, 100, 35)

    def _createGraphics(self):
        self.LabelForPaintBorder = QLabel(self)
        self.labelForPaint = QLabel(self)
        self.canvas = QPixmap(730, 590)
        self.color = QColor(255, 255, 255, 255)
        self.colorBackground = QColor(252, 252, 242, 255)
        self.canvas.fill(self.colorBackground)
        self.labelForPaint.setPixmap(self.canvas)
        self.painter = QPainter(self.labelForPaint.pixmap())
        
        self.LabelForPaintBorder.setStyleSheet("border-image: url(/Users/temasarkisov/BMSTU/labsCG/lab_03/auxiliary/viewBorder.jpeg);"
                            "border-radius: 27px;"
                            "padding: 6px;")
        self.LabelForPaintBorder.setGeometry(397, 27, 756, 616)

        self.labelForPaint.setStyleSheet("background-color: #fcfcf2;"
                        "border-radius: 25px;"
                        "padding: 6px;")    
        self.labelForPaint.setGeometry(400, 30, 750, 610)
        
def main():
    window = QApplication(sys.argv)
    view = Window()
    view.show()
    sys.exit(window.exec_())

if __name__ == '__main__':
    main()