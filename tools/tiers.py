import gpsd
import requests

def get_current_location():
   gpsd.connect()
   packet=gpsd.get_current()
   print(packet.position())


get_current_location()