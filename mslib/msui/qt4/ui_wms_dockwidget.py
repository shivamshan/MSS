# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_wms_dockwidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WMSDockWidget(object):
    def setupUi(self, WMSDockWidget):
        WMSDockWidget.setObjectName(_fromUtf8("WMSDockWidget"))
        WMSDockWidget.resize(1001, 155)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WMSDockWidget.sizePolicy().hasHeightForWidth())
        WMSDockWidget.setSizePolicy(sizePolicy)
        WMSDockWidget.setMinimumSize(QtCore.QSize(1001, 0))
        WMSDockWidget.setMaximumSize(QtCore.QSize(16777215, 155))
        self.verticalLayout_4 = QtGui.QVBoxLayout(WMSDockWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(WMSDockWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.cbWMS_URL = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbWMS_URL.sizePolicy().hasHeightForWidth())
        self.cbWMS_URL.setSizePolicy(sizePolicy)
        self.cbWMS_URL.setEditable(True)
        self.cbWMS_URL.setObjectName(_fromUtf8("cbWMS_URL"))
        self.cbWMS_URL.addItem(_fromUtf8(""))
        self.cbWMS_URL.addItem(_fromUtf8(""))
        self.horizontalLayout_9.addWidget(self.cbWMS_URL)
        self.btGetCapabilities = QtGui.QPushButton(WMSDockWidget)
        self.btGetCapabilities.setObjectName(_fromUtf8("btGetCapabilities"))
        self.horizontalLayout_9.addWidget(self.btGetCapabilities)
        self.pbViewCapabilities = QtGui.QPushButton(WMSDockWidget)
        self.pbViewCapabilities.setObjectName(_fromUtf8("pbViewCapabilities"))
        self.horizontalLayout_9.addWidget(self.pbViewCapabilities)
        self.line_4 = QtGui.QFrame(WMSDockWidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_9.addWidget(self.line_4)
        self.cbAutoUpdate = QtGui.QCheckBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAutoUpdate.sizePolicy().hasHeightForWidth())
        self.cbAutoUpdate.setSizePolicy(sizePolicy)
        self.cbAutoUpdate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cbAutoUpdate.setObjectName(_fromUtf8("cbAutoUpdate"))
        self.horizontalLayout_9.addWidget(self.cbAutoUpdate)
        self.btGetMap = QtGui.QPushButton(WMSDockWidget)
        self.btGetMap.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btGetMap.setFont(font)
        self.btGetMap.setObjectName(_fromUtf8("btGetMap"))
        self.horizontalLayout_9.addWidget(self.btGetMap)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.cbLayer = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLayer.sizePolicy().hasHeightForWidth())
        self.cbLayer.setSizePolicy(sizePolicy)
        self.cbLayer.setMinimumSize(QtCore.QSize(200, 0))
        self.cbLayer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbLayer.setStyleSheet(_fromUtf8("QComboBox QAbstractItemView { min-width: 600px; }"))
        self.cbLayer.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cbLayer.setMinimumContentsLength(0)
        self.cbLayer.setObjectName(_fromUtf8("cbLayer"))
        self.cbLayer.addItem(_fromUtf8(""))
        self.cbLayer.addItem(_fromUtf8(""))
        self.cbLayer.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.cbLayer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_11 = QtGui.QLabel(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(40, 0))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.cbStyle = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbStyle.sizePolicy().hasHeightForWidth())
        self.cbStyle.setSizePolicy(sizePolicy)
        self.cbStyle.setMinimumSize(QtCore.QSize(200, 0))
        self.cbStyle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbStyle.setStyleSheet(_fromUtf8("QComboBox QAbstractItemView { min-width: 600px; }"))
        self.cbStyle.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.cbStyle.setFrame(True)
        self.cbStyle.setObjectName(_fromUtf8("cbStyle"))
        self.cbStyle.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cbStyle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teLayerAbstract = QtGui.QTextEdit(WMSDockWidget)
        self.teLayerAbstract.setMinimumSize(QtCore.QSize(242, 0))
        self.teLayerAbstract.setReadOnly(True)
        self.teLayerAbstract.setObjectName(_fromUtf8("teLayerAbstract"))
        self.verticalLayout.addWidget(self.teLayerAbstract)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line_2 = QtGui.QFrame(WMSDockWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_5.addWidget(self.line_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.cbInitTime = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbInitTime.sizePolicy().hasHeightForWidth())
        self.cbInitTime.setSizePolicy(sizePolicy)
        self.cbInitTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbInitTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbInitTime.setObjectName(_fromUtf8("cbInitTime"))
        self.cbInitTime.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.cbInitTime)
        self.tbInitTime_cbback = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_cbback.setObjectName(_fromUtf8("tbInitTime_cbback"))
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbback)
        self.tbInitTime_cbfwd = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_cbfwd.setObjectName(_fromUtf8("tbInitTime_cbfwd"))
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbfwd)
        self.dteInitTime = QtGui.QDateTimeEdit(WMSDockWidget)
        self.dteInitTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteInitTime.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.dteInitTime.setFont(font)
        self.dteInitTime.setCorrectionMode(QtGui.QAbstractSpinBox.CorrectToPreviousValue)
        self.dteInitTime.setCalendarPopup(False)
        self.dteInitTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteInitTime.setObjectName(_fromUtf8("dteInitTime"))
        self.horizontalLayout_3.addWidget(self.dteInitTime)
        self.tbInitTime_back = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_back.setObjectName(_fromUtf8("tbInitTime_back"))
        self.horizontalLayout_3.addWidget(self.tbInitTime_back)
        self.cbInitTime_step = QtGui.QComboBox(WMSDockWidget)
        self.cbInitTime_step.setObjectName(_fromUtf8("cbInitTime_step"))
        self.horizontalLayout_3.addWidget(self.cbInitTime_step)
        self.tbInitTime_fwd = QtGui.QToolButton(WMSDockWidget)
        self.tbInitTime_fwd.setObjectName(_fromUtf8("tbInitTime_fwd"))
        self.horizontalLayout_3.addWidget(self.tbInitTime_fwd)
        spacerItem = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.cbValidTime = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbValidTime.sizePolicy().hasHeightForWidth())
        self.cbValidTime.setSizePolicy(sizePolicy)
        self.cbValidTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbValidTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbValidTime.setObjectName(_fromUtf8("cbValidTime"))
        self.horizontalLayout_8.addWidget(self.cbValidTime)
        self.tbValidTime_cbback = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_cbback.setObjectName(_fromUtf8("tbValidTime_cbback"))
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbback)
        self.tbValidTime_cbfwd = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_cbfwd.setObjectName(_fromUtf8("tbValidTime_cbfwd"))
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbfwd)
        self.dteValidTime = QtGui.QDateTimeEdit(WMSDockWidget)
        self.dteValidTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteValidTime.setMaximumSize(QtCore.QSize(160, 16777215))
        self.dteValidTime.setDate(QtCore.QDate(2010, 1, 18))
        self.dteValidTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(8, 0, 0)))
        self.dteValidTime.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dteValidTime.setMinimumTime(QtCore.QTime(8, 0, 0))
        self.dteValidTime.setCalendarPopup(False)
        self.dteValidTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteValidTime.setObjectName(_fromUtf8("dteValidTime"))
        self.horizontalLayout_8.addWidget(self.dteValidTime)
        self.tbValidTime_back = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_back.setObjectName(_fromUtf8("tbValidTime_back"))
        self.horizontalLayout_8.addWidget(self.tbValidTime_back)
        self.cbValidTime_step = QtGui.QComboBox(WMSDockWidget)
        self.cbValidTime_step.setObjectName(_fromUtf8("cbValidTime_step"))
        self.horizontalLayout_8.addWidget(self.cbValidTime_step)
        self.tbValidTime_fwd = QtGui.QToolButton(WMSDockWidget)
        self.tbValidTime_fwd.setObjectName(_fromUtf8("tbValidTime_fwd"))
        self.horizontalLayout_8.addWidget(self.tbValidTime_fwd)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.cbLevel = QtGui.QComboBox(WMSDockWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLevel.sizePolicy().hasHeightForWidth())
        self.cbLevel.setSizePolicy(sizePolicy)
        self.cbLevel.setMinimumSize(QtCore.QSize(180, 0))
        self.cbLevel.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbLevel.setObjectName(_fromUtf8("cbLevel"))
        self.horizontalLayout_4.addWidget(self.cbLevel)
        self.tbLevel_back = QtGui.QToolButton(WMSDockWidget)
        self.tbLevel_back.setObjectName(_fromUtf8("tbLevel_back"))
        self.horizontalLayout_4.addWidget(self.tbLevel_back)
        self.tbLevel_fwd = QtGui.QToolButton(WMSDockWidget)
        self.tbLevel_fwd.setObjectName(_fromUtf8("tbLevel_fwd"))
        self.horizontalLayout_4.addWidget(self.tbLevel_fwd)
        spacerItem2 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.line_5 = QtGui.QFrame(WMSDockWidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_4.addWidget(self.line_5)
        self.cbTransparent = QtGui.QCheckBox(WMSDockWidget)
        self.cbTransparent.setChecked(True)
        self.cbTransparent.setObjectName(_fromUtf8("cbTransparent"))
        self.horizontalLayout_4.addWidget(self.cbTransparent)
        self.line_3 = QtGui.QFrame(WMSDockWidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_4.addWidget(self.line_3)
        self.label = QtGui.QLabel(WMSDockWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.cbCacheEnabled = QtGui.QCheckBox(WMSDockWidget)
        self.cbCacheEnabled.setChecked(True)
        self.cbCacheEnabled.setTristate(False)
        self.cbCacheEnabled.setObjectName(_fromUtf8("cbCacheEnabled"))
        self.horizontalLayout_4.addWidget(self.cbCacheEnabled)
        self.btClearCache = QtGui.QPushButton(WMSDockWidget)
        self.btClearCache.setObjectName(_fromUtf8("btClearCache"))
        self.horizontalLayout_4.addWidget(self.btClearCache)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.cbValidOn = QtGui.QCheckBox(WMSDockWidget)
        self.cbValidOn.setEnabled(False)
        self.cbValidOn.setMinimumSize(QtCore.QSize(0, 0))
        self.cbValidOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbValidOn.setPalette(palette)
        self.cbValidOn.setObjectName(_fromUtf8("cbValidOn"))
        self.gridLayout.addWidget(self.cbValidOn, 2, 0, 1, 1)
        self.cbLevelOn = QtGui.QCheckBox(WMSDockWidget)
        self.cbLevelOn.setEnabled(False)
        self.cbLevelOn.setMinimumSize(QtCore.QSize(0, 0))
        self.cbLevelOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbLevelOn.setPalette(palette)
        self.cbLevelOn.setCheckable(True)
        self.cbLevelOn.setObjectName(_fromUtf8("cbLevelOn"))
        self.gridLayout.addWidget(self.cbLevelOn, 0, 0, 1, 1)
        self.cbInitialisationOn = QtGui.QCheckBox(WMSDockWidget)
        self.cbInitialisationOn.setEnabled(False)
        self.cbInitialisationOn.setMinimumSize(QtCore.QSize(0, 0))
        self.cbInitialisationOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbInitialisationOn.setPalette(palette)
        self.cbInitialisationOn.setObjectName(_fromUtf8("cbInitialisationOn"))
        self.gridLayout.addWidget(self.cbInitialisationOn, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line = QtGui.QFrame(WMSDockWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_4.addWidget(self.line)

        self.retranslateUi(WMSDockWidget)
        QtCore.QMetaObject.connectSlotsByName(WMSDockWidget)

    def retranslateUi(self, WMSDockWidget):
        WMSDockWidget.setWindowTitle(_translate("WMSDockWidget", "WMS Dock Widget", None))
        self.label_7.setText(_translate("WMSDockWidget", "WMS URL:", None))
        self.cbWMS_URL.setToolTip(_translate("WMSDockWidget", "Enter a valid WMS URL here.", None))
        self.cbWMS_URL.setItemText(0, _translate("WMSDockWidget", "http://localhost:8002/fc_wms", None))
        self.cbWMS_URL.setItemText(1, _translate("WMSDockWidget", "http://osm.omniscale.net/proxy/service", None))
        self.btGetCapabilities.setToolTip(_translate("WMSDockWidget", "Request the capabilities from the WMS server.", None))
        self.btGetCapabilities.setText(_translate("WMSDockWidget", "get capabilities", None))
        self.pbViewCapabilities.setToolTip(_translate("WMSDockWidget", "Show information on the selected WMS server.", None))
        self.pbViewCapabilities.setText(_translate("WMSDockWidget", "view", None))
        self.cbAutoUpdate.setToolTip(_translate("WMSDockWidget", "Automatically request an updated map when the layer parameters have changed.", None))
        self.cbAutoUpdate.setText(_translate("WMSDockWidget", "update on changes", None))
        self.btGetMap.setToolTip(_translate("WMSDockWidget", "Request a map with the specifed parameters.", None))
        self.btGetMap.setText(_translate("WMSDockWidget", "get map", None))
        self.label_8.setText(_translate("WMSDockWidget", "Layer:", None))
        self.cbLayer.setItemText(0, _translate("WMSDockWidget", "BASEMAP", None))
        self.cbLayer.setItemText(1, _translate("WMSDockWidget", "MSLP", None))
        self.cbLayer.setItemText(2, _translate("WMSDockWidget", "TCC", None))
        self.label_11.setText(_translate("WMSDockWidget", "Style:", None))
        self.cbStyle.setItemText(0, _translate("WMSDockWidget", "...", None))
        self.teLayerAbstract.setHtml(_translate("WMSDockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p></body></html>", None))
        self.cbInitTime.setToolTip(_translate("WMSDockWidget", "Forecast initialisation time (base time) values provided by the WMS server.", None))
        self.cbInitTime.setItemText(0, _translate("WMSDockWidget", "2010-12-12T00:00:00Z", None))
        self.tbInitTime_cbback.setText(_translate("WMSDockWidget", "<", None))
        self.tbInitTime_cbfwd.setText(_translate("WMSDockWidget", ">", None))
        self.dteInitTime.setToolTip(_translate("WMSDockWidget", "You can also specify an initialisation date here.", None))
        self.dteInitTime.setDisplayFormat(_translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC", None))
        self.tbInitTime_back.setText(_translate("WMSDockWidget", "<", None))
        self.tbInitTime_fwd.setText(_translate("WMSDockWidget", ">", None))
        self.cbValidTime.setToolTip(_translate("WMSDockWidget", "Valid time values provided by the WMS server.", None))
        self.tbValidTime_cbback.setText(_translate("WMSDockWidget", "<", None))
        self.tbValidTime_cbfwd.setText(_translate("WMSDockWidget", ">", None))
        self.dteValidTime.setToolTip(_translate("WMSDockWidget", "Specify the time value here, especially if the server does not provide predefined values. Keep in mind that the specified value may not be available from the server, though.", None))
        self.dteValidTime.setDisplayFormat(_translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC", None))
        self.tbValidTime_back.setText(_translate("WMSDockWidget", "<", None))
        self.tbValidTime_fwd.setText(_translate("WMSDockWidget", ">", None))
        self.cbLevel.setToolTip(_translate("WMSDockWidget", "Elevation values provided by the WMS server.", None))
        self.tbLevel_back.setText(_translate("WMSDockWidget", "<", None))
        self.tbLevel_fwd.setText(_translate("WMSDockWidget", ">", None))
        self.cbTransparent.setText(_translate("WMSDockWidget", "transparent", None))
        self.label.setText(_translate("WMSDockWidget", "Cache:", None))
        self.cbCacheEnabled.setToolTip(_translate("WMSDockWidget", "Enable the image cache (retrieved images will be stored locally to speed up repeated retrievals).", None))
        self.cbCacheEnabled.setText(_translate("WMSDockWidget", "on", None))
        self.btClearCache.setToolTip(_translate("WMSDockWidget", "Clear all cache contents.", None))
        self.btClearCache.setText(_translate("WMSDockWidget", "clear", None))
        self.cbValidOn.setText(_translate("WMSDockWidget", "Valid:", None))
        self.cbLevelOn.setText(_translate("WMSDockWidget", "Level:", None))
        self.cbInitialisationOn.setText(_translate("WMSDockWidget", "Initialisation:", None))

