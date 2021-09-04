from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import cv2 as cv
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QApplication, QDialog, QFileDialog, QGridLayout,
                             QLabel, QPushButton)
fname=''

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 596)
        self.center()  # Center the window
        self.setWindowTitle("PONS TECH IMAGE")
        self.setWindowIcon(QIcon('pin.jpg'))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 281, 281))
        self.groupBox.setObjectName("groupBox")
        self.btn1 = QtWidgets.QPushButton(self.groupBox)
        self.btn1.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.open)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 261, 231))
        self.label.setText("")
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 289, 281, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn3 = QtWidgets.QPushButton(self.groupBox_3)
        self.btn3.setGeometry(QtCore.QRect(190, 10, 71, 23))
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(self.PONS_LAB)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 41, 261, 231))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(80, 10, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.currentTextChanged.connect(self.pons_combo)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 0, 281, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btn2.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.OG_PONS)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 41, 261, 231))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(310, 290, 281, 281))
        self.groupBox_4.setObjectName("groupBox_4")
        self.btn4 = QtWidgets.QPushButton(self.groupBox_4)
        self.btn4.setGeometry(QtCore.QRect(110, 10, 75, 23))
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(self.phase_PONS)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(10, 41, 261, 231))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(500, 10, 80, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(500, 300, 80, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        
        self.horizontalSlider.valueChanged['int'].connect(self.SliderVal)
        self.horizontalSlider_2.valueChanged['int'].connect(self.SliderVal_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PONS Tech"))
        self.groupBox.setTitle(_translate("Form", "Original image"))
        self.btn1.setText(_translate("Form", "Start"))
        self.groupBox_3.setTitle(_translate("Form", "Image enhancement"))
        self.btn3.setText(_translate("Form", "Apply"))
        self.comboBox.setItemText(0, _translate("Form", "Logarithmic transformation"))
        self.comboBox.setItemText(1, _translate("Form", "Non-linear transformation"))
        self.comboBox.setItemText(2, _translate("Form", "Gamma transform"))
        self.comboBox.setItemText(3, _translate("Form", "Histogram equalization"))
        self.comboBox.setItemText(4, _translate("Form", "Restricted equilibrium"))
        self.groupBox_2.setTitle(_translate("Form", "LPF"))
        self.btn2.setText(_translate("Form", "Apply"))
        self.groupBox_4.setTitle(_translate("Form", "Phase Symmetry"))
        self.btn4.setText(_translate("Form", "Apply"))

    def open(self):
        global fname
        global one
        global two
        QMessageBox.question(self, 'Reminder', 'Select the image path',
                             QMessageBox.Ok)
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open picture", "", "*;;*.png;;All Files(*)")
        # jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        # self.label.setPixmap(QPixmap(jpg))
        # self.label2.setPixmap(QPixmap(jpg))

        image = cv.imread(imgName)
        if image is None:
            print("No picture selected")
        else:
            size = (int(self.label.width()), int(self.label.height()))
            shrink = cv.resize(image, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1]*3,
                                      QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            #self.label2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))
            fname = imgName
            print(imgName)
            one = 50
            two = 50


    def OG_PONS(self):
        global fname
        image = cv.imread(fname)
        if image is None:
            print("No picture selected")
        else:
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            image = cv.blur(image,(5,5))
            size = (int(self.label_2.width()), int(self.label_2.height()))
            shrink = cv.resize(image, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1]*3,
                                      QtGui.QImage.Format_RGB888)
            self.label_2.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))


    def phase_PONS(self):
        global fname
        image = cv.imread(fname)
        if image is None:
            print("No picture selected")
        else:
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            ret, binary = cv.threshold(image, 0, 255, cv.THRESH_OTSU | cv.THRESH_BINARY)
            print("The threshold is:", ret)
            size = (int(self.label_4.width()), int(self.label_4.height()))
            shrink = cv.resize(binary, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                      shrink.shape[1],
                                      shrink.shape[0],
                                      shrink.shape[1]*3,
                                      QtGui.QImage.Format_RGB888)
            self.label_4.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def SliderVal(self,value):
        """ This function will take value from the slider
        for the LPF from 0 to 99
        """
        self.sliderval_now = value
        print('LPF: ',value)
        self.update()

    def SliderVal_2(self,value):
        """ This function will take value from the slider
        for the LPF from 0 to 99
        """
        self.sliderval2_now = value
        print('Phase: ',value)
        self.update()
        


    def PONS_LAB(self):
        global fname
        image = cv.imread(fname)
        if image is None:
            print("No picture selected")
        else:
            if self.str == 'Gamma transform':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                def gamma(img, c, v):
                    lut = np.zeros(256, dtype=np.float32)
                    for i in range(256):
                        lut[i] = c * i ** v
                    output_img = cv.LUT(img, lut)  # Pixel gray value mapping
                    output_img = np.uint8(output_img + 0.5)
                    return output_img
                out_put = gamma(image,0.0000005,4)
                out_image = out_put

            if self.str =='Non-linear transformation':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                height = image.shape[0]
                width = image.shape[1]
                result = np.zeros((height,width),np.uint8)
                for i in range(height):
                    for j in range(width):
                        gray = int(image[i, j]) * int(image[i, j]) / 255
                        result[i, j] = np.uint8(gray)
                out_image = result

            if self.str =='Logarithmic transformation':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                def log(c,img):
                    out_put = c*np.log(1.0+img)
                    out_put = np.uint8(out_put+0.5)
                    return out_put
                out_image = log(42,image)
            if self.str =='Histogram equalization':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                out_image = cv.equalizeHist(image)

            if self.str =='Restricted equilibrium':
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
                out_image = clahe.apply(image)


            size = (int(self.label_3.width()), int(self.label_3.height()))
            shrink = cv.resize(out_image, size, interpolation=cv.INTER_AREA)
            shrink = cv.cvtColor(shrink, cv.COLOR_BGR2RGB)
            self.QtImg = QtGui.QImage(shrink.data,
                                    shrink.shape[1],
                                    shrink.shape[0],
                                    shrink.shape[1] * 3,
                                    QtGui.QImage.Format_RGB888)
            self.label_3.setPixmap(QtGui.QPixmap.fromImage(self.QtImg))

    def pons_combo(self):
        self.str = self.comboBox.currentText()
        print(self.str)




    def center(self):  # Method of controlling window display in the center of the screen

        # Get window
        qr = self.frameGeometry()
        # Get the center point of the screen
        cp = QDesktopWidget().availableGeometry().center()
        # Show to the center of the screen
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload =  Ui_Form()
    fileload.show()
    sys.exit(app.exec_())
