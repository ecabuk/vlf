from PyQt4 import QtGui

from ui.intro import Ui_IntroView


class IntroView(QtGui.QWidget, Ui_IntroView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
