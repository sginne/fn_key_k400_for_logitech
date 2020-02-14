"""
ad hoc solution for stupid windows keys for kr400+
"""
import os
import hidraw2
fkeys = [0x10, 0x01, 0x09, 0x19, 0x00, 0x00, 0x00] #fkeys on
#fkeys = [0x10, 0x01, 0x09, 0x18, 0x01, 0x00, 0x00] #fkeys off

logitech_vendor=0x46
k400_plus=0x404d



path = "/dev/hidraw"


for i in ['0','1','2']:

    fd=os.open(path+i, os.O_RDWR)
    os.close(fd)
    try:
        fd=os.open(path+i, os.O_RDWR)
        os.set_blocking(fd,False)
        result=hidraw2.getInfo(fd)

        if (result.product==k400_plus):
            print (path+i)
            os.write(fd,bytes(fkeys))
        os.close(fd)
    except FileNotFoundError:
        pass