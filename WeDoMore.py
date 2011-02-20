import sys
import usb.core
import usb.util

from array import array

from WeDoDefs import *

WeDo = usb.core.find(idVendor=0x0694, idProduct=0x0003)

if WeDo is None:
	sys.exit("Can't find Lego WeDo")

if WeDo.is_kernel_driver_active(0):
	try:
		WeDo.detach_kernel_driver(0)
	except usb.core.USBError as e:
		sys.exit("Could not detatch kernel driver: %s" % str(e))

endpoint = WeDo[0][(0,0)][0]

print(endpoint.read(64)[-8:])

def WeDoWrite(motorA, motorB):
	motorA = int(motorA)
	motorB = int(motorB)
	magicNumber = 64
	data = [magicNumber, motorA&0xFF, motorB&0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]
	WeDo.ctrl_transfer(bmRequestType = 0x21, bRequest = 0x09, wValue = 0x0200, wIndex = 0, data_or_wLength = data)
