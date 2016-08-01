"""
This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.
"""
import sys
import socket
import os

from PyQt4 import QtGui, QtCore

import inclinometer, vlfrx
from settings import SETTINGS, DB_ENGINE, DB_FILE
from views.main import MainView
from views.intro import IntroView


class MainWindow(QtGui.QMainWindow):
    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)
        self.setCentralWidget(IntroView())

        QtCore.QTimer.singleShot(SETTINGS.value('common/intro_length', 5000), self._start_main_view)

    def _start_main_view(self):
        self.setCentralWidget(MainView())


if __name__ == '__main__':
    # Run single process at once
    try:
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # Create an abstract socket, by prefixing it with null.
        s.bind('\0vlf1500_single_notify_lock')
    except socket.error:
        print('Process already running. Exiting...')
        sys.exit(0)

    app = QtGui.QApplication(sys.argv)

    # Create DB file if not exist
    if not os.path.isfile(DB_FILE):
        from models import Base

        Base.metadata.create_all(DB_ENGINE)

    # Hide cursor
    app.setOverrideCursor(QtCore.Qt.BlankCursor)

    window = MainWindow()

    # Full screenw
    window.showFullScreen()

    # Start inclinometer readings
    inclinometer.start_readings()

    # Init sound card reading
    QtCore.QTimer.singleShot(2000, vlfrx.start_reading)

    sys.exit(app.exec_())
