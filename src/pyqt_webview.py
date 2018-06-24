import sys

from PyQt4 import QtGui, QtWebKit, QtCore
from PyQt4.QtGui import QApplication, QCalendarWidget


HTML = """
<html>
   <head>
      <title>QtWebKit Plug-in Test</title>
   </head>
   <body>
      <h1>Hello, World!</h1>
      <object type="application/x-qt-plugin" classid="MyCalendarWidget" name="calendar" height=300 width=500></object>
      <script>
         calendar.setGridVisible(true);
         calendar.setCurrentPage(1985, 5);
      </script>
   </body>
</html>
"""

HTML2 = """
<html>
   <head>
      <title>QtWebKit Plug-in Test</title>
   </head>
   <body>
      <h1>Hello, World!</h1>
   </body>
</html>
"""


class MyWebView(QtWebKit.QWebView):

    def __init__(self, parent=None):

        super(MyWebView, self).__init__(parent)

        self._page = MyWebPage(self)
        self.setPage(self._page)


class MyWebPage(QtWebKit.QWebPage):

    def __init__(self, parent=None):

        super(MyWebPage, self).__init__(parent)

        self.settings().setAttribute(QtWebKit.QWebSettings.PluginsEnabled, True)

    def createPlugin(self, classid, url, paramNames, paramValues):

        return MyCalendarWidget(self.view())


class MyCalendarWidget(QCalendarWidget):

    def __init__(self, parent=None):

        super(MyCalendarWidget, self).__init__(parent)

        # Just to prove that this is being used.
        self.setFirstDayOfWeek(QtCore.Qt.Monday)


app = QApplication(sys.argv)

viewer = QtWebKit.QWebView() #MyWebView()
viewer.setHtml(HTML2)
viewer.show()

app.exec_()
