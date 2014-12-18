# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys, datetime, hashlib




class LearningClock(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.initialize()        
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.millisecond = 0
        self.lastTime = 0
        self.totalTime = 0
        self.key = 'Ge ya an I love you'
        self.record = open('LearningTimeRecord.log', 'a+')        

    def initialize(self):
        self.setWindowTitle(u'计时器')
        self.resize(400, 300)            
        
        self.hour_label = QtGui.QLabel('00',self)
        colon_label1 = QtGui.QLabel(':', self)
        self.minute_label = QtGui.QLabel('00',self)
        colon_label2 = QtGui.QLabel(':', self)
        self.second_label = QtGui.QLabel('00',self)
        dot_label = QtGui.QLabel('.', self)
        self.millisecond_label = QtGui.QLabel('00',self)

        self.start_button = QtGui.QPushButton(u'开始', self)
        self.stop_button = QtGui.QPushButton(u'停止', self)
        self.clear_button = QtGui.QPushButton(u'重置', self)

        self.hour_label.setStyleSheet('QLabel {font-family: Serif;\
                    font-size:50px; color:#000}')
        colon_label1.setStyleSheet('QLabel {font-family:Serif;\
                    font-size:50px; color:#000}')
        self.minute_label.setStyleSheet('QLabel {font-family:Serif;\
                    font-size:50px; color:#000}')
        colon_label2.setStyleSheet('QLabel {font-family:Serif;\
                    font-size:50px; color:#000}')
        self.second_label.setStyleSheet('QLabel {font-family:Serif;\
                    font-size:50px; color:#000}')
        dot_label.setStyleSheet('QLabel {font-family:Serif;\
                    font-size:50px; color:#000}')
        self.millisecond_label.setStyleSheet('QLabel {font-family:Serif;\
                    font-size:50px; color:#000}')
        self.start_button.setStyleSheet(u'QPushButton {font-family:仿宋;\
                    font-size: 20px; color: #4B0082}')
        self.stop_button.setStyleSheet(u'QPushButton {font-family:仿宋;\
                    font-size: 20px; color: #4B0082}')
        self.clear_button.setStyleSheet(u'QPushButton {font-family:仿宋;\
                    font-size: 20px; color: #4B0082}')
        
        label = QtGui.QHBoxLayout()
        label.addStretch(1)
        label.addWidget(self.hour_label)
        label.addWidget(colon_label1)
        label.addWidget(self.minute_label)
        label.addWidget(colon_label2)
        label.addWidget(self.second_label)
        label.addWidget(dot_label)
        label.addWidget(self.millisecond_label)
        label.addStretch(1)
        
        button = QtGui.QHBoxLayout()
        button.addStretch(1)
        button.addWidget(self.start_button)
        button.addStretch(1)
        button.addWidget(self.stop_button)
        button.addStretch(1)
        button.addWidget(self.clear_button)
        button.addStretch(1)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(label)
        vbox.addStretch(1)
        vbox.addLayout(button)
        vbox.addStretch(1)

        self.setLayout(vbox)
        
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.onTimer)
        self.connect(self.start_button, QtCore.SIGNAL('clicked()'),
                     self.start)
        self.connect(self.stop_button, QtCore.SIGNAL('clicked()'),
                     self.stop)
        self.connect(self.clear_button, QtCore.SIGNAL('clicked()'),
                     self.clear)
        
        

    def start(self):
        if(not self.timer.isActive()):
            self.lastTime = datetime.datetime.now()
            line = datetime.datetime.strftime(self.lastTime,
                    '%Y-%m-%d %H:%M:%S') + '孬开始了学习'
            md5 = hashlib.md5(self.key + line)
            self.record.write(line + '\t:' + md5.hexdigest() + '\n')
            self.timer.start(10)    
        

    def stop(self):
        if(self.timer.isActive()):
            self.timer.stop()
            tempTime1 = datetime.datetime.now()
            line = datetime.datetime.strftime(tempTime1,
                        '%Y-%m-%d %H:%M:%S') + '孬停止了学习'
            md5 = hashlib.md5(self.key + line)
            self.record.write(line + '\t:' + md5.hexdigest() + '\n')
            
            tempTime2 = tempTime1 - self.lastTime
            s = tempTime2.seconds
            if s/3600 == 0:
                t_hour = ''
            else:
                t_hour = str(s/3600) + '小时'
            if (s%3600)/60 == 0:
                t_minute = ''
            else:
                t_minute = str((s%3600)/60) + '分钟'
            if s%60 == 0:
                t_second = ''
            else:
                t_second = str(s%60) + '秒'
            
            line  = '孬这次学习了' + t_hour + t_minute + t_second
            md5 = hashlib.md5(self.key + line)
            self.record.write(line + '\t:' + md5.hexdigest() + '\n')
            
            self.totalTime += s
            s = self.totalTime
            if s/3600 == 0:
                t_hour = ''
            else:
                t_hour = str(s/3600) + '小时'
            if (s%3600)/60 == 0:
                t_minute = ''
            else:
                t_minute = str((s%3600)/60) + '分钟'
            if s%60 == 0:
                t_second = ''
            else:
                t_second = str(s%60) + '秒'
            
            line = '孬累计学习了' + t_hour + t_minute + t_second
            md5 = hashlib.md5(self.key + line)
            self.record.write(line + '\t:' + md5.hexdigest() + '\n')            
        

    def clear(self):
        self.hour = self.minute = self.second = self.millisecond = 0
        self.millisecond_label.setText("{:02d}".format(self.millisecond))        
        self.second_label.setText("{:02d}".format(self.second))
        self.minute_label.setText("{:02d}".format(self.minute))
        self.hour_label.setText("{:02d}".format(self.hour))
        QtGui.QApplication.processEvents()
        self.lastTime = self.totalTime = 0
        line = '孬清空了学习计时器'
        md5 = hashlib.md5(self.key + line)
        self.record.write(line + '\t:' + md5.hexdigest() + '\n')
        

    def onTimer(self):
        self.millisecond += 1
        if self.millisecond == 100:
            self.second += 1
            self.millisecond = 0
        if self.second == 60:
            self.minute += 1
            self.second = 0
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        
        self.millisecond_label.setText("{:02d}".format(self.millisecond))        
        self.second_label.setText("{:02d}".format(self.second))
        self.minute_label.setText("{:02d}".format(self.minute))
        self.hour_label.setText("{:02d}".format(self.hour))
        QtGui.QApplication.processEvents()

    def encrypt(self, text):
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)            
            text = text + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + ('\0' * add)
        return text
    
    def closeEvent(self, event):
        self.record.close()

def main():
    app = QtGui.QApplication(sys.argv)
    clock = LearningClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
