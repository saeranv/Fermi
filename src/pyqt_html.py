
import sys
import os
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets

if sys.platform.startswith( 'linux' ) : from OpenGL import GL

sys.argv.append("--disable-web-security")
app = QtWidgets.QApplication(sys.argv)
view = QtWebEngineWidgets.QWebEngineView()


view.load(QtCore.QUrl().fromLocalFile(os.path.join("C:/saeran/master/git/Fermi/src/pyqt.html")))

view.show()
sys.exit(app.exec_())
