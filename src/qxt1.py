
from __future__ import print_function
from loadenv import *
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
import dataframe2html as dfhtml
import parse_osm

import pprint
pp = pprint.pprint

#import qdarkstyle

import sys
import os

CURR_DIRECTORY = os.path.abspath(os.path.dirname("__file__"))


# https://stackoverflow.com/questions/29421936/cant-quit-pyqt5-application-with-embedded-ipython-qtconsole


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

class ConsoleWidget(RichJupyterWidget):
    def __init__(self, customBanner=None, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        # console widget
        getghargs = str(sys.argv[1]) if len(sys.argv)>1 else "None"
        doc = ("Check GH args: " + getghargs + "\n"
            "%run -m src.load_osm $osmfile DEPRECATED!\n"
            "%run -m src.loadenv\n"
            "!clear to clear screen\n"
            "Batch scripts:\n"
            "%run -m src.run_batch start\n"
            "%run -m src.run_batch git\n"
            "Ctrl A: reload html\n"
            "Ctrl Q: quit\n"
            "PID: {}\n".format(os.getpid())
            )

        self.banner = "qxt\n\n" + doc
        self.font_size = 6

        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        monokai = qtconsole.styles.default_dark_style_sheet
        self.style_sheet = monokai

        self.execute_command("%run -m src.loadenv")
        self.execute_command("%matplotlib inline\n")

        self.push_vars({"doc": doc})

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            get_app_qt5().exit()
        #self.exit_requested.connect(stop)


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

        self.html_url = QtCore.QUrl.fromLocalFile(os.path.join(CURR_DIRECTORY, "src","trnco_fe","trnco_fe.html"))
        self.load(self.html_url)
        #viewer.setHtml(HTML, img_url)

class MainWidget(QtWidgets.QMainWindow):
    # Main GUI Window including a button and IPython Console widget inside vertical layout
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle('hpr')
        self.mainWidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.mainWidget)

        self.layout = QtWidgets.QVBoxLayout(self.mainWidget)

        # frontend widget
        self.viewer = GUIWidget()
        self.ipyConsole = ConsoleWidget()

        # Add widgets to layout
        self.layout.addWidget(self.viewer)
        self.layout.addWidget(self.ipyConsole)

        # set size
        self.viewer.setMinimumWidth(470)
        self.viewer.setMinimumHeight(450)
        self.viewer.setMaximumHeight(450)
        self.ipyConsole.setMinimumHeight(300)

        self.resize(470,750)
        self.move(40,40)
        self.show()

    def resizeEvent(self, event):
        #self.resized.emit()
        return self.ipyConsole.resizeEvent(event)

    def showMsg(self, msg_text="default msg"):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Show")
        msg.setText(msg_text)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()

    def keyPressEvent(self, event):

        key = event.key()
        modifier = QtWidgets.QApplication.keyboardModifiers()

        if modifier == QtCore.Qt.ControlModifier:
            if key == QtCore.Qt.Key_D:

                # get json of df
                df,osm,ops = parse_osm.main()
                N = df.shape[1]
                new_dict = {}
                new_dict["df"] = df
                new_dict["osm"] = osm


                self.ipyConsole.push_vars(new_dict)
                self.showMsg("pushed vars")

                #N = 10
                #df = pd.DataFrame(index=range(N))
                #df['x'] = range(10)
                #df['y'] = range(10)

                #dfhtml.get_html(df,N)
                #dfhtml.to_frontend()

                #self.viewer.load(self.viewer.html_url)

                self.ipyConsole.print_text("'DataFrame pushed'")
                print('hello')

            elif key == QtCore.Qt.Key_Q:

                self.close()

            elif key == QtCore.Qt.Key_M:
                self.showMsg("Msg from M")




def print_process_id():
    print('Process ID is:', os.getpid())

def get_app_qt5(*args, **kwargs):
    """Create a new qt5 app or return an existing one."""
    app = QtWidgets.QApplication.instance()
    if app is None:
        if not args:
            args = ([''],)
        app = QtWidgets.QApplication(*args, **kwargs)
    return app

def main():

    print_process_id()

    app  = get_app_qt5()

    app.setWindowIcon(QtGui.QIcon(os.path.join(CURR_DIRECTORY,"src/trnco_fe/img/tmplogo_pink.png")))
    file = QFile(os.path.join(CURR_DIRECTORY,"src","trnco_fe","qdarkstyle_custom.qss"))
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    widget = MainWidget()

    widget.show()
    #app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
