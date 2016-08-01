from PyQt4 import QtGui
from matplotlib.ticker import FuncFormatter
import alsaaudio

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def translate(context, text, disambig=None):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def translate(context, text, disambig=None):
        return QtGui.QApplication.translate(context, text, disambig)

HZ_2_KHZ_FORMATTER = FuncFormatter(lambda x, pos: round(float(x) / 1000))


def get_mixer():
    return alsaaudio.Mixer(control='Mic', cardindex=1)


def get_mic_vol():
    return get_mixer().getvolume(alsaaudio.PCM_CAPTURE)[0]


def set_mic_vol(vol):
    get_mixer().setvolume(vol, 0, alsaaudio.PCM_CAPTURE)
    get_mixer().setvolume(vol, 1, alsaaudio.PCM_CAPTURE)
