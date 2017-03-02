# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutMSUIDialog(object):
    def setupUi(self, AboutMSUIDialog):
        AboutMSUIDialog.setObjectName("AboutMSUIDialog")
        AboutMSUIDialog.resize(1104, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutMSUIDialog.sizePolicy().hasHeightForWidth())
        AboutMSUIDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(AboutMSUIDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(AboutMSUIDialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.textBrowser = QtWidgets.QTextBrowser(AboutMSUIDialog)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 200))
        self.textBrowser.setMaximumSize(QtCore.QSize(1310, 300))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.lblVersion = QtWidgets.QLabel(AboutMSUIDialog)
        self.lblVersion.setObjectName("lblVersion")
        self.verticalLayout_2.addWidget(self.lblVersion)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(AboutMSUIDialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(AboutMSUIDialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(AboutMSUIDialog)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btOK = QtWidgets.QPushButton(AboutMSUIDialog)
        self.btOK.setObjectName("btOK")
        self.horizontalLayout.addWidget(self.btOK)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AboutMSUIDialog)
        self.btOK.clicked.connect(AboutMSUIDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutMSUIDialog)

    def retranslateUi(self, AboutMSUIDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutMSUIDialog.setWindowTitle(_translate("AboutMSUIDialog", "About MSUI"))
        self.label.setText(_translate("AboutMSUIDialog", "Mission Support System User Interface"))
        self.textBrowser.setHtml(_translate("AboutMSUIDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans Mono\'; font-size:11pt; color:#000000; background-color:#ffffff;\">Please read the reference documentation:</span><span style=\" font-family:\'DejaVu Sans Mono\'; font-size:11pt; color:#000000;\"><br /><br />Rautenhaus, M., Bauer, G., and Doernbrack, A.: A web service based tool to plan<br />atmospheric research flights, Geosci. Model Dev., 5,55-71, doi:10.5194/gmd-5-55-2012, 2012.<br /><br />and the paper\'s Supplement (which includes a tutorial) before using the application. The documents are available at:<br /><br /> * </span><span style=\" font-family:\'DejaVu Sans Mono\'; font-size:11pt; color:#000000; background-color:#ffffff;\">http://www.geosci-model-dev.net/5/55/2012/gmd-5-55-2012.pdf</span><span style=\" font-family:\'DejaVu Sans Mono\'; font-size:11pt; color:#000000;\"><br /> * http://www.geosci-model-dev.net/5/55/2012/gmd-5-55-2012-supplement.pdf<br /><br />When using this software, please be so kind and acknowledge its use by citing the above mentioned reference documentation in publications, presentations, reports, etc. that you create. Thank you very much.<br /><br /></span></p></body></html>"))
        self.lblVersion.setText(_translate("AboutMSUIDialog", "Version: --VERSION--"))
        self.label_7.setText(_translate("AboutMSUIDialog", "License: Apache License Version 2.0"))
        self.label_3.setText(_translate("AboutMSUIDialog", "Copyright 2008-2014: Deutsches Zentrum fuer Luft- und Raumfahrt e.V.\n"
"Copyright 2011-2014: Marc Rautenhaus\n"
"Copyright 2015-2016: Marc Rautenhaus, Isabell Krisch, Jörn Ungermann, Jens-Uwe Grooß, Thomas Breuer, Reimar Bauer"))
        self.label_6.setText(_translate("AboutMSUIDialog", "<html><head/><body><p>See <a href=\"http://mss.rtfd.io\"><span style=\" text-decoration: underline; color:#0000ff;\">http://mss.rtfd.io</span></a> for detailed information and documentation.<br>Report bugs or feature requests at <a href=\"https://bitbucket.org/wxmetvis/mss\"><span style=\" text-decoration: underline; color:#0000ff;\">https://bitbucket.org/wxmetvis/mss</span></a>.</p></body></html>"))
        self.btOK.setText(_translate("AboutMSUIDialog", "Ok"))

