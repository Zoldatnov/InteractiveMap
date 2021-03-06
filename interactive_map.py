# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interactive_map.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import folium
import io
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 411)
        font = QtGui.QFont()
        font.setFamily("Garamond")
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
                                 "                stop:0 white, stop:1 rgb(204, 204, 204));\n"
                                 "border: 1px solid black;\n"
                                 "}\n"
                                 "")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setWindowIcon(QtGui.QIcon('icons/app.svg'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(11, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.latitude_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.latitude_spinbox.setFont(font)
        self.latitude_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.latitude_spinbox.setDecimals(6)
        self.latitude_spinbox.setMinimum(-90.0)
        self.latitude_spinbox.setMaximum(90.0)
        self.latitude_spinbox.setObjectName("latitude_spinbox")
        self.verticalLayout_2.addWidget(self.latitude_spinbox)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.longitude_spinbox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.longitude_spinbox.setFont(font)
        self.longitude_spinbox.setAutoFillBackground(False)
        self.longitude_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.longitude_spinbox.setSpecialValueText("")
        self.longitude_spinbox.setDecimals(6)
        self.longitude_spinbox.setMinimum(-180.0)
        self.longitude_spinbox.setMaximum(180.0)
        self.longitude_spinbox.setObjectName("longitude_spinbox")
        self.verticalLayout_2.addWidget(self.longitude_spinbox)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.radius_spinbox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.radius_spinbox.setFont(font)
        self.radius_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.radius_spinbox.setMinimum(100)
        self.radius_spinbox.setMaximum(5000)
        self.radius_spinbox.setObjectName("radius_spinbox")
        self.verticalLayout_2.addWidget(self.radius_spinbox)
        self.radius_slider = QtWidgets.QSlider(self.centralwidget)
        self.radius_slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                         "    border-radius: 1px;       \n"
                                         "    height: 7px;              \n"
                                         "    margin: -1px 0;           \n"
                                         "}\n"
                                         "QSlider::handle:horizontal {\n"
                                         "    background-color: white;\n"
                                         "    border: 2px solid black;\n"
                                         "    height: 14px;     \n"
                                         "    width: 12px;\n"
                                         "    margin: -4px 0;     \n"
                                         "    border-radius: 7px  ;\n"
                                         "    padding: -4px 0px;  \n"
                                         "}\n"
                                         "QSlider::add-page:horizontal {\n"
                                         "    background: darkgray;\n"
                                         "}\n"
                                         "QSlider::sub-page:horizontal {\n"
                                         "    background: darkgray;\n"
                                         "}")
        self.radius_slider.setMinimum(100)
        self.radius_slider.setMaximum(5000)
        self.radius_slider.setOrientation(QtCore.Qt.Horizontal)
        self.radius_slider.setObjectName("radius_slider")
        self.verticalLayout_2.addWidget(self.radius_slider)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.find_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_button.sizePolicy().hasHeightForWidth())
        self.find_button.setSizePolicy(sizePolicy)
        self.find_button.setMinimumSize(QtCore.QSize(0, 0))
        self.find_button.setMaximumSize(QtCore.QSize(60, 40))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(10)
        self.find_button.setFont(font)
        self.find_button.setStyleSheet("QPushButton {\n"
                                       "    background-color: white;\n"
                                       "    border: 2px solid black;\n"
                                       "    border-radius: 6px;\n"
                                       "    padding:5px;\n"
                                       "}\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: lightblue;\n"
                                       "    border-style: inset;\n"
                                       "}\n"
                                       "")
        self.find_button.setAutoDefault(False)
        self.find_button.setDefault(False)
        self.find_button.setFlat(False)
        self.find_button.setObjectName("find_button")
        self.horizontalLayout_3.addWidget(self.find_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self._2 = QtWidgets.QHBoxLayout()
        self._2.setObjectName("_2")
        self.find_parking = QtWidgets.QRadioButton(self.centralwidget)
        self.find_parking.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_parking.sizePolicy().hasHeightForWidth())
        self.find_parking.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.find_parking.setFont(font)
        self.find_parking.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/parking.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_parking.setIcon(icon)
        self.find_parking.setChecked(False)
        self.find_parking.setObjectName("find_parking")
        self._2.addWidget(self.find_parking)
        self.find_hospital = QtWidgets.QRadioButton(self.centralwidget)
        self.find_hospital.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_hospital.sizePolicy().hasHeightForWidth())
        self.find_hospital.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.find_hospital.setFont(font)
        self.find_hospital.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/hospital.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_hospital.setIcon(icon1)
        self.find_hospital.setChecked(False)
        self.find_hospital.setObjectName("find_hospital")
        self._2.addWidget(self.find_hospital)
        self.find_fuel = QtWidgets.QRadioButton(self.centralwidget)
        self.find_fuel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_fuel.sizePolicy().hasHeightForWidth())
        self.find_fuel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.find_fuel.setFont(font)
        self.find_fuel.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/gas.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_fuel.setIcon(icon2)
        self.find_fuel.setChecked(True)
        self.find_fuel.setObjectName("find_fuel")
        self._2.addWidget(self.find_fuel)
        self.find_cafe = QtWidgets.QRadioButton(self.centralwidget)
        self.find_cafe.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_cafe.sizePolicy().hasHeightForWidth())
        self.find_cafe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.find_cafe.setFont(font)
        self.find_cafe.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/cafe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_cafe.setIcon(icon3)
        self.find_cafe.setChecked(False)
        self.find_cafe.setObjectName("find_cafe")
        self._2.addWidget(self.find_cafe)
        self.find_bank = QtWidgets.QRadioButton(self.centralwidget)
        self.find_bank.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.find_bank.sizePolicy().hasHeightForWidth())
        self.find_bank.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Book")
        font.setPointSize(11)
        self.find_bank.setFont(font)
        self.find_bank.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/safe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_bank.setIcon(icon4)
        self.find_bank.setChecked(False)
        self.find_bank.setObjectName("find_bank")
        self._2.addWidget(self.find_bank)
        self.verticalLayout.addLayout(self._2)
        self.widget = QtWebEngineWidgets.QWebEngineView()
        self.widget.setObjectName("web_widget")
        self.map = folium.Map(
            location=[55.751624, 37.626386], tiles="OpenStreetMap", zoom_start=13
        )
        data = io.BytesIO()
        self.map.save(data, close_file=False)
        self.widget.setHtml(data.getvalue().decode())
        self.verticalLayout.addWidget(self.widget)
        self.distance_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.distance_label.sizePolicy().hasHeightForWidth())
        self.distance_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(11)
        self.distance_label.setFont(font)
        self.distance_label.setText("")
        self.distance_label.setScaledContents(False)
        self.distance_label.setAlignment(QtCore.Qt.AlignCenter)
        self.distance_label.setObjectName("distance_label")
        self.verticalLayout.addWidget(self.distance_label)
        self.verticalLayout.setStretch(1, 7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(1, 7)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Latitude"))
        self.label.setText(_translate("MainWindow", "Longitude"))
        self.label_3.setText(_translate("MainWindow", "Search radius, m"))
        self.find_button.setText(_translate("MainWindow", "Find"))
        self.find_parking.setText(_translate("MainWindow", "Parking"))
        self.find_hospital.setText(_translate("MainWindow", "Hospital"))
        self.find_fuel.setText(_translate("MainWindow", "Fuel"))
        self.find_cafe.setText(_translate("MainWindow", "Cafe"))
        self.find_bank.setText(_translate("MainWindow", "Bank"))
