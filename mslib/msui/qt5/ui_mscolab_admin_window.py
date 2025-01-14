# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mscolab_admin_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MscolabAdminWindow(object):
    def setupUi(self, MscolabAdminWindow):
        MscolabAdminWindow.setObjectName("MscolabAdminWindow")
        MscolabAdminWindow.resize(982, 756)
        self.centralwidget = QtWidgets.QWidget(MscolabAdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 5, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(0, 8, -1, 8)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.horizontalLayout_7.addWidget(self.usernameLabel)
        self.operationNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.operationNameLabel.setObjectName("operationNameLabel")
        self.horizontalLayout_7.addWidget(self.operationNameLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addUsersSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.addUsersSearch.setObjectName("addUsersSearch")
        self.horizontalLayout_2.addWidget(self.addUsersSearch)
        self.selectAllAddBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectAllAddBtn.setObjectName("selectAllAddBtn")
        self.horizontalLayout_2.addWidget(self.selectAllAddBtn)
        self.deselectAllAddBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deselectAllAddBtn.setObjectName("deselectAllAddBtn")
        self.horizontalLayout_2.addWidget(self.deselectAllAddBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.addUsersTable = QtWidgets.QTableWidget(self.centralwidget)
        self.addUsersTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.addUsersTable.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.addUsersTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.addUsersTable.setObjectName("addUsersTable")
        self.addUsersTable.setColumnCount(1)
        self.addUsersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.addUsersTable.setHorizontalHeaderItem(0, item)
        self.addUsersTable.horizontalHeader().setStretchLastSection(True)
        self.addUsersTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.addUsersTable)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addUsersPermission = QtWidgets.QComboBox(self.centralwidget)
        self.addUsersPermission.setObjectName("addUsersPermission")
        self.addUsersPermission.addItem("")
        self.addUsersPermission.addItem("")
        self.addUsersPermission.addItem("")
        self.horizontalLayout_3.addWidget(self.addUsersPermission)
        self.addUsersBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addUsersBtn.setObjectName("addUsersBtn")
        self.horizontalLayout_3.addWidget(self.addUsersBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.importPermissionsCB = QtWidgets.QComboBox(self.centralwidget)
        self.importPermissionsCB.setObjectName("importPermissionsCB")
        self.horizontalLayout_8.addWidget(self.importPermissionsCB)
        self.importPermissionsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.importPermissionsBtn.setObjectName("importPermissionsBtn")
        self.horizontalLayout_8.addWidget(self.importPermissionsBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.modifyUsersSearch = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyUsersSearch.sizePolicy().hasHeightForWidth())
        self.modifyUsersSearch.setSizePolicy(sizePolicy)
        self.modifyUsersSearch.setObjectName("modifyUsersSearch")
        self.horizontalLayout_4.addWidget(self.modifyUsersSearch)
        self.modifyUsersPermissionFilter = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modifyUsersPermissionFilter.sizePolicy().hasHeightForWidth())
        self.modifyUsersPermissionFilter.setSizePolicy(sizePolicy)
        self.modifyUsersPermissionFilter.setObjectName("modifyUsersPermissionFilter")
        self.modifyUsersPermissionFilter.addItem("")
        self.modifyUsersPermissionFilter.addItem("")
        self.modifyUsersPermissionFilter.addItem("")
        self.modifyUsersPermissionFilter.addItem("")
        self.horizontalLayout_4.addWidget(self.modifyUsersPermissionFilter)
        self.selectAllModifyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.selectAllModifyBtn.setObjectName("selectAllModifyBtn")
        self.horizontalLayout_4.addWidget(self.selectAllModifyBtn)
        self.deselectAllModifyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deselectAllModifyBtn.setObjectName("deselectAllModifyBtn")
        self.horizontalLayout_4.addWidget(self.deselectAllModifyBtn)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.modifyUsersTable = QtWidgets.QTableWidget(self.centralwidget)
        self.modifyUsersTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.modifyUsersTable.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.modifyUsersTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.modifyUsersTable.setObjectName("modifyUsersTable")
        self.modifyUsersTable.setColumnCount(2)
        self.modifyUsersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.modifyUsersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.modifyUsersTable.setHorizontalHeaderItem(1, item)
        self.modifyUsersTable.horizontalHeader().setStretchLastSection(True)
        self.modifyUsersTable.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.modifyUsersTable)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.modifyUsersPermission = QtWidgets.QComboBox(self.centralwidget)
        self.modifyUsersPermission.setObjectName("modifyUsersPermission")
        self.modifyUsersPermission.addItem("")
        self.modifyUsersPermission.addItem("")
        self.modifyUsersPermission.addItem("")
        self.horizontalLayout_5.addWidget(self.modifyUsersPermission)
        self.modifyUsersBtn = QtWidgets.QPushButton(self.centralwidget)
        self.modifyUsersBtn.setObjectName("modifyUsersBtn")
        self.horizontalLayout_5.addWidget(self.modifyUsersBtn)
        self.deleteUsersBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteUsersBtn.setObjectName("deleteUsersBtn")
        self.horizontalLayout_5.addWidget(self.deleteUsersBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MscolabAdminWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MscolabAdminWindow)
        self.statusbar.setObjectName("statusbar")
        MscolabAdminWindow.setStatusBar(self.statusbar)
        self.actionCloseWindow = QtWidgets.QAction(MscolabAdminWindow)
        self.actionCloseWindow.setObjectName("actionCloseWindow")
        MscolabAdminWindow.addAction(self.actionCloseWindow)

        self.retranslateUi(MscolabAdminWindow)
        self.actionCloseWindow.triggered.connect(MscolabAdminWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MscolabAdminWindow)

    def retranslateUi(self, MscolabAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        MscolabAdminWindow.setWindowTitle(_translate("MscolabAdminWindow", "Admin Window"))
        self.usernameLabel.setText(_translate("MscolabAdminWindow", "Logged In: "))
        self.operationNameLabel.setText(_translate("MscolabAdminWindow", "Operation: "))
        self.label.setText(_translate("MscolabAdminWindow", "All Users Without Permission:"))
        self.addUsersSearch.setPlaceholderText(_translate("MscolabAdminWindow", "Search User"))
        self.selectAllAddBtn.setText(_translate("MscolabAdminWindow", "Select All"))
        self.deselectAllAddBtn.setText(_translate("MscolabAdminWindow", "Deselect All"))
        item = self.addUsersTable.horizontalHeaderItem(0)
        item.setText(_translate("MscolabAdminWindow", "Username"))
        self.addUsersPermission.setItemText(0, _translate("MscolabAdminWindow", "admin"))
        self.addUsersPermission.setItemText(1, _translate("MscolabAdminWindow", "collaborator"))
        self.addUsersPermission.setItemText(2, _translate("MscolabAdminWindow", "viewer"))
        self.addUsersBtn.setToolTip(_translate("MscolabAdminWindow", "Add the selected users to the operation"))
        self.addUsersBtn.setText(_translate("MscolabAdminWindow", "Add"))
        self.label_3.setText(_translate("MscolabAdminWindow", "Clone Operation Permissions:"))
        self.importPermissionsBtn.setToolTip(_translate("MscolabAdminWindow", "Import permissions from another operation"))
        self.importPermissionsBtn.setText(_translate("MscolabAdminWindow", "Clone"))
        self.label_2.setText(_translate("MscolabAdminWindow", "All Users With Permission:"))
        self.modifyUsersSearch.setPlaceholderText(_translate("MscolabAdminWindow", "Search User"))
        self.modifyUsersPermissionFilter.setItemText(0, _translate("MscolabAdminWindow", "all"))
        self.modifyUsersPermissionFilter.setItemText(1, _translate("MscolabAdminWindow", "admin"))
        self.modifyUsersPermissionFilter.setItemText(2, _translate("MscolabAdminWindow", "collaborator"))
        self.modifyUsersPermissionFilter.setItemText(3, _translate("MscolabAdminWindow", "viewer"))
        self.selectAllModifyBtn.setText(_translate("MscolabAdminWindow", "Select All"))
        self.deselectAllModifyBtn.setText(_translate("MscolabAdminWindow", "Deselect All"))
        item = self.modifyUsersTable.horizontalHeaderItem(0)
        item.setText(_translate("MscolabAdminWindow", "Username"))
        item = self.modifyUsersTable.horizontalHeaderItem(1)
        item.setText(_translate("MscolabAdminWindow", "Permission"))
        self.modifyUsersPermission.setItemText(0, _translate("MscolabAdminWindow", "admin"))
        self.modifyUsersPermission.setItemText(1, _translate("MscolabAdminWindow", "collaborator"))
        self.modifyUsersPermission.setItemText(2, _translate("MscolabAdminWindow", "viewer"))
        self.modifyUsersBtn.setToolTip(_translate("MscolabAdminWindow", "Modify access permission of selected users"))
        self.modifyUsersBtn.setText(_translate("MscolabAdminWindow", "Modify"))
        self.deleteUsersBtn.setToolTip(_translate("MscolabAdminWindow", "Delete access permission of selected users"))
        self.deleteUsersBtn.setText(_translate("MscolabAdminWindow", "Delete"))
        self.actionCloseWindow.setText(_translate("MscolabAdminWindow", "actionCloseWindow"))
        self.actionCloseWindow.setShortcut(_translate("MscolabAdminWindow", "Ctrl+W"))
