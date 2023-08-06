from PyQt5.QtCore import QMutex, QVariant, QTimer, QEvent, pyqtSlot, pyqtSignal, QObject, QCoreApplication
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtCore import QMutex, QVariant, QTimer, QEvent, pyqtSlot, pyqtSignal, QObject, QCoreApplication
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
import csv

from stdcomQt import *

if __name__ == '__main__':

    class Subs(QObject):
        timer = None
        w = None
        data = [0,1,2]

        def CallBackDescH(self,name, desc):
            print(" CallBackDescH :", name, desc)

        def CallBackDataH(self,name, desc):
            print(" CallBackDataH :", name, desc)

        def CallBackDescHH(self,name, desc):
            print(" CallBackDescHH :", name, desc)

        def CallBackDataHH(self,name, desc):
            print(" CallBackDataHH :", name, desc)
        def __init__(self, name, w : stecQSocket, Parent=None):
            self.name = name
            self.w = w
            timer = None


            if Parent is not None:
                super().__init__(Parent)
            else:
                super().__init__()

            self.h = Subscriber("hello2", self.w, self.CallBackDataH, self.CallBackDescH, self)
            self.hh = Subscriber("hello2", self.w, self.CallBackDataHH, self.CallBackDescHH,self)
            self.timer = QTimer(self)
            self.timer.setInterval(5000)
            self.timer.timeout.connect(self.timerout)
            self.timer.start()

        @pyqtSlot()
        def timerout(self):
            self.h.UpdateData(self.data)
            self.data[0] = int(self.data[0] + 1)



    print("stdcomQt")
    import sys

    if "--version" in sys.argv:
        print(stdcomQtVersion )
        sys.exit()

    app = QCoreApplication(sys.argv)
    w = stecQSocket()
    sub = Subs("Hello.There", w)
    app.exec_()
    w.quit()
    sys.exit(0)
