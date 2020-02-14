import ctypes
import collections
import fcntl
import ioctl_opt

BUS_USB = 0x03
BUS_HIL = 0x04
BUS_BLUETOOTH = 0x05
BUS_VIRTUAL = 0x06

class _hidraw_report_descriptor(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint),
        ('value', ctypes.c_ubyte * 4096),
    ]

class _hidraw_devinfo(ctypes.Structure):
    _fields_ = [
        ('bustype', ctypes.c_uint),
        ('vendor', ctypes.c_short),
        ('product', ctypes.c_short),
    ]
HIDIOCGRAWINFO = ioctl_opt.IOR(ord('H'), 0x03, _hidraw_devinfo)
HIDIOCSFEATURE = lambda len: ioctl_opt.IOC(ioctl_opt.IOC_WRITE|ioctl_opt.IOC_READ, ord('H'), 0x06, len)
DevInfo = collections.namedtuple('DevInfo', ['bustype', 'vendor', 'product'])


def getInfo(device):
    devinfo = _hidraw_devinfo()
    result = fcntl.ioctl(device, HIDIOCGRAWINFO, devinfo, True)
    """ioctl(_HIDIOCGRAWINFO, devinfo, True)"""
    return DevInfo(devinfo.bustype, devinfo.vendor, devinfo.product)

def sendFeatureReport(device, report, report_num=0):
    """
    Send a feature report.
    """
    length = len(report) + 1
    buf = bytearray(length)
    buf[0] = report_num
    buf[1:] = report
    fcntl.ioctl(device,HIDIOCSFEATURE(length),(ctypes.c_char * length).from_buffer(buf),True)