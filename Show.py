# -*- coding: utf8 -*-

import sys
from PyQt4 import QtGui, QtCore
from math import sin, cos, radians

class DrawText(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.j = 0
        self.text = [u'孬', u'孬', u'我', u'爱', u'你']
        self.initUI()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(200)              

    def initUI(self):
        self.setWindowTitle('You are my heart')
        self.resize(600, 600)
        

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.setRenderHint(QtGui.QPainter.Antialiasing)
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#FF0000')
        paint.setPen(color)
                        
        paint.save()
        paint.setWindow(-300, -300, 600, 600)
        center = QtCore.QPoint(0, 0)
        paint.drawEllipse(center, 200, 200)        
        for i in range(0, min(21, self.j)):            
            paint.save()
            paint.rotate(-4.5*i)
            paint.drawLine(0,200,200,0)
            paint.restore()        
        for i in range(0, min(21, self.j-21)):            
            paint.save()
            paint.rotate(4.5*i)
            paint.drawLine(0,200,-200,0)
            paint.restore()            
        for i in range(1, min(41, self.j - 41)):            
            paint.save()
            paint.rotate(-90-4.5*i)
            paint.drawLine(0, 200, 200*cos(radians(-4.5*i)),
                           200*sin(radians(-4.5*i)))
            paint.restore()
        paint.restore()

        paint.setFont(QtGui.QFont('System', 20))        
        for i in range(1, min(len(self.text)+1, self.j - 80)):
            temp =  ''.join(self.text[:i])
            paint.drawText(QtCore.QPoint(225, 550), temp)
        
        self.j += 1
        if self.j > 81 + len(self.text):
            self.timer.stop()

        paint.end()

app = QtGui.QApplication(sys.argv)
dt = DrawText()
dt.show()
sys.exit(app.exec_())



'''
class DrawText(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.resize(600, 600)
        
        self.setWindowTitle('Draw Text')


    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#FF0000')
        paint.setPen(color)
                        
        paint.save()
        paint.setWindow(-300, -300, 600, 600)
        center = QtCore.QPoint(0, 0)
        paint.drawEllipse(center, 200, 200)
        
        for i in range(0, 21):            
            paint.save()
            paint.rotate(-4.5*i)
            paint.drawLine(0,200,200,0)
            paint.restore()        
        for i in range(0, 21):            
            paint.save()
            paint.rotate(4.5*i)
            paint.drawLine(0,200,-200,0)
            paint.restore()
        for i in range(1, 41):            
            paint.save()
            paint.rotate(-90-4.5*i)
            paint.drawLine(0, 200, 200*cos(radians(-4.5*i)),
                           200*sin(radians(-4.5*i)))
            paint.restore()
        paint.restore()

        paint.setFont(QtGui.QFont('Decorative', 20))
        text = [u'妈', u'妈', u'辛', u'苦', u'了', u'！', '\n',
                u'母', u'亲', u'节', u'快', u'乐', u'！']
        temp = ''
        for i in text:
            temp += i
            paint.drawText(QtCore.QPoint(150, 550), temp)            
        paint.end()
'''
