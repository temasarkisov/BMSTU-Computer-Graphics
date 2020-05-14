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
        self.setWindowTitle("2D Viewer")
        self.setStyleSheet("background-color: white")

        self._createPickerPannel()
        self._createLabels()
        self._createButtonsShape()
        self._createButtonsMethod()
        self._createButtonsColor()
        self._createlineEditCenter()
        self._createLineEditCircleRadius()
        self._createLineEditOvalAB()
        self._createLineEditStepNumber()
        self._createButtonsAction()
        self._createGraphics()

    def _createPickerPannel(self):
        self.pickerPannelBorder = QLabel(self)
        self.pickerPannel = QLabel(self)
        self.pickerPannelColor = QLabel(self)
        
        self.pickerPannel.setStyleSheet("background-color: #ffcccc;"
                            "border-radius: 25px;"
                            "padding: 6px;")
        self.pickerPannel.setGeometry(70, 30, 300, 610)
        
        self.pickerPannelBorder.setStyleSheet("background-color: #ff9f1a;"
                            "border-radius: 27px;"
                            "padding: 6px;")
        self.pickerPannelBorder.setGeometry(67, 27, 306, 616)

        self.pickerPannelColor.setStyleSheet("background-color: #ffcccc;" 
                            "border-style: solid;" 
                            "border-width: 2px;"
                            "border-radius: 25px;" 
                            "border-color: #ff9f1a;"
                            "padding: 6px;")
        self.pickerPannelColor.setGeometry(10, 30, 51, 220)

    def _createLabels(self):
        self.labelShape = QLabel(self)
        self.labelMethod = QLabel(self)
        self.labelCenter = QLabel(self)
        self.labelCircleRadius = QLabel(self)
        self.labelOvalAB = QLabel(self)
        self.labelStep = QLabel(self)
        self.labelNumber = QLabel(self)

        self.labelShape.setStyleSheet(style.labelStyleSheet)
        self.labelShape.setText("SHAPE")
        self.labelShape.setGeometry(80, 50, 280, 35)

        self.labelMethod.setStyleSheet(style.labelStyleSheet)
        self.labelMethod.setText("METHOD")
        self.labelMethod.setGeometry(80, 130, 280, 35)

        self.labelCenter.setStyleSheet(style.labelStyleSheet)
        self.labelCenter.setText("CENTER")
        self.labelCenter.setGeometry(80, 290, 71, 35)

        self.labelCircleRadius.setStyleSheet(style.labelStyleSheet)
        self.labelCircleRadius.setText("CIRCLE (RADIUS)")
        self.labelCircleRadius.setGeometry(80, 330, 130, 35)

        self.labelOvalAB.setStyleSheet(style.labelStyleSheet)
        self.labelOvalAB.setText("OVAL (A, B")
        self.labelOvalAB.setGeometry(80, 370, 90, 35)

        self.labelStep.setStyleSheet(style.labelStyleSheet)
        self.labelStep.setText("STEP")
        self.labelStep.setGeometry(80, 450, 52, 35)

        self.labelNumber.setStyleSheet(style.labelStyleSheet)
        self.labelNumber.setText("NUMBER")
        self.labelNumber.setGeometry(80, 490, 75, 35)

    def _createButtonsShape(self):
        self.shapeID = QPushButton()
        self.buttonShapeCircle = QPushButton(self)
        self.buttonShapeOval = QPushButton(self)
        self.buttonShapeInfoArray = [[self.buttonShapeCircle, "CIRCLE", 80, 90], 
                                [self.buttonShapeOval, "OVAL", 230, 90]]

        for buttonShapeInfo in self.buttonShapeInfoArray:
            buttonShapeInfo[0].setStyleSheet(style.buttonMethodStyleSheet)
            buttonShapeInfo[0].setText(buttonShapeInfo[1])
            buttonShapeInfo[0].setGeometry(buttonShapeInfo[2], buttonShapeInfo[3], 130, 35)
        
        self.buttonShapeCircle.clicked.connect(lambda: interaction.shapeIDCircle(self))
        self.buttonShapeOval.clicked.connect(lambda: interaction.shapeIDOval(self))

    def _createButtonsMethod(self):
        self.methodID = QPushButton()
        self.buttonMethodCanonicalEquation = QPushButton(self)
        self.buttonMethodParametricEquation = QPushButton(self)
        self.buttonMethodBresenham = QPushButton(self) 
        self.buttonMethodMeanPoint = QPushButton(self) 
        self.buttonMethodLibrary = QPushButton(self)
        self.buttonMethodInfoArray = [[self.buttonMethodCanonicalEquation, "CANONICAL EQ.", 80, 170], 
                                      [self.buttonMethodParametricEquation, "PARAMETRIC EQ.", 230, 170], 
                                      [self.buttonMethodBresenham, "BRESENHAM", 230, 210], 
                                      [self.buttonMethodMeanPoint, "MEAN POINT", 80, 210], 
                                      [self.buttonMethodLibrary, "LIBRARY", 80, 250]]

        for buttonMethodInfo in self.buttonMethodInfoArray:
            buttonMethodInfo[0].setStyleSheet(style.buttonMethodStyleSheet)
            buttonMethodInfo[0].setText(buttonMethodInfo[1])
            buttonMethodInfo[0].setGeometry(buttonMethodInfo[2], buttonMethodInfo[3], 130, 35)
        
        self.buttonMethodCanonicalEquation.clicked.connect(lambda: interaction.methodIDCanonicalEquation(self))
        self.buttonMethodParametricEquation.clicked.connect(lambda: interaction.methodIDParametricEquation(self))
        self.buttonMethodBresenham.clicked.connect(lambda: interaction.methodIDBreseham(self))
        self.buttonMethodMeanPoint.clicked.connect(lambda: interaction.methodIDMeanPoint(self))
        self.buttonMethodLibrary.clicked.connect(lambda: interaction.methodIDLib(self))

    def _createButtonsColor(self):
        self.buttonColorID = [QPushButton(), "", 0, 0, 0, 0, 0]
        self.buttonColorGreen = QPushButton(self)
        self.buttonColorBlue = QPushButton(self)
        self.buttonColorRed = QPushButton(self)
        self.buttonColorBlack = QPushButton(self)
        self.buttonColorWhite = QPushButton(self)
        self.buttonColorInfoArray = [[self.buttonColorGreen, "QPushButton { background-color: #86df83; }", 18, 40, 134, 223, 131],
                                     [self.buttonColorBlue, "QPushButton { background-color: #5e67c1; }", 18, 80, 94, 103, 193],
                                     [self.buttonColorRed, "QPushButton { background-color: #ab2b3f; }", 18, 120, 171, 43, 63],
                                     [self.buttonColorBlack, "QPushButton { background-color: #231f20; }", 18, 160, 35, 31, 32],
                                     [self.buttonColorWhite, "QPushButton { background-color: white; }\n" + "QPushButton { border-color: #aaaaaa; }", 18, 200, 255, 255, 255]]
                
        for buttonColorInfo in self.buttonColorInfoArray:
            buttonColorInfo[0].setStyleSheet(buttonColorInfo[1] + style.buttonColorStyleSheet)
            buttonColorInfo[0].setGeometry(buttonColorInfo[2], buttonColorInfo[3], 35, 35)

        self.buttonColorGreen.clicked.connect(lambda: interaction.colorIDGreen(self))
        self.buttonColorBlue.clicked.connect(lambda: interaction.colorIDBlue(self))
        self.buttonColorRed.clicked.connect(lambda: interaction.colorIDRed(self))
        self.buttonColorBlack.clicked.connect(lambda: interaction.colorIDBlack(self))
        self.buttonColorWhite.clicked.connect(lambda: interaction.colorIDWhite(self))

    def _createlineEditCenter(self):
        self.lineEditCenterX = QLineEdit(self)
        self.lineEditCenterY = QLineEdit(self)
        self.lineEditCenterInfoArray = [[self.lineEditCenterX, 161, 290], 
                                        [self.lineEditCenterY, 211, 290]]
            
        for lineEditCenterInfo in self.lineEditCenterInfoArray:
            lineEditCenterInfo[0].setStyleSheet(style.lineEditStyleSheet)
            lineEditCenterInfo[0].setGeometry(lineEditCenterInfo[1], lineEditCenterInfo[2], 45, 35)

    def _createLineEditCircleRadius(self):
        self.lineEditCircleRadius = QLineEdit(self)
        self.lineEditCircleRadiusInfoArray = [[self.lineEditCircleRadius, 220 , 330]]

        for lineEditCircleRadiusInfo in self.lineEditCircleRadiusInfoArray:
            lineEditCircleRadiusInfo[0].setStyleSheet(style.lineEditStyleSheet)
            lineEditCircleRadiusInfo[0].setGeometry(lineEditCircleRadiusInfo[1], lineEditCircleRadiusInfo[2], 45, 35)

    def _createLineEditOvalAB(self):
        self.lineEditOvalA = QLineEdit(self)
        self.lineEditOvalB = QLineEdit(self)
        self.lineEditOvalABInfoArray = [[self.lineEditOvalA, 180, 370], 
                                        [self.lineEditOvalB, 230, 370]]

        for lineEditOvalInfo in self.lineEditOvalABInfoArray:
            lineEditOvalInfo[0].setStyleSheet(style.lineEditStyleSheet)
            lineEditOvalInfo[0].setGeometry(lineEditOvalInfo[1], lineEditOvalInfo[2], 45, 35)

    def _createLineEditStepNumber(self):
        self.lineEditStep = QLineEdit(self)
        self.lineEditNumber = QLineEdit(self)
        self.lineEditStepNumberInfoArray = [[self.lineEditStep, 142, 450], 
                                   [self.lineEditNumber, 165, 490]]

        for lineEditStepNumberInfo in self.lineEditStepNumberInfoArray:
            lineEditStepNumberInfo[0].setStyleSheet(style.lineEditStyleSheet)
            lineEditStepNumberInfo[0].setGeometry(lineEditStepNumberInfo[1], lineEditStepNumberInfo[2], 45, 35)


    def _createButtonsAction(self):
        self.buttonDrawCircleOval = QPushButton(self)
        self.buttonClear = QPushButton(self)
        self.buttonConcentrator = QPushButton(self)

        self.buttonDrawCircleOval.setStyleSheet(style.buttonActionStyleSheet)
        self.buttonDrawCircleOval.setText("DRAW SHAPE")
        self.buttonDrawCircleOval.clicked.connect(lambda: methods.drawShape(self))
        self.buttonDrawCircleOval.setGeometry(80, 410, 130, 35)

        self.buttonConcentrator.setStyleSheet(style.buttonActionStyleSheet)
        self.buttonConcentrator.setText("CONCENTRATOR")
        self.buttonConcentrator.clicked.connect(lambda: methods.drawConcentrator(self))
        self.buttonConcentrator.setGeometry(80, 530, 130, 35)

        self.buttonClear.setStyleSheet(style.buttonActionStyleSheet)
        self.buttonClear.setText("CLEAR")
        self.buttonClear.clicked.connect(lambda: interaction.clear(self))
        self.buttonClear.setGeometry(80, 590, 100, 35)

    def _createGraphics(self):
        self.LabelForPaintBorder = QLabel(self)
        self.labelForPaint = QLabel(self)
        self.canvas = QPixmap(730, 590)
        self.color = QColor(255, 255, 255, 255)
        self.colorBackground = QColor(255, 204, 204, 255)
        self.canvas.fill(self.colorBackground)
        self.labelForPaint.setPixmap(self.canvas)
        self.painter = QPainter(self.labelForPaint.pixmap())
        
        self.LabelForPaintBorder.setStyleSheet("background-color: #ff9f1a;"
                            "border-radius: 27px;"
                            "padding: 6px;")
        self.LabelForPaintBorder.setGeometry(397, 27, 756, 616)

        self.labelForPaint.setStyleSheet("background-color: #ffcccc;"
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