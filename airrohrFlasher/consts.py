import sys

from .qtvariant import QtCore


# Firmware update repository
UPDATE_REPOSITORY = 'https://www.open4me.de/service/littleyoda-DCC-Decoder-Flasher/flash.csv'


# URI prefixes (protocol parts, essentially) to be downloaded using requests
ALLOWED_PROTO = ('https://')

# vid/pid pairs of known NodeMCU/ESP8266 development boards
PREFERED_PORTS = [
    # CH341
    (0x1A86, 0x7523),

    # CP2102
    (0x10c4, 0xea60),
]

ROLE_DEVICE = QtCore.Qt.UserRole + 1
ROLE_DNSSD_NAME = QtCore.Qt.UserRole + 2
ROLE_DNSSD_ADDR = QtCore.Qt.UserRole + 3
ROLE_DNSSD_INFO = QtCore.Qt.UserRole + 4

if sys.platform.startswith('darwin'):
    DRIVERS_URL = 'http://www.wch.cn/downloads/CH341SER_MAC_ZIP.html'
elif sys.platform.startswith(('cygwin', 'win32')):
    DRIVERS_URL = 'http://www.wch.cn/downloads/CH341SER_ZIP.html'
else:
    DRIVERS_URL = None
