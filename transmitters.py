import os
import json

from PyQt4 import QtGui
from PyQt4.QtCore import QAbstractTableModel, Qt

from settings import ASSETS_DIR
from tools import translate

# Load Countries
COUNTRIES = {}
with open(os.path.join(ASSETS_DIR, 'countries.json'), 'r') as countries_json:
    for country in json.load(countries_json):
        COUNTRIES[country['alpha-2']] = country['name']

# Load Transmitters
TRANSMITTERS = []
with open(os.path.join(ASSETS_DIR, 'transmitters.json'), 'r') as transmitters_json:
    transmitters = sorted(json.load(transmitters_json), key=lambda x: x[0])
    for tx in transmitters:
        TRANSMITTERS.append([float(tx[0]), tx[1]])


class TransmittersTableModel(QAbstractTableModel):
    COL_HEADERS = [
        translate('TransmittersTableModel', 'Frequency'),
        translate('TransmittersTableModel', 'Country')
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def rowCount(self, *args, **kwargs):
        return len(TRANSMITTERS)

    def columnCount(self, *args, **kwargs):
        return len(self.COL_HEADERS)

    def headerData(self, section, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.COL_HEADERS[section]
        return None

    def itemData(self, index):
        return float(TRANSMITTERS[index.row()][0])

    def data(self, index, role=None):
        # All centered except column 1
        if index.column() != 1 and role == Qt.TextAlignmentRole:
            return Qt.AlignCenter | Qt.AlignVCenter

        data = TRANSMITTERS[index.row()][index.column()]

        if index.column() == 0 and role == Qt.DisplayRole:
            return "%.2f kHz" % data
        if index.column() == 1:
            if role == Qt.DecorationRole:
                return QtGui.QPixmap(os.path.join(ASSETS_DIR, 'flags', str(data).lower()))
            elif role == Qt.DisplayRole:
                return COUNTRIES[str(data).upper()]
