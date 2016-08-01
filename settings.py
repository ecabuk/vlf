import os
import sys
from PyQt4 import QtCore
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Directories
# BASE_PATH = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
BASE_PATH = '/home/pi/Desktop/vlf'
UI_DIR = os.path.join(BASE_PATH, 'ui')
ASSETS_DIR = os.path.join(BASE_PATH, 'assets')
EXPORTS_DIR = os.path.join(BASE_PATH, 'exports')

# Database
DB_FILE = os.path.join(BASE_PATH, 'database.db')
DB_ENGINE = create_engine('sqlite:///%s' % DB_FILE, echo=False)
DB_SESSION_MAKER = sessionmaker(bind=DB_ENGINE)
DB_SESSION = DB_SESSION_MAKER()

# Settings File
SETTINGS = QtCore.QSettings(os.path.join(BASE_PATH, 'settings.ini'), QtCore.QSettings.IniFormat)
