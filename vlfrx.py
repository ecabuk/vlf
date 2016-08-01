import os
import re
import subprocess

STREAM_NAME = 'vlf_app'


def get_device():
    vtcard = subprocess.check_output(['vtcard', '-dq'])
    found = re.search("usb:.*", vtcard.decode("utf-8"))
    return found.group(0)


def start_reading():
    # Start reading
    os.system('vtcard -B -r96000 -c2 -d %s -u @%s' % (get_device(), STREAM_NAME))


def stop_reading():
    # Kill previous instances
    os.system('killall --quiet vtcard')


def wideband_spectrum(resolution, frames, channel=''):
    """
    :param resolution: Resolution (bin width) in hertz
    :param frames: Average up to this many transform frames, then exit
    :param channel: Channel(s)
    :return: list
    """
    data_raw = subprocess.check_output([
        'vtwspec',
        '-r%d' % resolution,
        '-a',
        '-N%d' % frames,
        '@%s:%s' % (STREAM_NAME, channel)
    ])
    data_raw = data_raw.decode("utf-8").split('\n')[:-1]
    ch_c = len(channel.split(','))  # Channel count
    col_c = ch_c * 2  # Column count
    columns = []

    for i in range(col_c):
        columns.append([])

    for row in data_raw:
        data = row.split(' ')
        for c in range(ch_c):
            columns[c * 2].append(data[0])
            columns[c * 2 + 1].append(data[c + 1])

    return columns


def average_amplitudes(sec=1):
    output = subprocess.check_output('vtstat -E %.1f -a r=%.1f @%s' % (
        (sec + 0.1),
        sec,
        STREAM_NAME
    ), shell=True)
    cols = output.decode("utf-8").split(' ')
    return float(cols[3]), float(cols[6])
