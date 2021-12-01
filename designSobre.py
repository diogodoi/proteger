# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designSobre.ui'
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

class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName(_fromUtf8("Sobre"))
        Sobre.setEnabled(True)
        Sobre.resize(300, 300)
        Sobre.setMinimumSize(QtCore.QSize(300, 300))
        Sobre.setMaximumSize(QtCore.QSize(300, 300))
        self.verticalLayout = QtGui.QVBoxLayout(Sobre)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Sobre)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtGui.QTextEdit(Sobre)
        self.textEdit.setEnabled(True)
        self.textEdit.setAcceptDrops(False)
        self.textEdit.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setReadOnly(True)
        self.textEdit.setAcceptRichText(True)
        self.textEdit.setCursorWidth(0)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButtonSobre = QtGui.QPushButton(Sobre)
        self.pushButtonSobre.setObjectName(_fromUtf8("pushButtonSobre"))
        self.verticalLayout.addWidget(self.pushButtonSobre)

        self.retranslateUi(Sobre)
        QtCore.QObject.connect(self.pushButtonSobre, QtCore.SIGNAL(_fromUtf8("clicked()")), Sobre.close)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        Sobre.setWindowTitle(_translate("Sobre", "Sobre", None))
        self.label.setText(_translate("Sobre", "Sobre o GUIPsyin", None))
        self.textEdit.setHtml(_translate("Sobre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">O GUIPsyin foi desenvolvido como projeto de mestrado do aluno Diogo Henrique Godoi pela Universidade de São Paulo, no Laboratório de Aprendizado de Robôs. Contou com o apoio do Centro Tecnológico da Informação Renato Archer e profissionais da área de psicologia. A interface foi desenvolvida com o intuido de criar uma forma amigável e de rápido aprendizado para que o Robô NAO seja manipulado.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Contato: diogo.godoi@usp.br</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Para conhecer o projeto acesse: https://github.com/diogodoi/proteger.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.pushButtonSobre.setText(_translate("Sobre", "Fechar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Sobre = QtGui.QWidget()
    ui = Ui_Sobre()
    ui.setupUi(Sobre)
    Sobre.show()
    sys.exit(app.exec_())

