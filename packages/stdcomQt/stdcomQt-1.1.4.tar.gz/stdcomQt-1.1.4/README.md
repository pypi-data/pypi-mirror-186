Name stdcom
===========

Files
-----

* stdcomQt.py
 



Description
-----------
stdcomQt provides a connection to Stec, Multiverse that is running the NextStep plugin.  It allows python3 users the ability to act on and react to any action made on the Multiverse platorm.
It allows usees to Subscribe from Python 3 moudles and interact with Multiverse just as they were writing C++ plugins.

stdcomqt5  is a PyQt5 version  that can be used in the PyQt5 enviroment, and has all the multi threading precautions built into it.

Changes
-------
 
1.0.04 C++ clone done in python to connect to Multiverse.  This is an alternative to stdcom a pure python version, this needs Qt to operate, but it is much like the c++ already used

1.1.3 makes new tree / can be used 

from stdcomQt import *

 
if __name__ == '__main__':

    print("stdcomQt")
    import sys

    if "--version" in sys.argv:
        print(stdcomQtVersion )
        sys.exit()

    app = QCoreApplication(sys.argv)
    w = stecQSocket()

    h = Subscriber("hello2", w)
    w.setOwner("hello2", True)

    h.UpdateDesc("Testing")
    h.UpdateData([0, 10, 20])

    hh = Subscriber("hello2", w)
    hh.UpdateData([222, 10, 20])

    app.exec_()
    w.quit()
    sys.exit(0)

 
#--------------------- Example Configuration Widgets -----------

from PyQt5.QtWidgets import QApplication
from stdcomutilitywidgets import StecIPconfigDialog, StecPostgresConfigWidget
import  sys, os

if __name__=="__main__":

    current = os.path.dirname(os.path.realpath(__file__))

    # Getting the parent directory name
    # where the current directory is present.
    parent = os.path.dirname(current)

    # adding the parent directory to
    # the sys.path.
    sys.path.append(parent)


    def callBack(ip, port):
        print("Address: ", ip, " Service Port: ", port)
    def cancel() :
        print("Cancel")

    def postCallback( a,b,c,d,e ) :
        print(a,b,c,d,e)

    app = QApplication(sys.argv)
    w = StecIPconfigDialog(callBack, cancel)
    w.show()
    p = StecPostgresConfigWidget(postCallback, cancel)
    p.show()
    sys.exit(app.exec_())