# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(612, 490)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(612, 490))
        MainWindow.setMaximumSize(QtCore.QSize(612, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../VideoAutoSplitter/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.splitimagefolderLabel = QtGui.QLabel(self.centralwidget)
        self.splitimagefolderLabel.setGeometry(QtCore.QRect(90, 13, 91, 16))
        self.splitimagefolderLabel.setObjectName(_fromUtf8("splitimagefolderLabel"))
        self.splitimagefolderLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.splitimagefolderLineEdit.setGeometry(QtCore.QRect(187, 11, 247, 20))
        self.splitimagefolderLineEdit.setReadOnly(True)
        self.splitimagefolderLineEdit.setObjectName(_fromUtf8("splitimagefolderLineEdit"))
        self.browseButton = QtGui.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(443, 9, 75, 24))
        self.browseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.xLabel = QtGui.QLabel(self.centralwidget)
        self.xLabel.setGeometry(QtCore.QRect(25, 139, 7, 16))
        self.xLabel.setObjectName(_fromUtf8("xLabel"))
        self.liveimageCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.liveimageCheckBox.setEnabled(True)
        self.liveimageCheckBox.setGeometry(QtCore.QRect(125, 253, 121, 17))
        self.liveimageCheckBox.setChecked(True)
        self.liveimageCheckBox.setTristate(False)
        self.liveimageCheckBox.setObjectName(_fromUtf8("liveimageCheckBox"))
        self.loopCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.loopCheckBox.setEnabled(True)
        self.loopCheckBox.setGeometry(QtCore.QRect(500, 320, 121, 17))
        self.loopCheckBox.setChecked(False)
        self.loopCheckBox.setTristate(False)
        self.loopCheckBox.setObjectName(_fromUtf8("loopCheckBox"))
        self.selectregionButton = QtGui.QPushButton(self.centralwidget)
        self.selectregionButton.setGeometry(QtCore.QRect(5, 67, 101, 23))
        self.selectregionButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectregionButton.setObjectName(_fromUtf8("selectregionButton"))
        self.similaritythresholdLabel = QtGui.QLabel(self.centralwidget)
        self.similaritythresholdLabel.setGeometry(QtCore.QRect(10, 378, 91, 16))
        self.similaritythresholdLabel.setObjectName(_fromUtf8("similaritythresholdLabel"))
        self.similaritythresholdDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.similaritythresholdDoubleSpinBox.setGeometry(QtCore.QRect(160, 383, 64, 22))
        self.similaritythresholdDoubleSpinBox.setMaximum(1.0)
        self.similaritythresholdDoubleSpinBox.setSingleStep(0.01)
        self.similaritythresholdDoubleSpinBox.setProperty("value", 0.9)
        self.similaritythresholdDoubleSpinBox.setObjectName(_fromUtf8("similaritythresholdDoubleSpinBox"))
        self.startautosplitterButton = QtGui.QPushButton(self.centralwidget)
        self.startautosplitterButton.setGeometry(QtCore.QRect(501, 425, 101, 31))
        self.startautosplitterButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startautosplitterButton.setObjectName(_fromUtf8("startautosplitterButton"))
        self.resetButton = QtGui.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(501, 385, 101, 31))
        self.resetButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.reloadsettingsButton = QtGui.QPushButton(self.centralwidget)
        self.reloadsettingsButton.setGeometry(QtCore.QRect(500, 350, 101, 21))
        self.reloadsettingsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.reloadsettingsButton.setObjectName(_fromUtf8("takescreenshotButton"))
        self.undosplitButton = QtGui.QPushButton(self.centralwidget)
        self.undosplitButton.setGeometry(QtCore.QRect(477, 251, 61, 21))
        self.undosplitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.undosplitButton.setObjectName(_fromUtf8("undosplitButton"))
        self.skipsplitButton = QtGui.QPushButton(self.centralwidget)
        self.skipsplitButton.setGeometry(QtCore.QRect(541, 251, 61, 21))
        self.skipsplitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.skipsplitButton.setObjectName(_fromUtf8("skipsplitButton"))
        self.pauseLabel = QtGui.QLabel(self.centralwidget)
        self.pauseLabel.setGeometry(QtCore.QRect(10, 420, 111, 16))
        self.pauseLabel.setObjectName(_fromUtf8("pauseLabel"))
        self.checkfpsButton = QtGui.QPushButton(self.centralwidget)
        self.checkfpsButton.setGeometry(QtCore.QRect(5, 225, 51, 21))
        self.checkfpsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkfpsButton.setObjectName(_fromUtf8("checkfpsButton"))
        self.fpsLabel = QtGui.QLabel(self.centralwidget)
        self.fpsLabel.setGeometry(QtCore.QRect(87, 225, 20, 20))
        self.fpsLabel.setObjectName(_fromUtf8("fpsLabel"))
        self.showlivesimilarityCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.showlivesimilarityCheckBox.setEnabled(True)
        self.showlivesimilarityCheckBox.setGeometry(QtCore.QRect(10, 330, 111, 17))
        self.showlivesimilarityCheckBox.setChecked(True)
        self.showlivesimilarityCheckBox.setTristate(False)
        self.showlivesimilarityCheckBox.setObjectName(_fromUtf8("showlivesimilarityCheckBox"))
        self.showhighestsimilarityCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.showhighestsimilarityCheckBox.setEnabled(True)
        self.showhighestsimilarityCheckBox.setGeometry(QtCore.QRect(10, 351, 131, 17))
        self.showhighestsimilarityCheckBox.setChecked(True)
        self.showhighestsimilarityCheckBox.setTristate(False)
        self.showhighestsimilarityCheckBox.setObjectName(_fromUtf8("showhighestsimilarityCheckBox"))
        self.livesimilarityLabel = QtGui.QLabel(self.centralwidget)
        self.livesimilarityLabel.setGeometry(QtCore.QRect(160, 332, 46, 13))
        self.livesimilarityLabel.setText(_fromUtf8(""))
        self.livesimilarityLabel.setObjectName(_fromUtf8("livesimilarityLabel"))
        self.highestsimilarityLabel = QtGui.QLabel(self.centralwidget)
        self.highestsimilarityLabel.setGeometry(QtCore.QRect(160, 353, 46, 13))
        self.highestsimilarityLabel.setText(_fromUtf8(""))
        self.highestsimilarityLabel.setObjectName(_fromUtf8("highestsimilarityLabel"))
        self.splitLabel = QtGui.QLabel(self.centralwidget)
        self.splitLabel.setGeometry(QtCore.QRect(249, 320, 61, 16))
        self.splitLabel.setObjectName(_fromUtf8("splitLabel"))
        self.resetLabel = QtGui.QLabel(self.centralwidget)
        self.resetLabel.setGeometry(QtCore.QRect(249, 350, 61, 16))
        self.resetLabel.setObjectName(_fromUtf8("resetLabel"))
        self.skiptsplitLabel = QtGui.QLabel(self.centralwidget)
        self.skiptsplitLabel.setGeometry(QtCore.QRect(249, 380, 50, 16))
        self.skiptsplitLabel.setObjectName(_fromUtf8("skiptsplitLabel"))
        self.undosplitLabel = QtGui.QLabel(self.centralwidget)
        self.undosplitLabel.setGeometry(QtCore.QRect(249, 410, 61, 16))
        self.undosplitLabel.setObjectName(_fromUtf8("undosplitLabel"))
        self.splitLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.splitLineEdit.setGeometry(QtCore.QRect(316, 320, 81, 20))
        self.splitLineEdit.setReadOnly(True)
        self.splitLineEdit.setObjectName(_fromUtf8("splitLineEdit"))
        self.undosplitLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.undosplitLineEdit.setGeometry(QtCore.QRect(316, 410, 81, 20))
        self.undosplitLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.undosplitLineEdit.setReadOnly(True)
        self.undosplitLineEdit.setObjectName(_fromUtf8("undosplitLineEdit"))
        self.skipsplitLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.skipsplitLineEdit.setGeometry(QtCore.QRect(316, 380, 81, 20))
        self.skipsplitLineEdit.setReadOnly(True)
        self.skipsplitLineEdit.setObjectName(_fromUtf8("skipsplitLineEdit"))
        self.resetLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.resetLineEdit.setGeometry(QtCore.QRect(316, 350, 81, 20))
        self.resetLineEdit.setReadOnly(True)
        self.resetLineEdit.setObjectName(_fromUtf8("resetLineEdit"))
        self.setsplithotkeyButton = QtGui.QPushButton(self.centralwidget)
        self.setsplithotkeyButton.setGeometry(QtCore.QRect(409, 320, 71, 21))
        self.setsplithotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setsplithotkeyButton.setObjectName(_fromUtf8("setsplithotkeyButton"))
        self.setresethotkeyButton = QtGui.QPushButton(self.centralwidget)
        self.setresethotkeyButton.setGeometry(QtCore.QRect(410, 350, 71, 21))
        self.setresethotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setresethotkeyButton.setObjectName(_fromUtf8("setresethotkeyButton"))
        self.setskipsplithotkeyButton = QtGui.QPushButton(self.centralwidget)
        self.setskipsplithotkeyButton.setGeometry(QtCore.QRect(410, 380, 71, 21))
        self.setskipsplithotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setskipsplithotkeyButton.setObjectName(_fromUtf8("setskipsplithotkeyButton"))
        self.setundosplithotkeyButton = QtGui.QPushButton(self.centralwidget)
        self.setundosplithotkeyButton.setGeometry(QtCore.QRect(410, 410, 71, 21))
        self.setundosplithotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setundosplithotkeyButton.setObjectName(_fromUtf8("setundosplithotkeyButton"))
        self.line_live_bottom = QtGui.QFrame(self.centralwidget)
        self.line_live_bottom.setGeometry(QtCore.QRect(111, 247, 240, 2))
        self.line_live_bottom.setFrameShadow(QtGui.QFrame.Plain)
        self.line_live_bottom.setLineWidth(1)
        self.line_live_bottom.setFrameShape(QtGui.QFrame.HLine)
        self.line_live_bottom.setObjectName(_fromUtf8("line_live_bottom"))
        self.line_live_top = QtGui.QFrame(self.centralwidget)
        self.line_live_top.setGeometry(QtCore.QRect(111, 68, 240, 2))
        self.line_live_top.setFrameShadow(QtGui.QFrame.Plain)
        self.line_live_top.setLineWidth(1)
        self.line_live_top.setFrameShape(QtGui.QFrame.HLine)
        self.line_live_top.setObjectName(_fromUtf8("line_live_top"))
        self.line_live_right = QtGui.QFrame(self.centralwidget)
        self.line_live_right.setGeometry(QtCore.QRect(349, 69, 2, 180))
        self.line_live_right.setFrameShadow(QtGui.QFrame.Plain)
        self.line_live_right.setLineWidth(1)
        self.line_live_right.setFrameShape(QtGui.QFrame.VLine)
        self.line_live_right.setObjectName(_fromUtf8("line_live_right"))
        self.line_left = QtGui.QFrame(self.centralwidget)
        self.line_left.setGeometry(QtCore.QRect(234, 296, 2, 163))
        self.line_left.setFrameShadow(QtGui.QFrame.Plain)
        self.line_left.setLineWidth(1)
        self.line_left.setFrameShape(QtGui.QFrame.VLine)
        self.line_left.setObjectName(_fromUtf8("line_left"))
        self.line_live_left = QtGui.QFrame(self.centralwidget)
        self.line_live_left.setGeometry(QtCore.QRect(110, 69, 2, 180))
        self.line_live_left.setFrameShadow(QtGui.QFrame.Plain)
        self.line_live_left.setLineWidth(1)
        self.line_live_left.setFrameShape(QtGui.QFrame.VLine)
        self.line_live_left.setObjectName(_fromUtf8("line_live_left"))
        self.line_split_left = QtGui.QFrame(self.centralwidget)
        self.line_split_left.setGeometry(QtCore.QRect(360, 69, 2, 180))
        self.line_split_left.setFrameShadow(QtGui.QFrame.Plain)
        self.line_split_left.setLineWidth(1)
        self.line_split_left.setFrameShape(QtGui.QFrame.VLine)
        self.line_split_left.setObjectName(_fromUtf8("line_split_left"))
        self.line_split_right = QtGui.QFrame(self.centralwidget)
        self.line_split_right.setGeometry(QtCore.QRect(599, 69, 2, 180))
        self.line_split_right.setFrameShadow(QtGui.QFrame.Plain)
        self.line_split_right.setLineWidth(1)
        self.line_split_right.setFrameShape(QtGui.QFrame.VLine)
        self.line_split_right.setObjectName(_fromUtf8("line_split_right"))
        self.line_split_top = QtGui.QFrame(self.centralwidget)
        self.line_split_top.setGeometry(QtCore.QRect(361, 68, 240, 2))
        self.line_split_top.setFrameShadow(QtGui.QFrame.Plain)
        self.line_split_top.setLineWidth(1)
        self.line_split_top.setFrameShape(QtGui.QFrame.HLine)
        self.line_split_top.setObjectName(_fromUtf8("line_split_top"))
        self.line_split_bottom = QtGui.QFrame(self.centralwidget)
        self.line_split_bottom.setGeometry(QtCore.QRect(361, 247, 240, 2))
        self.line_split_bottom.setFrameShadow(QtGui.QFrame.Plain)
        self.line_split_bottom.setLineWidth(1)
        self.line_split_bottom.setFrameShape(QtGui.QFrame.HLine)
        self.line_split_bottom.setObjectName(_fromUtf8("line_split_bottom"))
        self.timerglobalhotkeysLabel = QtGui.QLabel(self.centralwidget)
        self.timerglobalhotkeysLabel.setGeometry(QtCore.QRect(313, 296, 101, 20))
        self.timerglobalhotkeysLabel.setObjectName(_fromUtf8("timerglobalhotkeysLabel"))
        self.line_right = QtGui.QFrame(self.centralwidget)
        self.line_right.setGeometry(QtCore.QRect(489, 296, 2, 163))
        self.line_right.setFrameShadow(QtGui.QFrame.Plain)
        self.line_right.setLineWidth(1)
        self.line_right.setFrameShape(QtGui.QFrame.VLine)
        self.line_right.setObjectName(_fromUtf8("line_right"))
        self.liveImage = QtGui.QLabel(self.centralwidget)
        self.liveImage.setGeometry(QtCore.QRect(111, 69, 240, 180))
        self.liveImage.setText(_fromUtf8(""))
        self.liveImage.setObjectName(_fromUtf8("liveImage"))
        self.currentSplitImage = QtGui.QLabel(self.centralwidget)
        self.currentSplitImage.setGeometry(QtCore.QRect(361, 69, 240, 180))
        self.currentSplitImage.setText(_fromUtf8(""))
        self.currentSplitImage.setObjectName(_fromUtf8("currentSplitImage"))
        self.currentsplitimageLabel = QtGui.QLabel(self.centralwidget)
        self.currentsplitimageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentsplitimageLabel.setGeometry(QtCore.QRect(370, 50, 221, 20))
        self.currentsplitimageLabel.setObjectName(_fromUtf8("currentsplitimageLabel"))
        self.imageloopLabel = QtGui.QLabel(self.centralwidget)
        self.imageloopLabel.setGeometry(QtCore.QRect(362, 251, 108, 20))
        self.imageloopLabel.setObjectName(_fromUtf8("Image Loop #:"))
        self.widthLabel = QtGui.QLabel(self.centralwidget)
        self.widthLabel.setGeometry(QtCore.QRect(14, 177, 31, 16))
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.heightLabel = QtGui.QLabel(self.centralwidget)
        self.heightLabel.setGeometry(QtCore.QRect(68, 177, 31, 16))
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.fpsvalueLabel = QtGui.QLabel(self.centralwidget)
        self.fpsvalueLabel.setGeometry(QtCore.QRect(58, 225, 26, 20))
        self.fpsvalueLabel.setText(_fromUtf8(""))
        self.fpsvalueLabel.setObjectName(_fromUtf8("fpsvalueLabel"))
        self.widthSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.widthSpinBox.setGeometry(QtCore.QRect(6, 193, 44, 22))
        self.widthSpinBox.setMinimum(1)
        self.widthSpinBox.setMaximum(10000)
        self.widthSpinBox.setProperty("value", 640)
        self.widthSpinBox.setObjectName(_fromUtf8("widthSpinBox"))
        self.heightSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(62, 193, 44, 22))
        self.heightSpinBox.setMinimum(1)
        self.heightSpinBox.setMaximum(10000)
        self.heightSpinBox.setProperty("value", 480)
        self.heightSpinBox.setObjectName(_fromUtf8("heightSpinBox"))
        self.captureregionLabel = QtGui.QLabel(self.centralwidget)
        self.captureregionLabel.setGeometry(QtCore.QRect(192, 50, 81, 16))
        self.captureregionLabel.setObjectName(_fromUtf8("captureregionLabel"))
        self.fpslimitLabel = QtGui.QLabel(self.centralwidget)
        self.fpslimitLabel.setGeometry(QtCore.QRect(8, 251, 51, 16))
        self.fpslimitLabel.setObjectName(_fromUtf8("fpslimitLabel"))
        self.fpslimitSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.fpslimitSpinBox.setGeometry(QtCore.QRect(62, 248, 44, 22))
        self.fpslimitSpinBox.setPrefix(_fromUtf8(""))
        self.fpslimitSpinBox.setDecimals(0)
        self.fpslimitSpinBox.setMinimum(30.0)
        self.fpslimitSpinBox.setMaximum(5000.0)
        self.fpslimitSpinBox.setSingleStep(1.0)
        self.fpslimitSpinBox.setProperty("value", 60.0)
        self.fpslimitSpinBox.setObjectName(_fromUtf8("fpslimitSpinBox"))
        self.currentsplitimagefileLabel = QtGui.QLabel(self.centralwidget)
        self.currentsplitimagefileLabel.setGeometry(QtCore.QRect(362, 271, 237, 20))
        self.currentsplitimagefileLabel.setText(_fromUtf8(""))
        self.currentsplitimagefileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentsplitimagefileLabel.setObjectName(_fromUtf8("currentsplitimagefileLabel"))
        self.takescreenshotButton = QtGui.QPushButton(self.centralwidget)
        self.takescreenshotButton.setGeometry(QtCore.QRect(250, 251, 91, 21))
        self.takescreenshotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.takescreenshotButton.setObjectName(_fromUtf8("takescreenshotButton"))
        self.xSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.xSpinBox.setGeometry(QtCore.QRect(6, 154, 44, 22))
        self.xSpinBox.setReadOnly(False)
        self.xSpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.xSpinBox.setMinimum(0)
        self.xSpinBox.setMaximum(999999999)
        self.xSpinBox.setSingleStep(1)
        self.xSpinBox.setProperty("value", 0)
        self.xSpinBox.setObjectName(_fromUtf8("xSpinBox"))
        self.ySpinBox = QtGui.QSpinBox(self.centralwidget)
        self.ySpinBox.setGeometry(QtCore.QRect(62, 154, 44, 22))
        self.ySpinBox.setReadOnly(False)
        self.ySpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.ySpinBox.setMinimum(0)
        self.ySpinBox.setMaximum(999999999)
        self.ySpinBox.setProperty("value", 0)
        self.ySpinBox.setObjectName(_fromUtf8("ySpinBox"))
        self.yLabel = QtGui.QLabel(self.centralwidget)
        self.yLabel.setGeometry(QtCore.QRect(81, 139, 7, 16))
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.comparisonmethodComboBox = QtGui.QComboBox(self.centralwidget)
        self.comparisonmethodComboBox.setGeometry(QtCore.QRect(143, 299, 81, 22))
        self.comparisonmethodComboBox.setObjectName(_fromUtf8("comparisonmethodComboBox"))
        self.comparisonmethodComboBox.addItem(_fromUtf8(""))
        self.comparisonmethodComboBox.addItem(_fromUtf8(""))
        self.comparisonmethodComboBox.addItem(_fromUtf8(""))
        self.pauseDoubleSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.pauseDoubleSpinBox.setGeometry(QtCore.QRect(160, 425, 64, 22))
        self.pauseDoubleSpinBox.setMaximum(999999999.0)
        self.pauseDoubleSpinBox.setSingleStep(1.0)
        self.pauseDoubleSpinBox.setProperty("value", 10.0)
        self.pauseDoubleSpinBox.setObjectName(_fromUtf8("pauseDoubleSpinBox"))
        self.custompausetimesCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.custompausetimesCheckBox.setEnabled(True)
        self.custompausetimesCheckBox.setGeometry(QtCore.QRect(10, 435, 121, 17))
        self.custompausetimesCheckBox.setWhatsThis(_fromUtf8(""))
        self.custompausetimesCheckBox.setChecked(False)
        self.custompausetimesCheckBox.setTristate(False)
        self.custompausetimesCheckBox.setObjectName(_fromUtf8("custompausetimesCheckBox"))
        self.customthresholdsCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.customthresholdsCheckBox.setEnabled(True)
        self.customthresholdsCheckBox.setGeometry(QtCore.QRect(10, 394, 111, 17))
        self.customthresholdsCheckBox.setWhatsThis(_fromUtf8(""))
        self.customthresholdsCheckBox.setChecked(False)
        self.customthresholdsCheckBox.setTristate(False)
        self.customthresholdsCheckBox.setObjectName(_fromUtf8("customthresholdsCheckBox"))
        self.comparisonmethodLabel = QtGui.QLabel(self.centralwidget)
        self.comparisonmethodLabel.setGeometry(QtCore.QRect(10, 300, 101, 16))
        self.comparisonmethodLabel.setObjectName(_fromUtf8("comparisonmethodLabel"))
        self.alignregionButton = QtGui.QPushButton(self.centralwidget)
        self.alignregionButton.setGeometry(QtCore.QRect(5, 92, 101, 23))
        self.alignregionButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alignregionButton.setObjectName(_fromUtf8("alignregionButton"))
        self.groupDummySplitsCheckBox = QtGui.QCheckBox(self.centralwidget)
        self.groupDummySplitsCheckBox.setGeometry(QtCore.QRect(252, 440, 230, 17))
        self.groupDummySplitsCheckBox.setChecked(False)
        self.groupDummySplitsCheckBox.setObjectName(_fromUtf8("groupDummySplitsCheckBox"))
        self.selectwindowButton = QtGui.QPushButton(self.centralwidget)
        self.selectwindowButton.setGeometry(QtCore.QRect(5, 117, 101, 23))
        self.selectwindowButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectwindowButton.setObjectName(_fromUtf8("selectwindowButton"))
        self.splitimagefolderLabel.raise_()
        self.splitimagefolderLineEdit.raise_()
        self.browseButton.raise_()
        self.xLabel.raise_()
        self.liveimageCheckBox.raise_()
        self.loopCheckBox.raise_()
        self.selectregionButton.raise_()
        self.similaritythresholdLabel.raise_()
        self.similaritythresholdDoubleSpinBox.raise_()
        self.startautosplitterButton.raise_()
        self.resetButton.raise_()
        self.reloadsettingsButton.raise_()
        self.undosplitButton.raise_()
        self.skipsplitButton.raise_()
        self.pauseLabel.raise_()
        self.checkfpsButton.raise_()
        self.fpsLabel.raise_()
        self.showlivesimilarityCheckBox.raise_()
        self.showhighestsimilarityCheckBox.raise_()
        self.livesimilarityLabel.raise_()
        self.highestsimilarityLabel.raise_()
        self.splitLabel.raise_()
        self.resetLabel.raise_()
        self.skiptsplitLabel.raise_()
        self.undosplitLabel.raise_()
        self.splitLineEdit.raise_()
        self.undosplitLineEdit.raise_()
        self.skipsplitLineEdit.raise_()
        self.resetLineEdit.raise_()
        self.setsplithotkeyButton.raise_()
        self.setresethotkeyButton.raise_()
        self.setskipsplithotkeyButton.raise_()
        self.setundosplithotkeyButton.raise_()
        self.line_live_bottom.raise_()
        self.line_live_top.raise_()
        self.line_live_right.raise_()
        self.line_left.raise_()
        self.line_live_left.raise_()
        self.line_split_left.raise_()
        self.line_split_right.raise_()
        self.line_split_top.raise_()
        self.line_split_bottom.raise_()
        self.timerglobalhotkeysLabel.raise_()
        self.line_right.raise_()
        self.currentsplitimageLabel.raise_()
        self.imageloopLabel.raise_()
        self.liveImage.raise_()
        self.currentSplitImage.raise_()
        self.widthLabel.raise_()
        self.heightLabel.raise_()
        self.fpsvalueLabel.raise_()
        self.widthSpinBox.raise_()
        self.heightSpinBox.raise_()
        self.captureregionLabel.raise_()
        self.fpslimitLabel.raise_()
        self.fpslimitSpinBox.raise_()
        self.currentsplitimagefileLabel.raise_()
        self.takescreenshotButton.raise_()
        self.xSpinBox.raise_()
        self.ySpinBox.raise_()
        self.yLabel.raise_()
        self.comparisonmethodComboBox.raise_()
        self.pauseDoubleSpinBox.raise_()
        self.custompausetimesCheckBox.raise_()
        self.customthresholdsCheckBox.raise_()
        self.comparisonmethodLabel.raise_()
        self.alignregionButton.raise_()
        self.groupDummySplitsCheckBox.raise_()
        self.selectwindowButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionView_Help = QtGui.QAction(MainWindow)
        self.actionView_Help.setObjectName(_fromUtf8("actionView_Help"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.splitimagefolderLineEdit, self.xSpinBox)
        MainWindow.setTabOrder(self.xSpinBox, self.ySpinBox)
        MainWindow.setTabOrder(self.ySpinBox, self.widthSpinBox)
        MainWindow.setTabOrder(self.widthSpinBox, self.heightSpinBox)
        MainWindow.setTabOrder(self.heightSpinBox, self.fpslimitSpinBox)
        MainWindow.setTabOrder(self.fpslimitSpinBox, self.liveimageCheckBox)
        MainWindow.setTabOrder(self.liveimageCheckBox, self.comparisonmethodComboBox)
        MainWindow.setTabOrder(self.comparisonmethodComboBox, self.showlivesimilarityCheckBox)
        MainWindow.setTabOrder(self.showlivesimilarityCheckBox, self.showhighestsimilarityCheckBox)
        MainWindow.setTabOrder(self.showhighestsimilarityCheckBox, self.customthresholdsCheckBox)
        MainWindow.setTabOrder(self.customthresholdsCheckBox, self.similaritythresholdDoubleSpinBox)
        MainWindow.setTabOrder(self.similaritythresholdDoubleSpinBox, self.custompausetimesCheckBox)
        MainWindow.setTabOrder(self.custompausetimesCheckBox, self.pauseDoubleSpinBox)
        MainWindow.setTabOrder(self.pauseDoubleSpinBox, self.splitLineEdit)
        MainWindow.setTabOrder(self.splitLineEdit, self.resetLineEdit)
        MainWindow.setTabOrder(self.resetLineEdit, self.skipsplitLineEdit)
        MainWindow.setTabOrder(self.skipsplitLineEdit, self.undosplitLineEdit)
        MainWindow.setTabOrder(self.undosplitLineEdit, self.groupDummySplitsCheckBox)
        MainWindow.setTabOrder(self.groupDummySplitsCheckBox, self.loopCheckBox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoSplit", None))
        self.splitimagefolderLabel.setText(_translate("MainWindow", "Split Image Folder:", None))
        self.browseButton.setText(_translate("MainWindow", "Browse..", None))
        self.xLabel.setText(_translate("MainWindow", "X", None))
        self.liveimageCheckBox.setText(_translate("MainWindow", "Live Capture Region", None))
        self.loopCheckBox.setText(_translate("MainWindow", "Loop Split Images", None))
        self.selectregionButton.setText(_translate("MainWindow", "Select Region", None))
        self.similaritythresholdLabel.setText(_translate("MainWindow", "Similarity threshold", None))
        self.startautosplitterButton.setText(_translate("MainWindow", "Start Auto Splitter", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.reloadsettingsButton.setText(_translate("MainWindow", "Reload Settings", None))
        self.undosplitButton.setText(_translate("MainWindow", "Undo Split", None))
        self.skipsplitButton.setText(_translate("MainWindow", "Skip Split", None))
        self.pauseLabel.setText(_translate("MainWindow", "Pause time (seconds)", None))
        self.checkfpsButton.setText(_translate("MainWindow", "Max FPS", None))
        self.fpsLabel.setText(_translate("MainWindow", "FPS", None))
        self.showlivesimilarityCheckBox.setText(_translate("MainWindow", "Show live similarity", None))
        self.showhighestsimilarityCheckBox.setText(_translate("MainWindow", "Show highest similarity", None))
        self.splitLabel.setText(_translate("MainWindow", "Start / Split", None))
        self.resetLabel.setText(_translate("MainWindow", "Reset", None))
        self.skiptsplitLabel.setText(_translate("MainWindow", "Skip Split", None))
        self.undosplitLabel.setText(_translate("MainWindow", "Undo Split", None))
        self.setsplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setresethotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setskipsplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setundosplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.timerglobalhotkeysLabel.setText(_translate("MainWindow", "Timer Global Hotkeys", None))
        self.currentsplitimageLabel.setText(_translate("MainWindow", "Current Split Image", None))
        self.imageloopLabel.setText(_translate("MainWindow", "Image Loop #:", None))
        self.widthLabel.setText(_translate("MainWindow", "Width", None))
        self.heightLabel.setText(_translate("MainWindow", "Height", None))
        self.captureregionLabel.setText(_translate("MainWindow", "Capture Region", None))
        self.fpslimitLabel.setText(_translate("MainWindow", "FPS Limit:", None))
        self.takescreenshotButton.setText(_translate("MainWindow", "Take Screenshot", None))
        self.yLabel.setText(_translate("MainWindow", "Y", None))
        self.comparisonmethodComboBox.setItemText(0, _translate("MainWindow", "L2 Norm", None))
        self.comparisonmethodComboBox.setItemText(1, _translate("MainWindow", "Histograms", None))
        self.comparisonmethodComboBox.setItemText(2, _translate("MainWindow", "pHash", None))
        self.custompausetimesCheckBox.setText(_translate("MainWindow", "Custom pause times", None))
        self.customthresholdsCheckBox.setText(_translate("MainWindow", "Custom thresholds", None))
        self.comparisonmethodLabel.setText(_translate("MainWindow", "Comparison Method", None))
        self.alignregionButton.setText(_translate("MainWindow", "Align Region", None))
        self.groupDummySplitsCheckBox.setText(_translate("MainWindow", "Group dummy splits when undoing/skipping", None))
        self.selectwindowButton.setText(_translate("MainWindow", "Select Window", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionView_Help.setText(_translate("MainWindow", "View Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

