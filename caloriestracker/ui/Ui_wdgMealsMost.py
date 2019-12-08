# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgMealsMost.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgMealsMost(object):
    def setupUi(self, wdgMealsMost):
        wdgMealsMost.setObjectName("wdgMealsMost")
        wdgMealsMost.resize(1012, 669)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgMealsMost)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl = QtWidgets.QLabel(wdgMealsMost)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(wdgMealsMost)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cmbPeriod = QtWidgets.QComboBox(wdgMealsMost)
        self.cmbPeriod.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbPeriod.setObjectName("cmbPeriod")
        self.cmbPeriod.addItem("")
        self.cmbPeriod.addItem("")
        self.cmbPeriod.addItem("")
        self.cmbPeriod.addItem("")
        self.cmbPeriod.addItem("")
        self.horizontalLayout_3.addWidget(self.cmbPeriod)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tblMeals = myQTableWidget(wdgMealsMost)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblMeals.sizePolicy().hasHeightForWidth())
        self.tblMeals.setSizePolicy(sizePolicy)
        self.tblMeals.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tblMeals.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMeals.setAlternatingRowColors(True)
        self.tblMeals.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblMeals.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblMeals.setObjectName("tblMeals")
        self.tblMeals.setColumnCount(0)
        self.tblMeals.setRowCount(0)
        self.tblMeals.horizontalHeader().setStretchLastSection(False)
        self.tblMeals.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tblMeals)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.actionMealNew = QtWidgets.QAction(wdgMealsMost)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealNew.setIcon(icon)
        self.actionMealNew.setObjectName("actionMealNew")
        self.actionMealDelete = QtWidgets.QAction(wdgMealsMost)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/caloriestracker/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealDelete.setIcon(icon1)
        self.actionMealDelete.setObjectName("actionMealDelete")
        self.actionMealEdit = QtWidgets.QAction(wdgMealsMost)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/caloriestracker/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealEdit.setIcon(icon2)
        self.actionMealEdit.setObjectName("actionMealEdit")
        self.actionProductEdit = QtWidgets.QAction(wdgMealsMost)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/caloriestracker/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductEdit.setIcon(icon3)
        self.actionProductEdit.setObjectName("actionProductEdit")
        self.actionMealDeleteDay = QtWidgets.QAction(wdgMealsMost)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/caloriestracker/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealDeleteDay.setIcon(icon4)
        self.actionMealDeleteDay.setObjectName("actionMealDeleteDay")

        self.retranslateUi(wdgMealsMost)
        self.cmbPeriod.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(wdgMealsMost)

    def retranslateUi(self, wdgMealsMost):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgMealsMost", "Meals I eat the most"))
        self.label.setText(_translate("wdgMealsMost", "Select a period"))
        self.cmbPeriod.setItemText(0, _translate("wdgMealsMost", "Last week"))
        self.cmbPeriod.setItemText(1, _translate("wdgMealsMost", "Last month"))
        self.cmbPeriod.setItemText(2, _translate("wdgMealsMost", "Last year"))
        self.cmbPeriod.setItemText(3, _translate("wdgMealsMost", "Last three years"))
        self.cmbPeriod.setItemText(4, _translate("wdgMealsMost", "All registers"))
        self.actionMealNew.setText(_translate("wdgMealsMost", "New meal"))
        self.actionMealNew.setToolTip(_translate("wdgMealsMost", "New meal"))
        self.actionMealDelete.setText(_translate("wdgMealsMost", "Delete meal"))
        self.actionMealDelete.setToolTip(_translate("wdgMealsMost", "Delete meal"))
        self.actionMealEdit.setText(_translate("wdgMealsMost", "Edit meal"))
        self.actionMealEdit.setToolTip(_translate("wdgMealsMost", "Edit meal"))
        self.actionProductEdit.setText(_translate("wdgMealsMost", "Edit product"))
        self.actionProductEdit.setToolTip(_translate("wdgMealsMost", "Edit product"))
        self.actionMealDeleteDay.setText(_translate("wdgMealsMost", "Delete selected date meals"))
        self.actionMealDeleteDay.setToolTip(_translate("wdgMealsMost", "Delete selected date meals"))
from caloriestracker.ui.myqtablewidget import myQTableWidget
import caloriestracker.images.caloriestracker_rc