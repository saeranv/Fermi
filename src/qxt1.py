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

from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMessageBox

# for web dev
from PyQt5 import QtWebKitWidgets
#from PyQt5.QtWebEngineWidgets import QWebEngineView

# needs to be imported
#from PyQt5 import QtSvg

import pprint
pp = pprint.pprint

#import qdarkstyle

import sys
import os

CURR_DIRECTORY = os.path.abspath(os.path.dirname("__file__"))


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
        self.banner = "HYPER-SPACE\n\n" + customBanner
        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=True)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        # test this
        #t = Test(14)
        #t1 = Test(26)
        #D = {"t": t, "ti": t1, "ghargs": sys.argv}

        #kernel = kernel_manager.kernel
        #kernel.shell.push(D)

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

class GUIWidget(QtWebKitWidgets.QWebView):
    def __init__(self, parent=None):
        super(GUIWidget, self).__init__(parent)

        html_url = QtCore.QUrl.fromLocalFile(os.path.join(CURR_DIRECTORY, "src","trnco_fe","trnco_fe.html"))
        self.load(html_url)
        #viewer.setHtml(HTML, img_url)

class MainWidget(QtWidgets.QMainWindow):
    # Main GUI Window including a button and IPython Console widget inside vertical layout
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle('hpr')
        self.mainWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.mainWidget)
        layout = QtWidgets.QVBoxLayout(self.mainWidget)

        # frontend widget
        viewer = GUIWidget()

        # console widget
        getghargs = str(sys.argv[1]) if len(sys.argv)>1 else "None"
        doc = ("Check GH args: " + getghargs + "\n"
        "%run -m src.openstudio_python $osmfile\n"
        "%run -m src.loadenv\n"
        "!clear to clear screen\n"
        "Batch scripts:\n"
        "%run -m src.run_batch start\n"
        "%run -m src.run_batch git\n"
        "PID: {}\n".format(os.getpid())
        )


        self.ipyConsole = ConsoleWidget(customBanner = doc)

        monokai = qtconsole.styles.default_dark_style_sheet
        self.ipyConsole.style_sheet = monokai

        self.ipyConsole.execute_command("%run -m src.loadenv")
        self.ipyConsole.execute_command("%matplotlib inline\n")

        self.ipyConsole.push_vars({"doc": doc})
        #self.ipyConsole._append_plain_text(doc)


        #self.ipyConsole.setFixedSize(400, 400)

        layout.addWidget(viewer)
        layout.addWidget(self.ipyConsole)

        # set size

        viewer.setMinimumWidth(470)
        viewer.setMinimumHeight(450)
        viewer.setMaximumHeight(450)
        self.ipyConsole.setMinimumHeight(300)
        self.resize(470,750)

        #pp(dir(layout))
        # This allows the variable foo and method print_process_id to be accessed from the ipython console
        #ipyConsole.pushVariables({"foo":43,"print_process_id":print_process_id})
        #ipyConsole.printText("The variable 'foo' and the method 'print_process_id()' are available. Use the 'whos' command for information.\n\nTo push variables run this before starting the UI:\n ipyConsole.pushVariables({\"foo\":43,\"print_process_id\":print_process_id})")

        #self.setGeometry(40, 40, 300, 300)
        self.move(40,40)

        self.show()

    def resizeEvent(self, event):
        #self.resized.emit()
        return self.ipyConsole.resizeEvent(event)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

        elif event.key() == QtCore.Qt.Key_Alt:
            #error_dialog = QtWidgets.QErrorMessage()
            #error_dialog.showMessage('Oh no!')
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Show")
            msg.setText("This is a test of the Q Message.\nThis is the second line.\n")
            #msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            retval = msg.exec_()


def print_process_id():
    print('Process ID is:', os.getpid())

def onFileSystemChanged(path):
    print(path)
    print('testing')
def main():
    print_process_id()

    app = QtWidgets.QApplication([])
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt())
    app.setWindowIcon(QtGui.QIcon(os.path.join(CURR_DIRECTORY,"src/trnco_fe/img/tmplogo.png")))

    file = QFile(os.path.join(CURR_DIRECTORY,"src","trnco_fe","qdarkstyle_custom.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    widget = MainWidget()

    #widget.show()
    """
    # W file watcher use this to track different images
    # https://stackoverflow.com/questions/13518985/why-does-qfilesystemwatcher-work-for-directories-but-not-files-in-python
    # http://blog.mathieu-leplatre.info/filesystem-watch-with-pyqt4.html
    paths = [
        os.path.join(CURR_DIRECTORY, "src","trnco_fe","img"),
        os.path.join(CURR_DIRECTORY, "src","trnco_fe","img","2.jpg")
        ]
    # Set up file system watcher
    qfsw = QtCore.QFileSystemWatcher()
    qfsw.addPaths(paths)
    QtCore.QObject.connect(qfsw, QtCore.SIGNAL("directoryChanged(QString)"),onFileSystemChanged)
    QtCore.QObject.connect(qfsw, QtCore.SIGNAL("fileChanged(QString)"),onFileSystemChanged)

    # Allow program to be interrupted with Ctrl+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # end file watching
    """

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
