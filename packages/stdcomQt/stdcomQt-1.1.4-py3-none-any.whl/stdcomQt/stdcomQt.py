from PyQt5.QtCore import QMutex, QVariant, QTimer, QEvent, pyqtSlot, pyqtSignal, QObject, QCoreApplication
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
import csv


stdcomQtVersion = "1.1.4"
class SubObject(QObject):
    """
    Internal use, not for users
    """
    sigNewData = pyqtSignal(str, list)
    sigNewDesc = pyqtSignal(str, str)

    active = False
    owner = False
    name: str = None
    data = []
    desc = None
    connectedSubs = 0

    proxLock = QMutex()

    def __init__(self, name, Parent=None):
        self.name = name
        active = False
        if Parent is not None:
            super().__init__(Parent)
        else:
            super().__init__()
        self.connectedSubs = 0
    def AddData(self, data=[]):
        self.proxLock.lock()
        self.data = data
        self.proxLock.unlock()
        self.FireConnect()

    def GetData(self):
        self.proxLock.lock()
        data = self.data
        self.proxLock.unlock()
        return data

    def GetDesc(self):
        self.proxLock.lock()
        desc = self.desc
        self.proxLock.unlock()
        return desc

    def GetName(self):
        self.proxLock.lock()
        name = self.name
        self.proxLock.unlock()
        return name

    def AddDesc(self, desc):
        self.proxLock.lock()
        self.desc = desc
        self.proxLock.unlock()
        self.sigNewDesc.emit(self.name, self.desc)

    def FireConnect(self):
        self.sigNewData.emit(self.name, self.data)
        if self.desc is not None:
            self.sigNewDesc.emit(self.name, self.desc)

    def SetOwner(self, owner: bool = True):
        self.proxLock.lock()
        self.owner = owner
        self.proxLock.unlock()

    def isOwner(self):
        self.proxLock.lock()
        owner = self.owner
        self.proxLock.unlock()
        return owner

    def AddSub(self):
        self.proxLock.lock()
        self.connectedSubs = self.connectedSubs + 1
        subs = self.connectedSubs
        self.proxLock.unlock()
        return subs

    def DelSub(self):
        self.proxLock.lock()
        self.connectedSubs = self.connectedSubs  - 1
        subs = self.connectedSubs
        if self.connectedSubs < 0 :
            self.connectedSubs = 0
        self.proxLock.unlock()
        return subs

    def GetNumberSubs(self):
        subs = 0
        self.proxLock.lock()
        subs = self.connectedSubs
        self.proxLock.unlock()
        return subs

    def SetActive(self, active : bool = True):
        self.proxLock.lock()
        self.active = active
        self.proxLock.unlock()

    def isActive(self):
        self.proxLock.lock()
        active = self.active
        self.proxLock.unlock()
        return active


class stecQSocket(QObject):
    """
    Qt Style cBridge to  Multiverse just like c++ code
    """
    sigNewNames = pyqtSignal(list)
    sigDown = pyqtSignal()
    signUp = pyqtSignal()

    servicePort = None
    host = None
    timer = None
    xm = None
    Parent = None
    connected = False

    namesLock = QMutex()
    connectedLock = QMutex()
    names = {}

    def __init__(self, host: str = "localhost", port: int = 4897, Parent=None):
        """
        :param host: Host IP address default localhost
        :param port: Service Port, default 4897
        :param Parent: Qt QObject parent or None default
        """
        if Parent is not None:
            super().__init__(Parent)
        else:
            super().__init__()

        self.Parent = Parent

        self.servicePort = int(port)
        self.host = str(host)
        self.xm = QTcpSocket()
        self.xm.connected.connect(self.SlotConnected)
        self.xm.disconnected.connect(self.SlotDisconnected)
        self.xm.readyRead.connect(self.SlotDataReady)
        self.xm.error.connect(self.SlotSocketError)

        self.timer = QTimer(self)
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.SlotTimerout)
        self.timer.start()
        self.SlotTimerout()

    def quit(self):
        """
        call before deletelater by user
        :return:
        """
        self.xm.close()
        self.timer.stop()

    def InsertProxy(self, name):
        """
        Internal use, not for user
        :param name: name of the subscription
        :return:
        """
        self.namesLock.lock()
        if name not in self.names:
            self.names.update({name: SubObject(name)})

        xproxy = self.names.get(name)
        self.namesLock.unlock()
        return xproxy

    def getNames(self):
        keys = []
        self.namesLock.lock()
        keys = self.names.keys()
        self.namesLock.unlock()
        return keys

    def setOwner(self, name, description: str = "Make this MalcolmProof Please", flag: bool = True):
        """
        Sets us as the owner of the subscription, we will automatically refeed multiverse if reset
        :param name: subscription name
        :param flag:  True means we are golden copy, false restores to non-golden copy
        :return:
        """
        proxy = self.InsertProxy(name)
        proxy.SetOwner(flag)

    def isConnected(self):
        """
        returns true if connected to multiverse
        :return:
        """
        self.connectedLock.lock()
        connected = self.connected
        self.connectedLock.unlock()
        return connected

    def Host(self):
        """
        :return: current Host
        """
        return self.host
    def Port(self):
        """
        :return:  current service Port
        """
        return self.servicePort
    def ProcessCommand(self, row):
        """
        internal use, decodes messages
        :param row:
        :return:
        """
        if ('NAMESUP' in row):
            data = []
            for x in range(1, len(row)):
                name = str(row[x])
                data.append(name)
                xp = self.InsertProxy(name)
            if len(data):
                self.sigNewNames.emit(data)

        elif 'READDATA' in row:
            if len(row) > 2:
                name = str(row[1])
                data = []
                for x in range(2, len(row)):
                    data.append(row[x])
                if len(data):
                    xp = self.InsertProxy(name)
                    xp.AddData(data)

        elif 'UPDATE-DESC' in row:
            name = str(row[1])

            xp = self.InsertProxy(name)
            xp.AddDesc(str(row[2]))

    @pyqtSlot()
    def SlotSocketError(self):
        """
        internal use
        called when connection to multiverse fails
        :return:
        """
        if self.xm.isOpen():
            self.xm.close()
        self.connectedLock.lock()
        self.connected = False
        self.connectedLock.unlock()

    @pyqtSlot()
    def SlotConnected(self):
        """
        interal use
        Will restart any Subscription previously made
        :return:
        """
        self.connectedLock.lock()
        self.connected = True
        self.connectedLock.unlock()

        command = "NAMES\n"
        self.SlotWrite(command)

        self.namesLock.lock()
        names = self.names.keys()
        for name in names:
            proxy = self.names.get(name)
            if proxy.isActive() is True:
                command = "NOTIFY," + name + "\n"
                self.SlotWrite(command)

            if proxy.isOwner():
                what = proxy.GetData()
                if what is not None:

                    if len(what):
                        index = 0
                        if isinstance(what[0], int):
                            command = "UPDATEI," + name + "," + str(index)

                        elif isinstance(what[0], float):
                            command = "UPDATEF," + name + "," + str(index)

                        elif isinstance(what[0], bool):
                            command = "UPDATEB," + name + "," + str(index)

                        else:
                            command = "UPDATE," + name + "," + str(index)

                        for word in what:
                            command += "," + str(word)
                        command += "\n"

                        self.SlotWrite(command)

                what = proxy.GetDesc()
                if what is not None:
                    command = "UPDATE-DESC," + name + "," + what
                    command += "\n"
                    self.SlotWrite(command)

        self.namesLock.unlock()

    @pyqtSlot()
    def SlotDisconnected(self):
        """
        internal use
        :return:
        """
        self.connectedLock.lock()
        self.connected = False
        self.connectedLock.unlock()

    @pyqtSlot(str)
    def SlotWrite(self, command):
        """
        internal use
        :param command:
        :return:
        """
        if self.isConnected():
            self.xm.write(command.encode("ascii"))

    @pyqtSlot()
    def SlotDataReady(self):
        """
        Internal use
        :return:
        """
        while self.xm.canReadLine():
            data = self.xm.readLine()
            jv = data.data().decode("ascii")
            reader = list(csv.reader(jv.split('\n'), delimiter=','))
            for each in reader:
                if len(each):
                    self.ProcessCommand((each))

    @pyqtSlot()
    def SlotTimerout(self):
        """
        internal use
        :return:
        """
        # if self.xm.state() == QAbstractSocket.UnconnectedState:
        if self.isConnected() is False:
            print("State: ", self.xm.state())
            self.xm.connectToHost(str(self.host), int(self.servicePort))
        else:
            command = "PING\n"
            self.SlotWrite(command)

    @pyqtSlot(str, int)
    def SlotNewHost(self, host, port):
        """
        user can change the                                                                                                                                                             connection, by host and port
        :param host:
        :param port:
        :return:
        """
        self.timer.stop()
        self.host = host
        self.servicePort = port

        if self.isConnected() is True:
            self.xm.close()

        self.SlotTimerout()
        self.timer.start()


# ...................................................................................
class Subscriber(QObject):
    """
    User connects to Multiverse just like c++ code
    Subscribers are used by any user to connect to a name or create a name on Multiverse
    """
    sigUpdateData = pyqtSignal(str, list)
    sigUpdateDesc = pyqtSignal(str, str)
    sigUpdateMultiverse = pyqtSignal(str)

    name = str
    proxy = None
    cloud = None
    userData = None

    functionData = None
    functionDesc = None

    def __init__(self, name: str, cloud: stecQSocket, DataCallBack=None, DescCallBack=None, Parent=None):
        """
        Sunscription
        :param name: Subscription name
        :param cloud: Name of the stecQSocket cloud
        :param DataCallBack: Function a user can recieve data if desired, and if the user does not want to use signals
        :param DescCallBack: Function a user can recieve descciptions if desired, and if the user does not want to use signals
        :param Parent: QObject parent or None
        """
        if Parent is not None:
            super().__init__(Parent)
        else:
            super().__init__()

        self.cloud = cloud
        self.proxy = self.cloud.InsertProxy(name)
        self.name = self.proxy.GetName()
        self.functionData = DataCallBack
        self.functionDesc = DescCallBack
        self.proxy.sigNewDesc.connect(self.newDesc)
        self.proxy.sigNewData.connect(self.newData)
        self.sigUpdateMultiverse.connect(self.cloud.SlotWrite)

        if self.proxy.isActive() is False:
            command = "NOTIFY," + self.name + "\n"
            self.sigUpdateMultiverse.emit(command)
            self.proxy.SetActive()

        else:
            QTimer.singleShot(10, self.StartSingleShot)

        self.proxy.AddSub()

    def deleteLater(self) :
        """
        Deletes later inheritied
        """
        subs = self.proxy.DelSub()
        if subs <= 0 :
            self.proxy.SetActive(False)
            command = "REMOVESUB," + self.name + "\n"
            self.sigUpdateMultiverse.emit(command)

        super().deleteLater()


    def UserData(self):
        """
        Users can attach user data here
        """
        return self.userData

    def SetUserData(self, userData):
        """
        sets user data locally for user to decide what to do with can be anything
        """
        self.userData = userData


    def Data(self):
        """
        :return: The data if it exists
        """
        return self.proxy.GetData()

    def Desc(self):
        """
        :return: Description if exists
        """
        return self.proxy.GetDesc()

    def Name(self):
        return self.Name
    @pyqtSlot(str, list)
    def newData(self, name, data):
        """
        intenal use
        :param name: subscription name
        :param data: Data
        :return:
        """
        self.sigUpdateData.emit(name, data)
        if self.functionData is not None:
            self.functionData(name, data)

    @pyqtSlot(str, str)
    def newDesc(self, name, desc):
        """
        internal use
        :param desc: new description coming from multiverse
        :return:
        """
        if name == self.name:
            self.sigUpdateDesc.emit(self.name, desc)
            if self.functionDesc is not None:
                self.functionDesc(self.name, desc)

    def UpdateData(self, what, index=0):
        """
        User can update multiverse with data
        :param what: Data to send to Muliverse
        :param index:  Zero default, but it can be sent in the middle of an arrary
        :return:
        """
        if len(what):

            if isinstance(what[0], int):
                command = "UPDATEI," + self.name + "," + str(index)

            elif isinstance(what[0], float):
                command = "UPDATEF," + self.name + "," + str(index)

            elif isinstance(what[0], bool):
                command = "UPDATEB," + self.name + "," + str(index)

            else:
                command = "UPDATE," + self.name + "," + str(index)

            for word in what:
                command += "," + str(word)
            command += "\n"

            self.sigUpdateMultiverse.emit(command)
            master = self.proxy.isOwner()
            if master is True and self.cloud.isConnected() is False:
                self.proxy.AddData(what)

    def UpdateDesc(self, what):
        """
        if we are the golden copy, we can send a Malcolm proof descriptor
        :param what: the descriptor
        :return:
        """
        command = "UPDATE-DESC," + self.name + "," + what
        command += "\n"
        self.sigUpdateMultiverse.emit(command)
        master = self.proxy.isOwner()
        if master is True and self.cloud.isConnected() is False:
            self.proxy.AddDesc(what)

    @pyqtSlot()
    def StartSingleShot(self):
        """
        interanl use
        :return:
        """
        data = self.Data()
        if data is not None:
            self.newData(self.name, self.Data())

        desc = self.Desc()
        if desc is not None:
            self.newDesc(self.name, desc)








if __name__ == '__main__':

    from stdcomvsettings import RetensionSettings as RS

    print("stdcomQt")
    import sys

    if "--version" in sys.argv:
        print(stdcomQtVersion)
        sys.exit()

    app = QCoreApplication(sys.argv)
    w = stecQSocket()

    h = Subscriber("hello2", w)
    w.setOwner("hello2", True)

    h.UpdateDesc("Testing")
    h.UpdateData([0, 10, 20])

    hh = Subscriber("hello2", w)
    hh.UpdateData([222, 10, 20])

    residentText = "hello.ressident"
    residentTest =  Subscriber(residentText , w)

    rsetting = RS()
    data = rsetting.GetResidentData(residentText)

    if data is None :

        """ no resident data check for real data"""
        data = residentTest.Data()

        """ No Data has been output yet"""
        if data is None:
            data = ["Testing"]

        """ updata to multiverse """
        residentTest.UpdateData(data)

        """ Save resident data """
        rsetting.SaveResidentData(residentText, data)

    else:
        residentTest.UpdateData(data)




    app.exec_()
    w.quit()
    sys.exit(0)
