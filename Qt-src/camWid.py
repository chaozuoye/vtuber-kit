# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camWid.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(980, 723)
        self.camerashow = QtWidgets.QLabel(Form)
        self.camerashow.setGeometry(QtCore.QRect(40, 50, 640, 480))
        self.camerashow.setObjectName("camerashow")
        self.button_openCam = QtWidgets.QPushButton(Form)
        self.button_openCam.setGeometry(QtCore.QRect(50, 560, 111, 41))
        self.button_openCam.setObjectName("button_openCam")
        self.button_shoot = QtWidgets.QPushButton(Form)
        self.button_shoot.setGeometry(QtCore.QRect(50, 630, 111, 41))
        self.button_shoot.setObjectName("button_shoot")
        self.button_back = QtWidgets.QPushButton(Form)
        self.button_back.setGeometry(QtCore.QRect(180, 630, 111, 41))
        self.button_back.setObjectName("button_back")
        self.button_confrim = QtWidgets.QPushButton(Form)
        self.button_confrim.setGeometry(QtCore.QRect(310, 630, 111, 41))
        self.button_confrim.setObjectName("button_confrim")
        self.label_guide = QtWidgets.QLabel(Form)
        self.label_guide.setGeometry(QtCore.QRect(700, 40, 251, 71))
        self.label_guide.setObjectName("label_guide")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(180, 570, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_step1 = QtWidgets.QLabel(Form)
        self.label_step1.setGeometry(QtCore.QRect(700, 90, 251, 41))
        self.label_step1.setObjectName("label_step1")
        self.label_step2 = QtWidgets.QLabel(Form)
        self.label_step2.setGeometry(QtCore.QRect(700, 120, 251, 41))
        self.label_step2.setObjectName("label_step2")
        self.label_step3 = QtWidgets.QLabel(Form)
        self.label_step3.setGeometry(QtCore.QRect(700, 150, 251, 41))
        self.label_step3.setObjectName("label_step3")
        self.label_openImg = QtWidgets.QLabel(Form)
        self.label_openImg.setGeometry(QtCore.QRect(700, 210, 224, 168))
        self.label_openImg.setObjectName("label_openImg")
        self.label_closeImg = QtWidgets.QLabel(Form)
        self.label_closeImg.setGeometry(QtCore.QRect(700, 400, 224, 168))
        self.label_closeImg.setObjectName("label_closeImg")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "动作采集"))
        self.camerashow.setText(_translate("Form", "【摄像机未打开】"))
        self.button_openCam.setText(_translate("Form", "打开摄像头"))
        self.button_shoot.setText(_translate("Form", "拍摄照片"))
        self.button_back.setText(_translate("Form", "返回上一步"))
        self.button_confrim.setText(_translate("Form", "完成"))
        self.label_guide.setText(_translate("Form", "打开摄像头后，请按照以下顺序操作:"))
        self.label_step1.setText(_translate("Form", "1.张开眼睛和嘴巴，点击拍摄照片"))
        self.label_step2.setText(_translate("Form", "2.闭上眼睛和嘴巴，点击拍摄照片"))
        self.label_step3.setText(_translate("Form", "3.确认样张后，点击完成"))
        self.label_openImg.setText(_translate("Form", "睁眼动作图像"))
        self.label_closeImg.setText(_translate("Form", "闭眼动作图像"))
