import os
from PyQt4 import QtGui

from ui.license import Ui_LicenseView
from settings import BASE_PATH


class LicenseView(QtGui.QWidget, Ui_LicenseView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Text
        txt = open(os.path.join(BASE_PATH, 'LICENSE'))
        self.license_txt.setHtml("""<pre style="font-family:monospace;">%s</pre>""" % txt.read())
        txt.close()

        self.button_close.clicked.connect(self.close)
