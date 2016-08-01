import serial
from time import sleep

from PyQt4 import QtCore

from settings import SETTINGS

PORT_LOCK = QtCore.QMutex()
PORT = None
XYThread = None
TThread = None
FF_INDEX = {
    '8000': [0.125, 1],
    '4000': [0.25, 2],
    '2000': [0.5, 3],
    '1000': [1, 4],
    '500': [2, 5],
    '250': [4, 6],
    '125': [8, 7],
    '62': [16, 8],
    '31': [32, 9],
}


class _XYThread(QtCore.QThread):
    """
    X & Y Reading Thread
    """

    updated = QtCore.pyqtSignal(float, float)

    def run(self):
        while True:
            self.updated.emit(*read_xy())
            sleep(SETTINGS.value('inclinometer/xy_freq', 0.1))


class _TThread(QtCore.QThread):
    """
    T Reading Thread
    """

    updated = QtCore.pyqtSignal(float)

    def run(self):
        while True:
            self.updated.emit(read_t())
            sleep(SETTINGS.value('inclinometer/t_freq', 1))


def start_readings():
    """
    Start the reading threads.
    """
    global XYThread, TThread

    # Prepare port
    setup_port()

    # Start XY Thread
    XYThread = _XYThread()
    XYThread.start(QtCore.QThread.NormalPriority)

    # Start T Thread
    TThread = _TThread()
    TThread.start(QtCore.QThread.LowPriority)


def stop_readings():
    """
    Stop the reading threads
    """
    XYThread.terminate()
    TThread.terminate()
    PORT.flushInput()
    PORT.flushOutput()
    PORT_LOCK.unlock()
    PORT.close()


def setup_port():
    """
    Setup and open the serial port
    """
    global PORT
    PORT = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=57600,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=2
    )
    PORT.open()


def set_filter_frequency(id_):
    """
    Set Filter Frequency Response
    :param id_: Filter id
    :type id_: int
    """
    send_command('setflt%d' % id_, 2)


def set_zero():
    """
    Tare function to set the current position to zero
    """
    send_command('setzcur', 2)


def reset_zero():
    """
    Cancels tare function and resets zero to factory setting
    """
    send_command('setzfac', 2)


def send_command(cmd, response_len):
    """
    :param cmd: Command to set
    :param response_len: Reponse length, how many bytes
    :type cmd: str
    :type response_len: int
    """
    # Lock the port
    PORT_LOCK.lock()

    # Send command
    PORT.write(bytes(cmd, 'iso-8859-1'))

    # Read response
    response = PORT.read(response_len)

    # Unlock port
    PORT_LOCK.unlock()

    return response


def read_xy():
    """
    Read X&Y value
    :return: (float, float)
    """
    val = send_command('get-x&y', 8)
    x = float(int.from_bytes(val[4:], 'big', signed=True) / 1000)
    y = float(int.from_bytes(val[:4], 'big', signed=True) / 1000)
    return x, y


def read_t():
    """
    Read temp value
    :return: float
    """
    return float(int.from_bytes(send_command('gettemp', 2), 'big', signed=True) / 100)


def read_ff():
    """
    Read filter frequency value
    :return: float
    """
    ms = int.from_bytes(send_command('get-flt', 2), 'big', signed=True)
    return FF_INDEX[str(ms)][0]
