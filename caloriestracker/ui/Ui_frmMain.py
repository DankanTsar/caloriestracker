# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/frmMain.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(1458, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmMain.sizePolicy().hasHeightForWidth())
        frmMain.setSizePolicy(sizePolicy)
        frmMain.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/caloriestracker.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmMain.setWindowIcon(icon)
        self.central = QtWidgets.QWidget(frmMain)
        self.central.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central.sizePolicy().hasHeightForWidth())
        self.central.setSizePolicy(sizePolicy)
        self.central.setObjectName("central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setObjectName("layout")
        self.horizontalLayout.addLayout(self.layout)
        frmMain.setCentralWidget(self.central)
        self.menuBar = QtWidgets.QMenuBar(frmMain)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1458, 34))
        self.menuBar.setObjectName("menuBar")
        self.menuAyuda = QtWidgets.QMenu(self.menuBar)
        self.menuAyuda.setObjectName("menuAyuda")
        self.menuInformes = QtWidgets.QMenu(self.menuBar)
        self.menuInformes.setObjectName("menuInformes")
        self.menuXulpymoney = QtWidgets.QMenu(self.menuBar)
        self.menuXulpymoney.setObjectName("menuXulpymoney")
        self.menuProducts = QtWidgets.QMenu(self.menuBar)
        self.menuProducts.setObjectName("menuProducts")
        self.menuMealss = QtWidgets.QMenu(self.menuBar)
        self.menuMealss.setObjectName("menuMealss")
        self.menuCompanies = QtWidgets.QMenu(self.menuBar)
        self.menuCompanies.setObjectName("menuCompanies")
        self.menuBiometrics = QtWidgets.QMenu(self.menuBar)
        self.menuBiometrics.setObjectName("menuBiometrics")
        frmMain.setMenuBar(self.menuBar)
        self.tbMain = QtWidgets.QToolBar(frmMain)
        self.tbMain.setIconSize(QtCore.QSize(26, 26))
        self.tbMain.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tbMain.setObjectName("tbMain")
        frmMain.addToolBar(QtCore.Qt.TopToolBarArea, self.tbMain)
        self.statusBar = QtWidgets.QStatusBar(frmMain)
        self.statusBar.setObjectName("statusBar")
        frmMain.setStatusBar(self.statusBar)
        self.tbSettings = QtWidgets.QToolBar(frmMain)
        self.tbSettings.setObjectName("tbSettings")
        frmMain.addToolBar(QtCore.Qt.TopToolBarArea, self.tbSettings)
        self.actionExit = QtWidgets.QAction(frmMain)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/caloriestracker/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(frmMain)
        self.actionAbout.setIcon(icon)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAuxiliarTables = QtWidgets.QAction(frmMain)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/caloriestracker/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAuxiliarTables.setIcon(icon2)
        self.actionAuxiliarTables.setObjectName("actionAuxiliarTables")
        self.actionMemory = QtWidgets.QAction(frmMain)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/caloriestracker/transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMemory.setIcon(icon3)
        self.actionMemory.setObjectName("actionMemory")
        self.actionSettings = QtWidgets.QAction(frmMain)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/caloriestracker/configure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon4)
        self.actionSettings.setObjectName("actionSettings")
        self.actionHelp = QtWidgets.QAction(frmMain)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/caloriestracker/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName("actionHelp")
        self.actionSearch = QtWidgets.QAction(frmMain)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/caloriestracker/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon6)
        self.actionSearch.setObjectName("actionSearch")
        self.actionProductsUser = QtWidgets.QAction(frmMain)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/xulpymoney/keko.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductsUser.setIcon(icon7)
        self.actionProductsUser.setObjectName("actionProductsUser")
        self.actionCuriosities = QtWidgets.QAction(frmMain)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/caloriestracker/curiosity.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCuriosities.setIcon(icon8)
        self.actionCuriosities.setObjectName("actionCuriosities")
        self.actionMeals = QtWidgets.QAction(frmMain)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/caloriestracker/meals.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMeals.setIcon(icon9)
        self.actionMeals.setObjectName("actionMeals")
        self.actionBiometricsAdd = QtWidgets.QAction(frmMain)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/caloriestracker/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBiometricsAdd.setIcon(icon10)
        self.actionBiometricsAdd.setObjectName("actionBiometricsAdd")
        self.actionBiometrics = QtWidgets.QAction(frmMain)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/caloriestracker/list-add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBiometrics.setIcon(icon11)
        self.actionBiometrics.setObjectName("actionBiometrics")
        self.menuAyuda.addAction(self.actionAbout)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionCuriosities)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionHelp)
        self.menuInformes.addSeparator()
        self.menuInformes.addSeparator()
        self.menuXulpymoney.addAction(self.actionMemory)
        self.menuXulpymoney.addSeparator()
        self.menuXulpymoney.addAction(self.actionAuxiliarTables)
        self.menuXulpymoney.addSeparator()
        self.menuXulpymoney.addAction(self.actionSettings)
        self.menuXulpymoney.addSeparator()
        self.menuXulpymoney.addAction(self.actionExit)
        self.menuProducts.addSeparator()
        self.menuProducts.addAction(self.actionSearch)
        self.menuProducts.addSeparator()
        self.menuProducts.addAction(self.actionProductsUser)
        self.menuMealss.addAction(self.actionMeals)
        self.menuBiometrics.addAction(self.actionBiometrics)
        self.menuBiometrics.addSeparator()
        self.menuBiometrics.addAction(self.actionBiometricsAdd)
        self.menuBar.addAction(self.menuXulpymoney.menuAction())
        self.menuBar.addAction(self.menuCompanies.menuAction())
        self.menuBar.addAction(self.menuProducts.menuAction())
        self.menuBar.addAction(self.menuMealss.menuAction())
        self.menuBar.addAction(self.menuBiometrics.menuAction())
        self.menuBar.addAction(self.menuInformes.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())
        self.tbMain.addAction(self.actionMeals)
        self.tbMain.addAction(self.actionBiometrics)
        self.tbMain.addAction(self.actionSearch)
        self.tbSettings.addAction(self.actionSettings)
        self.tbSettings.addAction(self.actionHelp)
        self.tbSettings.addAction(self.actionCuriosities)
        self.tbSettings.addAction(self.actionExit)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        self.menuAyuda.setTitle(_translate("frmMain", "He&lp"))
        self.menuInformes.setTitle(_translate("frmMain", "&Reports"))
        self.menuXulpymoney.setTitle(_translate("frmMain", "Calories tracker"))
        self.menuProducts.setTitle(_translate("frmMain", "Prod&ucts"))
        self.menuMealss.setTitle(_translate("frmMain", "Meals"))
        self.menuCompanies.setTitle(_translate("frmMain", "Companies"))
        self.menuBiometrics.setTitle(_translate("frmMain", "Biometrics"))
        self.tbMain.setWindowTitle(_translate("frmMain", "Main toolbar"))
        self.tbSettings.setWindowTitle(_translate("frmMain", "Settings toolbar"))
        self.actionExit.setText(_translate("frmMain", "E&xit"))
        self.actionExit.setToolTip(_translate("frmMain", "Exit"))
        self.actionExit.setShortcut(_translate("frmMain", "Alt+Esc"))
        self.actionAbout.setText(_translate("frmMain", "&About"))
        self.actionAbout.setToolTip(_translate("frmMain", "About"))
        self.actionAbout.setShortcut(_translate("frmMain", "F2"))
        self.actionAuxiliarTables.setText(_translate("frmMain", "&Auxiliar tables"))
        self.actionAuxiliarTables.setToolTip(_translate("frmMain", "Auxiliar tables"))
        self.actionMemory.setText(_translate("frmMain", "&Update memory"))
        self.actionMemory.setToolTip(_translate("frmMain", "Update memory"))
        self.actionSettings.setText(_translate("frmMain", "&Settings"))
        self.actionSettings.setToolTip(_translate("frmMain", "Settings"))
        self.actionHelp.setText(_translate("frmMain", "&Help"))
        self.actionHelp.setToolTip(_translate("frmMain", "Help"))
        self.actionHelp.setShortcut(_translate("frmMain", "F1"))
        self.actionSearch.setText(_translate("frmMain", "Search"))
        self.actionSearch.setShortcut(_translate("frmMain", "Ctrl+B"))
        self.actionProductsUser.setText(_translate("frmMain", "&User products"))
        self.actionProductsUser.setToolTip(_translate("frmMain", "User products"))
        self.actionCuriosities.setText(_translate("frmMain", "&Curiosities"))
        self.actionCuriosities.setToolTip(_translate("frmMain", "Curiosities"))
        self.actionMeals.setText(_translate("frmMain", "Meals"))
        self.actionMeals.setToolTip(_translate("frmMain", "Meals"))
        self.actionBiometricsAdd.setText(_translate("frmMain", "Add biometrics"))
        self.actionBiometricsAdd.setToolTip(_translate("frmMain", "Add biometrics"))
        self.actionBiometrics.setText(_translate("frmMain", "Biometric information"))
        self.actionBiometrics.setToolTip(_translate("frmMain", "Biometric information"))
import caloriestracker.images.caloriestracker_rc
