import  sys, os
from PyQt5.QtWidgets import QApplication

import stdcomQt
from stdcomQt.stdcomutilitywidgets import StecIPconfigDialog, StecPostgresConfigWidget

import argparse

try:
    from PyQt5.QtSvg import QSvgWidget
except ImportError:
    QSvgWidget = None

from stdcomQt.stdcomQtPjanice import *
from stdcomQt.stdcomvsettings import *

from stdcomQt.pjanicesimple import *
from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QTableWidgetItem, QCheckBox
from PyQt5.QtCore import QSettings, QVariant, Qt, QEvent, QObject
from PyQt5.Qt import pyqtSlot, pyqtSignal
from stdcomQt import *
from stdcomQt.stdcomutilitywidgets import *
from stdcomQt.stdcomvsettings import *


class pjanice(pjanicesimpleGeneric):

    ipW = None

    host = "localhost"
    port = 4897

    pjanice = None


    def __init__(self, parent = None):
        settings = VSettings("Stec.PJanice")
        self.port = settings.value("pjanice.port", int(self.port))
        self.host = settings.value("pjanice.host", str(self.host))
        self.cBridge =  stecQSocket(self.host, self.port)

        super().__init__(self.cBridge)
        self.ipW = StecIPconfigDialog(self.callBack, self.cancel, self.host, self.port)
        self.ipW.hide()
        self.sigLeftMouseClick.connect(self.Click)
        self.sigRightMouseClick.connect(self.Click)



    def callBack(self, ip, port):
        print("Address: ", ip, " Service Port: ", port)
        self.ipW.hide()
        self.host = ip
        self.port = port
        settings = VSettings("Stec.PJanice")
        settings.setValue("pjanice.port", self.port)
        settings.setValue("pjanice.host", self.host)
        self.reset(self.host, self.port)



    def cancel(self):
        print("Cancel")
        self.ipW.hide()

    @pyqtSlot()
    def Click(self):
        self.ipW.show()



if __name__=="__main__":
    my_parser = argparse.ArgumentParser(description="Version :" + stdcomQt.stdcomQtVersion + " Stec Pjanice2 Python Version")
    current = os.path.dirname(os.path.realpath(__file__))

    # Getting the parent directory name
    # where the current directory is present.
    parent = os.path.dirname(current)

    # adding the parent directory to
    # the sys.path.
    sys.path.append(parent)
    app = QApplication(sys.argv)
    w = pjanice()
    w.show()

    sys.exit(app.exec_())