# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt6 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_aboutAutoSplitWidget(object):
    def setupUi(self, aboutAutoSplitWidget):
        aboutAutoSplitWidget.setObjectName(_fromUtf8("aboutAutoSplitWidget"))
        aboutAutoSplitWidget.resize(276, 249)
        aboutAutoSplitWidget.setMinimumSize(QtCore.QSize(276, 249))
        aboutAutoSplitWidget.setMaximumSize(QtCore.QSize(276, 249))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        aboutAutoSplitWidget.setWindowIcon(icon)
        self.okButton = QtWidgets.QPushButton(aboutAutoSplitWidget)
        self.okButton.setGeometry(QtCore.QRect(190, 220, 71, 21))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.createdbyLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.createdbyLabel.setGeometry(QtCore.QRect(10, 44, 151, 16))
        self.createdbyLabel.setObjectName(_fromUtf8("createdbyLabel"))
        self.versionLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.versionLabel.setGeometry(QtCore.QRect(10, 21, 71, 16))
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.donatetextLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.donatetextLabel.setGeometry(QtCore.QRect(46, 95, 191, 41))
        self.donatetextLabel.setObjectName(_fromUtf8("donatetextLabel"))
        self.donatebuttonLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.donatebuttonLabel.setGeometry(QtCore.QRect(52, 127, 171, 91))
        self.donatebuttonLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.donatebuttonLabel.setObjectName(_fromUtf8("donatebuttonLabel"))
        self.iconLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.iconLabel.setGeometry(QtCore.QRect(190, 17, 62, 71))
        self.iconLabel.setObjectName(_fromUtf8("iconLabel"))

        self.retranslateUi(aboutAutoSplitWidget)
        self.okButton.clicked.connect(aboutAutoSplitWidget.close)
        QtCore.QMetaObject.connectSlotsByName(aboutAutoSplitWidget)

    def retranslateUi(self, aboutAutoSplitWidget):
        aboutAutoSplitWidget.setWindowTitle(_translate("aboutAutoSplitWidget", "About AutoSplit", None))
        self.okButton.setText(_translate("aboutAutoSplitWidget", "OK", None))
        self.createdbyLabel.setText(_translate("aboutAutoSplitWidget", "<html><head/><body><p>Created by <a href=\"https://twitter.com/toufool\"><span style=\" text-decoration: underline; color:#0000ff;\">Toufool</span></a> and <a href=\"https://twitter.com/faschz\"><span style=\" text-decoration: underline; color:#0000ff;\">Faschz</span></a></p></body></html>", None))
        self.versionLabel.setText(_translate("aboutAutoSplitWidget", "Version: ", None))
        self.donatetextLabel.setText(_translate("aboutAutoSplitWidget", "If you enjoy using this program, please\n"
"       consider donating. Thank you!", None))
        self.donatebuttonLabel.setText(_translate("aboutAutoSplitWidget", "<html><head/><body><p><a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=BYRHQG69YRHBA&item_name=AutoSplit+development&currency_code=USD&source=url\"><img src=\":/resources/donatebutton.png\"/></p></body></html>", None))
        self.iconLabel.setText(_translate("aboutAutoSplitWidget", "<html><head/><body><p><img src=\":/resources/icon.ico\"/></p></body></html>", None))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutAutoSplitWidget = QtWidgets.QWidget()
    ui = Ui_aboutAutoSplitWidget()
    ui.setupUi(aboutAutoSplitWidget)
    aboutAutoSplitWidget.show()
    sys.exit(app.exec())
