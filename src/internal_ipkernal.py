#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
# https://stackoverflow.com/questions/29421936/cant-quit-pyqt5-application-with-embedded-ipython-qtconsole
import sys
import os

from IPython.lib.kernel import connect_qtconsole
#from IPython.kernel.zmq.kernelapp import IPKernelApp
from ipykernel.kernelapp import IPKernelApp
from IPython.lib import guisupport

from PyQt4 import QtGui, QtWebKit, QtCore

# Import the console machinery from ipython
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager

import pprint
pp = pprint.pprint
#pprint.pprint(dir(QtGui))

HTML = """
<html>
   <head>
      <title>QtWebKit Plug-in Test</title>
   </head>
   <body>
      <h1>Hello, World!</h1>
   </body>
</html>
"""


#-----------------------------------------------------------------------------
# Functions and classes
#-----------------------------------------------------------------------------
def mpl_kernel(gui):
    """Launch and return an IPython kernel with matplotlib support for the desired gui
    """
    kernel = IPKernelApp.instance()
    kernel.initialize(['python', '--matplotlib=%s' % gui,
                       #'--log-level=10'
                       ])
    return kernel

class QIPythonWidget(RichJupyterWidget):
    """ Convenience class for a live IPython console widget.
     We can replace the standard banner using the customBanner argument"""
    def __init__(self,customBanner=None,*args,**kwargs):
        super(QIPythonWidget, self).__init__(*args,**kwargs)
        #if customBanner!=None: self.banner=customBanner

        self.banner = "HYPER-SPACE\n\n"
        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()
        kernel = kernel_manager.kernel

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt().exit()

        self.exit_requested.connect(stop)

    def pushVariables(self,variableDict):
        """ Given a dictionary containing name / value pairs, push those variables to the IPython console widget """
        self.kernel_manager.kernel.shell.push(variableDict)
    def clearTerminal(self):
        """ Clears the terminal """
        self._control.clear()
    def printText(self,text):
        """ Prints some plain text to the console """
        self._append_plain_text(text)
    def executeCommand(self,command):
        """ Execute a command in the frame of the console widget """
        self._execute(command,False)


class ExampleWidget(QtGui.QMainWindow):
    """ Main GUI Window including a button and IPython Console widget inside vertical layout """
    def __init__(self, parent=None):
        super(ExampleWidget, self).__init__(parent)
        self.setWindowTitle('iPython in PyQt5 app example')
        self.mainWidget = QtGui.QWidget(self)
        self.setCentralWidget(self.mainWidget)
        layout = QtGui.QVBoxLayout(self.mainWidget)

        #self.button = QtGui.QPushButton('Another widget')

        viewer = QtWebKit.QWebView()
        viewer.setHtml(HTML)
        viewer.setFixedSize(400, 300)
        customBanner="Welcome to the embedded ipython console\n"

        ipyConsole = QIPythonWidget()
        """
        ipyConsole.setFixedSize(400, 500)

        layout.addWidget(viewer)
        layout.addWidget(ipyConsole)
        """
        #pp(dir(layout))
        # This allows the variable foo and method print_process_id to be accessed from the ipython console
        #ipyConsole.pushVariables({"foo":43,"print_process_id":print_process_id})
        #ipyConsole.printText("The variable 'foo' and the method 'print_process_id()' are available. Use the 'whos' command for information.\n\nTo push variables run this before starting the UI:\n ipyConsole.pushVariables({\"foo\":43,\"print_process_id\":print_process_id})")

        #self.setGeometry(10, 10, 300, 300)

def print_process_id():
    print('Process ID is:', os.getpid())

def main():
    app  = QtGui.QApplication([])
    #widget = ExampleWidget()
    widget = QIPythonWidget()
    #monokai_style_sheet = qtconsole.styles.default_dark_style_sheet
    #widget.style_sheet = monokai

    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
