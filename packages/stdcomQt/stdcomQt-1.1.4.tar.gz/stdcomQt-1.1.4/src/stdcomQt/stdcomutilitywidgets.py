from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal

try :
    from stdcomipconfigdialog import *
    from stedcompostgresconfig import *
except :
    from stdcomQt.stdcomipconfigdialog import *
    from stdcomQt.stedcompostgresconfig import *


from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem, QTreeWidget
import re


class StecIPconfigDialog(QDialog):
    """
    IP Dialog, it is a IP and Port Configuation Dialog
    User can attach to sigNewIPPort to get IP and Port Changes
    """
    sigNewIPPort = pyqtSignal(str, str)
    sigCancel = pyqtSignal()

    def __init__(self, OkCallBack: object = None, CancelCallBack: object = None, ip: object = "localhost", port: object = "4897", parent: object = None) -> object:
        """
        :param callBack: func( str(ip), str(port))  user function or None
        :param cancelcallBack: func()  user function or None
        :param ip:
        :param port:
        :param parent:
        """
        super().__init__(parent)
        self.callBack = OkCallBack
        self.cancel = CancelCallBack
        self.ui = Ui_IPConfgDialog()
        self.ui.setupUi(self)
        self.ui.pushButtonOk.clicked.connect(self._OK)
        self.ui.pushButtonCancel.clicked.connect(self._Cancel)
        self.ui.lineEditIP.setText(str(ip))
        self.ui.lineEditPort.setText(str(port))
        self.show()

    @pyqtSlot()
    def _OK(self):
        """
        Ok is pressed, if ok callback is not set to None, it calls it, with ip and host as parameters.
        self.sigNewIPPort.emit(str(ip), str(port))
        :return:
        """
        ip = self.ui.lineEditIP.text()
        port = self.ui.lineEditPort.text()
        if self.callBack != None:
            self.callBack(ip, port)
        self.sigNewIPPort.emit(str(ip), str(port))

    def _Cancel(self):
        """
        When Cancel is pessed, if cancel callback is not None, it is called,
        also  self.sigCancel.emit()  
        :return:
        """
        if self.cancel != None:
            self.cancel()
        self.sigCancel.emit()


class StecPostgresConfigWidget(QWidget):
    """
    Configuration Widget for connecting to Stec Postgres Database
    """
    OKSignal = pyqtSignal(str, str, str, str, str)
    CancelSignal = pyqtSignal()
    OKCb = None

    def __init__(self, okCb=None, cancel=None, host: str = "localhost", port: str = 5432, database: str = "vremsoft",
                 user: str = "vremsoft", passowrd: str = "vrem2010!", parent=None):
        """

        :param okCb: Ok Call back, callback is called if not None, with host,port, database,user,password
        :param cancel:  If cancel is pressed, and this call back is not None
        :param host:  Host where postgres is running
        :param port:  Service port for postgres connection
        :param database: Database for stec
        :param user:  Database user
        :param passowrd:  Password, for user
        :param parent: QParent or None
        """
        self.OKCb = okCb
        self.cancel = cancel
        super().__init__(parent)
        self.ui = Ui_PostgresConfig()
        self.ui.setupUi(self)
        self.ui.lineEditHost.setText(host)
        self.ui.lineEditPort.setText(str(port))
        self.ui.lineEditDatabase.setText(database)
        self.ui.lineEditUser.setText(user)
        self.ui.lineEditPassword.setText(passowrd)
        self.ui.pushButtonOk.clicked.connect(self.Ok)
        self.ui.pushButtonCancel.clicked.connect(self.Cancel)

    @pyqtSlot()
    def Ok(self):
        """
        when ok is pressed
        also  self.OKSignal.emit(a, b, c, d, e)  
        :return:
        """
        a = self.ui.lineEditHost.text()
        b = self.ui.lineEditPort.text()
        c = self.ui.lineEditDatabase.text()
        d = self.ui.lineEditUser.text()
        e = self.ui.lineEditPassword.text()

        self.OKSignal.emit(a, b, c, d, e)
        if self.OKCb is not None:
            self.OKCb(a, b, c, d, e)

    @pyqtSlot()
    def Cancel(self):
        """
        cancel ir pressed
        :return:
        """
        if self.cancel != None:
            self.cancel()
        self.CancelSignal.emit()


class StecTreeMorph(QWidget):
    """
    Used to create a communication tree of names based on NextStep names
    It is passed with an exisiting QTreeWidget, this is the most userful of the tree widget because
    it uses exisitng QTreeWidgets
    """
    newTextSignal = pyqtSignal(str, str)
    newTextUserSignal = pyqtSignal(str, str, list)
    deleteTextSignal = pyqtSignal(str)
    originalList = None
    KeyMap = {"": QTreeWidgetItem}
    descriptions = {"": ""}
    userData     = {"" : []  }

    def __init__(self, tree: QTreeWidget, listOf=[""], parent=None):
        """
        :param tree: A QTreeWidget from a drawing or from a program module
        :param listOf: A list of parameters to sort into it
        :param parent:  QWidget parent or None
        """
        super().__init__(parent)
        self.ui = tree

        sortedList = []

        if listOf is not None:
            sortedList = sorted(listOf)
        self.originalList = sortedList

        keys = list()

        for i in range(0, len(sortedList)):
            keyLine = str(sortedList[i])
            key = re.split(r'[.;:,\s]\s*', keyLine)
            if len(key) >= 0:
                word = key[0]
                try:
                    idx = word.index('//')
                    if idx == 0:
                        rdx = word.rindex('/')
                        word = word[idx:rdx]
                        keys.append(word)

                except:
                    keys.append(word)

        keys = dict.fromkeys(keys).keys()
        keys = tuple(keys)
        self.headerItem = QTreeWidgetItem()

        item = QTreeWidgetItem()

        for i in range(0, len(keys)):
            parent = QTreeWidgetItem(self.ui)
            parent.setText(0, str(keys[i]))
            key = str(keys[i])

            self.KeyMap.update({word: parent})
            for x in range(0, len(sortedList)):
                word = str(sortedList[x])
                try:
                    result = word.index(key)
                    if result == 0:
                        child = QTreeWidgetItem(parent, 10001)
                        child.setText(0, word)
                        self.KeyMap.update({word: parent})
                        self.descriptions.update({word: ""})
                except:
                    print("Index Key", key)

        self.ui.clicked.connect(self._Selected)

    def clear(self):
        """
        clears the list, and puts the original back
        """
        self.ui.clear()
        self.KeyMap.clear()
        self.descriptions.clear()
        self.AddNames(self.originalList)

    def getData(self, item: QTreeWidgetItem):
        """
        gets
        """
        if self.callbackgetdata is not None:
            item.setData(0, Qt.UserRole, self.callbackgetdata(item.text()))


    def Index(self, base : str, search : str ):
        try :
            idx = base.index(search)
            return idx
        except :
            return -1
    @pyqtSlot(str)
    def AddName(self, name: str):
        """
        Connection from Multiverse, for one name at a time
        :param name:
        :return:
        """

        print("New Name:", name)

        key = re.split(r'[/.;:,\s]\s*', name)
        if len(key) >= 0:
            if  self.Index(name, '/') == 0 :
                if len(key) > 1 :
                    word = key[1]
            else:
                word = key[0]
            parent = None
            try:
                idx = word.index('//')
                if idx == 0:
                    rdx = word.rindex('/')
                    word = word[idx:rdx]
                    if word not in self.KeyMap.keys():
                        parent = QTreeWidgetItem(self.ui)
                        parent.setText(0, str(word))
                        self.KeyMap.update({word: parent})


            except:
                if word not in self.KeyMap.keys():
                    parent = QTreeWidgetItem(self.ui)
                    parent.setText(0, str(word))
                    self.KeyMap.update({word: parent})

            if parent == None:
                parent = self.KeyMap.get(word)

            self.ui.sortByColumn(0, QtCore.Qt.AscendingOrder)
            parent.setForeground(0, QtGui.QBrush(QtGui.QColor("red")))

            child = QTreeWidgetItem(parent, 10001)
            child.setForeground(0, QtGui.QBrush(QtGui.QColor("red")))
            child.setText(0, name)

    @pyqtSlot(list)
    def AddNames(self, names: list):
        """
        adds a list of names
        """
        sortedList = []
        if names is not None:
            sortedList = sorted(names)
            for name in sortedList:
                print("Add Names", name)
                self.AddName(str(name))
                self.descriptions.update({name: ""})

    @pyqtSlot(str, str)
    def AddDesc(self, name, desc):
        """
        :param name: Name in the tree
        :param desc: Description of that name
        :return:
        """
        self.descriptions.update({name: desc})

    @pyqtSlot(str, list)
    def AddUserData(self, name : str, userData : list):
        self.userData.update( {name :userData} )

    def _Selected(self):
        """
        internal use
        :return:
        """
        l = []
        for ix in self.ui.selectedItems():
            type = ix.type()
            if type == 10001:
                text = ix.text(0)
                l.append(text)
                desc = self.descriptions.get(text)
                if desc == None:
                    desc = "Tell Wang to Make this Malcolm Proof"
                self.newTextSignal.emit(text, desc)
                if text in self.userData :
                    data = self.userData.get(text )
                    self.newTextUserSignal.emit(text, desc, data)

    def DeleteSelected(self):
        """
        deletes selected items
        """
        for ix in self.ui.selectedItems():
            type = ix.type()
            if type == 10001:
                pp = ix.parent()
                if pp is not None:
                    pp.removeChild(ix)
                    text = ix.text(0)
                    self.deleteTextSignal.emit(text)
                    self.descriptions.update( { text: None })
                    self.userData.update( { text: None })
                    del ix

    def DeleteKey(self,key):

        listOf = self.ui.findItems(key, Qt.MatchExactly | Qt.MatchRecursive)
        for ix in listOf:
            type = ix.type()
            if type == 10001:
                pp = ix.parent()
                if pp is not None:
                    pp.removeChild(ix)
                    text = ix.text(0)
                    self.deleteTextSignal.emit(text)
                    self.descriptions.update( { text: None })
                    self.userData.update( { text: None })
                    del ix


