import binascii
from datetime import datetime
import pytz
import time

# function to transform hex string like "0a cd" into signed integer
def hexStrToInt(hexstr):
  hexstr = hexstr.replace(" ","")
  hexstr = hexstr.replace("0x","")
  bs = binascii.unhexlify(hexstr)
  val = int.from_bytes(bs, byteorder='little')
  return val

def hexStrToBytes(hexstr):
  hexstr = hexstr.replace(" ","")
  return bytearray.fromhex(hexstr)

def intToHexStr(i):
  try:
      hexstr = (i).to_bytes(4, byteorder='little').hex()
      return hexstr
  except:
      return ""

def intToTimeStr(i):
  d = datetime.fromtimestamp(i, tz=pytz.utc)
  tz = pytz.timezone('America/Montreal')
  return d.astimezone(tz).strftime("%Y-%m-%d %H:%M:%S")

def celsiusToFahrenheit(c):
  return c * 1.8 + 32.0

epoch = datetime.utcfromtimestamp(0)

def unix_time_seconds(dt):
    return int((dt - epoch).total_seconds())

def currentTimeInt():
    return int(time.time())
#unix_time_seconds(datetime.now())

def bytesToInt(bs):
    val = int.from_bytes(bs, byteorder='little')
    return val

def bytesToHexStr(bs):
    return bs.hex()
