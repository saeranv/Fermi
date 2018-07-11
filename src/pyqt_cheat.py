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
from PyQt4 import QtGui

import pprint
pp = pprint.pprint

#pp(dir(QtGui))

class GUI(QtGui.QWidget):

    def __init__(self):
        super(GUI, self).__init__()

        self.initUI()

    def initUI(self):

        # tooltips are properties of Widget objects
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))    # set font (static method)
        self.setToolTip('This is a <b>QWidget</b> widget')          # set text

        btn = QtGui.QPushButton('Button', self)                 # button object
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # QtWidgets.QWidget is a base class for all user interface objects
        # this is a window
        #w = QtWidgets.QWidget()
        #w.resize(250, 150)  # resizes window launch
        #w.move(300,300)     # move on screen
        self.setGeometry(300,300,250,150) # combines resize and move from obove
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('5.jpg'))


        self.show()


def main():


    app = QtGui.QApplication(sys.argv)
    ex = GUI()


    # mainloop is where event handling occurs
    # mainloop recieves events from windows system and dispatches
    # to the application
    # it ends when we call exit() method or widget is destroyed
    # sys.exit exits cleanly from python by raising an excpetion when window
    # is closed
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
