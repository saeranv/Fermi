from silx.gui import qt
from silx.gui.console import IPythonWidget

app = qt.QApplication([])

hello_button = qt.QPushButton("Hello World!", None)
hello_button.show()

console = IPythonWidget()
console.show()
console.pushVariables({"the_button": hello_button})

app.exec_()
