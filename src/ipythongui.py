"""
    ipython_widget
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging

log = logging.getLogger(__name__)


import os

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport


def print_process_id():
    print('Process ID is:', os.getpid())


def terminal_widget(**kwargs):

    # Create an in-process kernel
    # >>> print_process_id()
    # will print the same process ID as the main process
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    kernel = kernel_manager.kernel
    kernel.gui = 'qt4'
    kernel.shell.push(kwargs)

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    control = RichJupyterWidget()
    control.kernel_manager = kernel_manager
    control.kernel_client = kernel_client
    return control

def main():
    # Print the ID of the main process
    print_process_id()

    app = guisupport.get_app_qt4()
    control = terminal_widget(testing=123)

    def stop():
        control.kernel_client.stop_channels()
        control.kernel_manager.shutdown_kernel()
        app.exit()

    control.exit_requested.connect(stop)

    control.show()

    guisupport.start_event_loop_qt4(app)

if __name__ == '__main__':
    main()
