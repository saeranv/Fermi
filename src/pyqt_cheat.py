#!/usr/bin/env python
# tells *nix distributions to find python interpreter
# -*- coding: utf-8 -*-

"""
PyQt main classes

QtCore
- core non GUI functionality
- work w/ files/dir/streams/urls/threads/processes
QtGui
- graphical components and related classes
- i.e buttons, windows, status bars, fonts etc
QtNetwork
- classes for network programming
- i.e TCP/IP, UDP clinets and servers
QtXml
- classes for XML files
QtSvg
- svg files (2d graphics in XML format)
QtOpenGL
- rendering 3D and 2D graphics
QtSql
- seamless integration of Qt GUI library

"""

import sys
from PyQt5 import QtGui, QtWidgets


def main():
    # application object
    # sys.argv = list of arguments
    app = QtWidgets.QApplication(sys.argv)

    # base class for all user interface objects
    # this is a window
    w = QtWidgets.QWidget()
    w.resize(250, 150)  # resizes window launch
    w.move(300,300)     # move on screen
    w.setWindowTitle('Simple')

    w.show()

    # mainloop is where event handling occurs
    # mainloop recieves events from windows system and dispatches
    # to the application
    # it ends when we call exit() method or widget is destroyed
    # sys.exit ensures clean exit
    print(app.exec_.__doc__)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    #app = QtWidgets.QApplication(sys.argv)
    #mainWin = HelloWindow()
    #mainWin.show()
    #sys.exit( app.exec_() )
