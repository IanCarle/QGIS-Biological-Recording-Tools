# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_osgr.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_osgr(object):
    def setupUi(self, osgr):
        osgr.setObjectName("osgr")
        osgr.setEnabled(True)
        osgr.resize(245, 292)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(osgr)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cboPrecision = QtWidgets.QComboBox(osgr)
        self.cboPrecision.setObjectName("cboPrecision")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.cboPrecision.addItem("")
        self.verticalLayout_3.addWidget(self.cboPrecision)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(osgr)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dsbGridSize = QtWidgets.QDoubleSpinBox(osgr)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dsbGridSize.sizePolicy().hasHeightForWidth())
        self.dsbGridSize.setSizePolicy(sizePolicy)
        self.dsbGridSize.setDecimals(3)
        self.dsbGridSize.setMaximum(100000000.0)
        self.dsbGridSize.setSingleStep(100.0)
        self.dsbGridSize.setObjectName("dsbGridSize")
        self.horizontalLayout.addWidget(self.dsbGridSize)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gbGridRef = QtWidgets.QGroupBox(osgr)
        self.gbGridRef.setMinimumSize(QtCore.QSize(0, 86))
        self.gbGridRef.setObjectName("gbGridRef")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbGridRef)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leOSGR = QtWidgets.QLineEdit(self.gbGridRef)
        self.leOSGR.setText("")
        self.leOSGR.setObjectName("leOSGR")
        self.horizontalLayout_3.addWidget(self.leOSGR)
        self.butZoom = QtWidgets.QPushButton(self.gbGridRef)
        self.butZoom.setMinimumSize(QtCore.QSize(40, 23))
        self.butZoom.setMaximumSize(QtCore.QSize(40, 23))
        self.butZoom.setObjectName("butZoom")
        self.horizontalLayout_3.addWidget(self.butZoom)
        self.butPan = QtWidgets.QPushButton(self.gbGridRef)
        self.butPan.setMinimumSize(QtCore.QSize(40, 22))
        self.butPan.setMaximumSize(QtCore.QSize(40, 23))
        self.butPan.setObjectName("butPan")
        self.horizontalLayout_3.addWidget(self.butPan)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbGROnClick = QtWidgets.QCheckBox(self.gbGridRef)
        self.cbGROnClick.setObjectName("cbGROnClick")
        self.horizontalLayout_4.addWidget(self.cbGROnClick)
        self.cbGRShowSquare = QtWidgets.QCheckBox(self.gbGridRef)
        self.cbGRShowSquare.setObjectName("cbGRShowSquare")
        self.horizontalLayout_4.addWidget(self.cbGRShowSquare)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addWidget(self.gbGridRef)
        self.gpGridSquares = QtWidgets.QGroupBox(osgr)
        self.gpGridSquares.setMinimumSize(QtCore.QSize(0, 119))
        self.gpGridSquares.setObjectName("gpGridSquares")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gpGridSquares)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.butGridTool = QtWidgets.QPushButton(self.gpGridSquares)
        self.butGridTool.setMinimumSize(QtCore.QSize(30, 30))
        self.butGridTool.setMaximumSize(QtCore.QSize(30, 30))
        self.butGridTool.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/osgr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butGridTool.setIcon(icon)
        self.butGridTool.setIconSize(QtCore.QSize(26, 26))
        self.butGridTool.setCheckable(True)
        self.butGridTool.setFlat(False)
        self.butGridTool.setObjectName("butGridTool")
        self.horizontalLayout_2.addWidget(self.butGridTool)
        self.butGridPoly = QtWidgets.QPushButton(self.gpGridSquares)
        self.butGridPoly.setMinimumSize(QtCore.QSize(30, 30))
        self.butGridPoly.setMaximumSize(QtCore.QSize(30, 30))
        self.butGridPoly.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/osgrPoly.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butGridPoly.setIcon(icon1)
        self.butGridPoly.setIconSize(QtCore.QSize(26, 26))
        self.butGridPoly.setCheckable(False)
        self.butGridPoly.setObjectName("butGridPoly")
        self.horizontalLayout_2.addWidget(self.butGridPoly)
        self.butClear = QtWidgets.QPushButton(self.gpGridSquares)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butClear.sizePolicy().hasHeightForWidth())
        self.butClear.setSizePolicy(sizePolicy)
        self.butClear.setMinimumSize(QtCore.QSize(30, 30))
        self.butClear.setMaximumSize(QtCore.QSize(30, 30))
        self.butClear.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butClear.setIcon(icon2)
        self.butClear.setIconSize(QtCore.QSize(30, 30))
        self.butClear.setObjectName("butClear")
        self.horizontalLayout_2.addWidget(self.butClear)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.butHelp = QtWidgets.QPushButton(self.gpGridSquares)
        self.butHelp.setMinimumSize(QtCore.QSize(30, 30))
        self.butHelp.setMaximumSize(QtCore.QSize(30, 30))
        self.butHelp.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butHelp.setIcon(icon3)
        self.butHelp.setIconSize(QtCore.QSize(24, 24))
        self.butHelp.setObjectName("butHelp")
        self.horizontalLayout_2.addWidget(self.butHelp)
        self.butGithub = QtWidgets.QPushButton(self.gpGridSquares)
        self.butGithub.setMinimumSize(QtCore.QSize(30, 30))
        self.butGithub.setMaximumSize(QtCore.QSize(30, 30))
        self.butGithub.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butGithub.setIcon(icon4)
        self.butGithub.setIconSize(QtCore.QSize(24, 24))
        self.butGithub.setObjectName("butGithub")
        self.horizontalLayout_2.addWidget(self.butGithub)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cbLabel = QtWidgets.QCheckBox(self.gpGridSquares)
        self.cbLabel.setChecked(True)
        self.cbLabel.setObjectName("cbLabel")
        self.verticalLayout.addWidget(self.cbLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pbGridSquares = QtWidgets.QProgressBar(self.gpGridSquares)
        self.pbGridSquares.setProperty("value", 0)
        self.pbGridSquares.setObjectName("pbGridSquares")
        self.horizontalLayout_5.addWidget(self.pbGridSquares)
        self.butCancel = QtWidgets.QPushButton(self.gpGridSquares)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butCancel.sizePolicy().hasHeightForWidth())
        self.butCancel.setSizePolicy(sizePolicy)
        self.butCancel.setMinimumSize(QtCore.QSize(0, 0))
        self.butCancel.setMaximumSize(QtCore.QSize(50, 500))
        self.butCancel.setObjectName("butCancel")
        self.horizontalLayout_5.addWidget(self.butCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.gpGridSquares)

        self.retranslateUi(osgr)
        self.cboPrecision.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(osgr)

    def retranslateUi(self, osgr):
        _translate = QtCore.QCoreApplication.translate
        osgr.setWindowTitle(_translate("osgr", "Form"))
        self.cboPrecision.setToolTip(_translate("osgr", "Set the OSGR precision."))
        self.cboPrecision.setItemText(0, _translate("osgr", "10 figure"))
        self.cboPrecision.setItemText(1, _translate("osgr", "8 figure"))
        self.cboPrecision.setItemText(2, _translate("osgr", "6 figure"))
        self.cboPrecision.setItemText(3, _translate("osgr", "Monad (1 km square)"))
        self.cboPrecision.setItemText(4, _translate("osgr", "Tetrad (2 km square)"))
        self.cboPrecision.setItemText(5, _translate("osgr", "Quadrant (5 km square)"))
        self.cboPrecision.setItemText(6, _translate("osgr", "Hectad (10 km square)"))
        self.cboPrecision.setItemText(7, _translate("osgr", "100 km square"))
        self.cboPrecision.setItemText(8, _translate("osgr", "User specified"))
        self.label.setText(_translate("osgr", "Grid size:"))
        self.dsbGridSize.setToolTip(_translate("osgr", "Set a size for the grid squares in the unitsused by the current project map CRS."))
        self.gbGridRef.setTitle(_translate("osgr", "Grid Ref at mouse cursor"))
        self.leOSGR.setToolTip(_translate("osgr", "<html><head/><body><p>Grid reference at mouse location or grid reference to which you want to navigate.</p></body></html>"))
        self.butZoom.setToolTip(_translate("osgr", "<html><head/><body><p>Zoom the map to the specified grid reference.</p></body></html>"))
        self.butZoom.setText(_translate("osgr", "Zoom"))
        self.butPan.setToolTip(_translate("osgr", "<html><head/><body><p>Pan the map to the specified grid reference.</p></body></html>"))
        self.butPan.setText(_translate("osgr", "Pan"))
        self.cbGROnClick.setToolTip(_translate("osgr", "<html><head/><body><p>Update grid reference only when map is clicked.</p></body></html>"))
        self.cbGROnClick.setText(_translate("osgr", "On click"))
        self.cbGRShowSquare.setToolTip(_translate("osgr", "<html><head/><body><p>Show grid square corresponding to grid reference. (For UK National Grid only.)</p></body></html>"))
        self.cbGRShowSquare.setText(_translate("osgr", "Show grid square"))
        self.gpGridSquares.setTitle(_translate("osgr", "OS grid squares"))
        self.butGridTool.setToolTip(_translate("osgr", "<html><head/><body><p>With this tool selected, drag a box over the map to generate grid squares.</p></body></html>"))
        self.butGridPoly.setToolTip(_translate("osgr", "<html><head/><body><p>With a feature selected, click this tool to generate grid squares over the feature.</p></body></html>"))
        self.butClear.setToolTip(_translate("osgr", "<html><head/><body><p>Delete all generated grid squares.</p></body></html>"))
        self.butHelp.setToolTip(_translate("osgr", "<html><head/><body><p><span style=\" font-size:12pt;\">Get more information about this tool and help on using it. This links to a webpage with up-to-date information about the tool. </span></p></body></html>"))
        self.butGithub.setToolTip(_translate("osgr", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Report an issue with this tool.</span><span style=\" font-size:12pt;\"> Using this channel is the best way to get attention quickly. Issues can be bug reports, enhancement requests or just questions. Anyone can view current issues, but to add a new issue you will need to sign up for a free Github account (very easy).</span></p></body></html>"))
        self.cbLabel.setToolTip(_translate("osgr", "<html><head/><body><p>Indicates whether or not to show labels for generated grids.</p></body></html>"))
        self.cbLabel.setText(_translate("osgr", "Label"))
        self.butCancel.setToolTip(_translate("osgr", "<html><head/><body><p>Interrupt the generation of grid squares.</p></body></html>"))
        self.butCancel.setText(_translate("osgr", "Cancel"))

