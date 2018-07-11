from IPython.lib import guisupport
import sys
import os

from PyQt4 import QtGui
import pprint
pp = pprint.pprint
import IPython
from IPython.kernel.inprocess.ipkernel import InProcessKernel
#from IPython.qt.inprocess_kernelmanager import QtInProcessKernelManager

#pp(dir(IPython))

def print_process_id():
    print 'Process ID is:', os.getpid()

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


        #self.show()


def main():
    """Create a QT window in Python, or interactively in IPython with QT GUI
    event loop integration.
    """
    print_process_id()

    app = guisupport.get_app_qt4()
    app.references = set()

    window = GUI()
    app.references.add(window)
    window.show()

    guisupport.start_event_loop_qt4(app)



if __name__ == "__main__":
    main()
