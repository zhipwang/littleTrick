# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys, re, hashlib, winsound

class Detector(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.key = 'Ge ya an I love you'
        self.initialize()

    def initialize(self):
        self.setWindowTitle(u'学习结果检测器')
        self.resize(400, 300)

        label1 = QtGui.QLabel(u'诚信学习，人人有责！', self)
        label2 = QtGui.QLabel(u'打开日志文件:', self)
        self.label3 = QtGui.QLabel(self)
        self.button = QtGui.QPushButton(u'选择', self)

        label1.setStyleSheet('QLabel {font-family: Serif;\
                    font-size:30px; color:#000}')
        label2.setStyleSheet('QLabel {font-family: Serif;\
                    font-size:20px; color:#000}')
        self.label3.setStyleSheet('QLabel {font-family: Serif;\
                    font-size:30px; color:#FF0000}')
        self.button.setStyleSheet(u'font-family:仿宋;\
                    font-size: 20px; color: #4B0082}')

        hbox1 = QtGui.QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(label1)
        hbox1.addStretch(1)

        hbox2 = QtGui.QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(label2)
        hbox2.addWidget(self.button)
        hbox2.addStretch(1)

        hbox3 = QtGui.QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.label3)
        hbox3.addStretch(1)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.open)


    def open(self):
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                        u'打开',
                        "",
                        u'日志文件 (*.log)');
        if fileName != '':
            self.detect(fileName)


    def detect(self, fileName):
        mark = False
        file = open(fileName, 'r')
        while 1:
            line = file.readline()
            if not line:
                break
            m = re.match('(.*?)\s+:(.*)', line)
            md5 = hashlib.md5(self.key + m.group(1)).hexdigest()
            if md5 != m.group(2):
                self.label3.setText(u'居然敢篡改学习记录！')
                winsound.Beep(1000,5000)
                mark = True
                break
        if not mark:
            self.label3.setText(u'你是一个诚实的人！')        
        QtGui.QApplication.processEvents()
        

def main():
    app = QtGui.QApplication(sys.argv)
    detector = Detector()
    detector.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
