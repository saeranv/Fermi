#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
# https://stackoverflow.com/questions/29421936/cant-quit-pyqt5-application-with-embedded-ipython-qtconsole

from __future__ import print_function

#qtgui
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
import qtconsole

from IPython.lib import guisupport
from IPython.lib.kernel import connect_qtconsole
from ipykernel.kernelapp import IPKernelApp

from PyQt4 import QtGui, QtWebKit, QtCore, Qt
from PyQt4.QtCore import QFile, QTextStream

import pprint
pp = pprint.pprint

import qdarkstyle

import sys
import os

CURR_DIRECTORY = os.path.abspath(os.path.dirname("__file__"))


HTML = """
<html>
   <head>
      <title>QtWebKit Plug-in Test</title>
   </head>
   <body bgcolor="#000">
      <!-- <p style="color:white">hyper-xspace</p> -->
      <img src="C:/saeran/master/git/Fermi/src/img/2.jpg" width="390">
   </body>
</html>
"""


#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------
"""
def mpl_kernel(gui):
    #Launch and return an IPython kernel with matplotlib support for the desired gui

    kernel = IPKernelApp.instance()
    kernel.initialize(['python', '--matplotlib=%s' % gui,
                       #'--log-level=10'
                       ])
    return kernel
"""
def print_process_id():
    print('Process ID {}'.format(os.getpid()))

class Test(object):
    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return "I am a test haha " + str(self.input)

class ConsoleWidget(RichJupyterWidget):
    def __init__(self, customBanner=None, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        # if customBanner is not None:
        """
        if len(sys.argv) > 1:
            customBanner = "{}{}{}{}{}".format(
                "Check 'ghargs': ",
                str(sys.argv[1]),
                "\n%run -m src.loadenv\n",
                "%run -m src.openstudio_python $osmfile\n",
                "%matplotlib inline\n"
                )
        """
        self.banner = "HYPER-SPACE\n\n"
        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        # test this
        t = Test(14)
        t1 = Test(26)
        D = {"t": t, "ti": t1, "ghargs": sys.argv}
        kernel = kernel_manager.kernel
        kernel.shell.push(D)

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt().exit()

        self.exit_requested.connect(stop)

    def push_vars(self, variableDict):
        """
        Given a dictionary containing name / value pairs, push those variables
        to the Jupyter console widget
        """
        self.kernel_manager.kernel.shell.push(variableDict)

    def clear(self):
        """
        Clears the terminal
        """
        self._control.clear()

        # self.kernel_manager

    def print_text(self, text):
        """
        Prints some plain text to the console
        """
        self._append_plain_text(text)

    def execute_command(self, command):
        """
        Execute a command in the frame of the console widget
        """
        self._execute(command, True)


class ExampleWidget(QtGui.QMainWindow):
    # Main GUI Window including a button and IPython Console widget inside vertical layout
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)
        self.setWindowTitle('hpr')
        self.mainWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.mainWidget)
        layout = QtGui.QVBoxLayout(self.mainWidget)

        #self.button = QtGui.QPushButton('Another widget')

        viewer = QtWebKit.QWebView()
        viewer.setHtml(HTML)
        viewer.setFixedSize(410, 370)
        customBanner="Welcome to the embedded ipython console\n"

        ipyConsole = ConsoleWidget()

        monokai = qtconsole.styles.default_dark_style_sheet
        ipyConsole.style_sheet = monokai

        ipyConsole.execute_command("%run -m src.loadenv")
        ipyConsole.execute_command("%matplotlib inline\n")

        instructions = "{}{}{}{}".format(
            "Check 'ghargs': ",
            str(sys.argv[1]) if len(sys.argv)>1 else "Null",
            "%run -m src.openstudio_python $osmfile\n",
            "PID: "+str(os.getpid())
            )
        ipyConsole.print_text(instructions)


        ipyConsole.setFixedSize(400, 500)

        layout.addWidget(viewer)
        layout.addWidget(ipyConsole)

        #pp(dir(layout))
        # This allows the variable foo and method print_process_id to be accessed from the ipython console
        #ipyConsole.pushVariables({"foo":43,"print_process_id":print_process_id})
        #ipyConsole.printText("The variable 'foo' and the method 'print_process_id()' are available. Use the 'whos' command for information.\n\nTo push variables run this before starting the UI:\n ipyConsole.pushVariables({\"foo\":43,\"print_process_id\":print_process_id})")

        #self.setGeometry(10, 10, 300, 300)

def print_process_id():
    print('Process ID is:', os.getpid())

def main():
    print_process_id()

    app = QtGui.QApplication([])
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    app.setWindowIcon(QtGui.QIcon("C:/saeran/master/git/Fermi/src/img/logo.jpg"))

    file = QFile(os.path.join(CURR_DIRECTORY,"src","qdarkstyle.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    widget = ExampleWidget()

    widget.show()

    app.exec_()

if __name__ == '__main__':
    main()
