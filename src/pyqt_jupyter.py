from qtconsole.qt import QtGui
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager

import sys


class Test(object):
    def __init__(self, input):
        self.input = input

    def __repr__(self):
        return "I am a test haha " + str(self.input)


class ConsoleWidget(RichJupyterWidget):
    def __init__(self, customBanner=None, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        # if customBanner is not None:
        customBanner = "Check 'ghargs': " + str(sys.argv[1]) + "\n%load src/loadenv.py\n\n"
        self.banner = customBanner
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
        self._execute(command, False)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    widget = ConsoleWidget()
    widget.show()
    app.exec_()
