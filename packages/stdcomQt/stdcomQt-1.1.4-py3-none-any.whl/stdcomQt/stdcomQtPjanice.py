import sys, re
import argparse

try:
    from PyQt5.QtSvg import QSvgWidget
except ImportError:
    QSvgWidget = None


try :
    from pjanicesimple import *
    from stdcomQt import *
    from stdcomutilitywidgets import *

except:
    from stdcomQt.pjanicesimple import *
    from stdcomQt.stdcomQt import *
    from stdcomQt.stdcomutilitywidgets import *

from PyQt5.QtWidgets import QDialog, QApplication, QTabWidget, QTableWidgetItem, QCheckBox
from PyQt5.QtCore import QSettings, QVariant, Qt, QEvent
from PyQt5.Qt import pyqtSlot, pyqtSignal

class pjanicesimpleGeneric(QWidget):
    """
    Stec Pjanice Widget, but with trees not list.
    """

    sigSelectedNewData = pyqtSignal(str, list)
    sigNewNameSelected = pyqtSignal(str)
    sigNewNameDescSelected = pyqtSignal(str,str)

    sigRightMouseClick = pyqtSignal()
    sigLeftMouseClick = pyqtSignal()

    selected = False
    cBridge = None
    currentSub = None
    suspectTable = False


    def __init__(self, cBridge: stecQSocket = None,  parent = None):
        """

        :param cBridge: or None, this will create one.
        :param parent:  or None
        """

        super().__init__(parent)
        self.ui = Ui_pJaniceSimple()
        self.ui.setupUi(self)
        self.show()

        if cBridge is None :
            self.cBridge = stecQSocket()

        else:
            self.cBridge = cBridge


        self.show()

        self.treeViewTags = StecTreeMorph(self.ui.treeWidgetUI, ["Stec"], self)
        self.treeViewTags.newTextSignal.connect(self.slotSelected)
        self.ui.tableWidgetData.itemChanged.connect(self.on_any_itemChanged)
        self.alternativeIgnore = None

        tags = self.cBridge.getNames()
        if tags is not None or len(tags) > 0:
            self.treeViewTags.AddNames(tags)
        self.cBridge.sigNewNames.connect(self.slotNames)

    def mousePressEvent(self, event):

        super().mousePressEvent( event)

        if event.button() == QtCore.Qt.RightButton:
            self.sigRightMouseClick.emit()
        else:
            self.sigLeftMouseClick.emit()

    def getcBridge(self):
        """
        return the current cBridge, the stdcomPyQt which is the qt version of the stdcom
        """
        return self.cBridge

    def newDesc(self, name, desc):
        print(name, desc)

    def newData(self, name, data):
        """
        Internal use
        :param name:
        :param data:
        :return:
        """
        self.ui.tableWidgetData.clear()
        self.ui.tableWidgetData.setRowCount(len(data))
        self.ui.tableWidgetData.setColumnCount(1)

        self.suspectTable = True
        for i in range(0, len(data)):
            d = QTableWidgetItem(str(data[i]))
            self.ui.tableWidgetData.setItem(i, 0, d)
        self.suspectTable = False
        self.sigSelectedNewData.emit(name,data)

    @pyqtSlot(str, str)
    def slotDesc(self, name, desc):
        """
        internal use
        """
        self.treeViewTags.AddDesc(name, desc)
        if name == self.currentSub:
            self.ui.plainTextEditDesc.clear()
            self.ui.plainTextEditDesc.insertPlainText(desc)
            self.sigNewNameDescSelected.emit(name, desc)

    @pyqtSlot(list)
    def slotNames(self, names):
        """
        internal use
        """
        self.treeViewTags.AddNames(names)


    @pyqtSlot(str, str)
    def slotSelected(self, name, desc):
        """
        selected slot, it tree item is clicked
        """
        self.ui.tableWidgetData.clear()

        if self.currentSub is not None :
            if name != self.currentSub.Name() :
                self.currentSub.deleteLater()
                self.currentSub = None
        if self.currentSub is None :
             self.currentSub = Subscriber(name, self.cBridge,self.newData, self.newDesc )

        self.ui.lineEditTag.setText(name)
        self.ui.plainTextEditDesc.clear()
        desc = self.currentSub.Desc()
        self.ui.plainTextEditDesc.clear()
        if desc is not None and desc != "":
            self.ui.plainTextEditDesc.insertPlainText(desc)
            self.sigNewNameDescSelected.emit(name,desc)
        else:
            self.ui.plainTextEditDesc.insertPlainText("Needs to Be Made Malcolm Proof")

        self.sigNewNameSelected.emit(name)

    @pyqtSlot(QTableWidgetItem)
    def on_any_itemChanged(self, itm: QTableWidgetItem):
        """
        when any item is clicked
        """
        c = itm.column()
        r = itm.row()

        if self.suspectTable is False:
            if self.currentSub is not None:
                Data = self.currentSub.Data()
                print("Changed R/C ", r, "/", c, itm.text())
                if Data is not None and r < len(Data):
                    Data[r] = itm.text()
                    self.currentSub.UpdateData(Data)

    @pyqtSlot()
    def addRow(self):
        """
        adds a row to table
        """
        rows = self.ui.tableWidgetLiveTags.rowCount()
        self.ui.tableWidgetLiveTags.setRowCount(rows + 1)


    @pyqtSlot()
    def reset(self, ip : str = "localhost", port: int = 4897):
        self.cBridge.SlotNewHost(ip, port)
        self.treeViewTags.clear()
        tags = self.cBridge.getNames()

        if tags is None or len(tags) == 0:
            tags = ["Stec"]
        else:
            self.treeViewTags.AddNames(tags)


if __name__ == "__main__":
    """
    bumped version
    """

    my_parser = argparse.ArgumentParser( description= "Version " + stdcomQtVersion + " Stec Pjanice Python Version")
    # Add the arguments
    my_parser.add_argument('-p','--project', metavar='project', required=False)

    args = my_parser.parse_args()
    nextProject = args.project
    app = QApplication(sys.argv)

    window = pjanicesimpleGeneric()
    cBridge = window.getcBridge()
    window.setWindowTitle("Stec PJanice Viewer")
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec_()

    if cBridge != None:
        cBridge.quit()
