#Osman Argueta was here
from machine import Pin, ADC
import time

sensor = ADC(Pin(16))

while True:
    print(sensor.read_u16())% 2 )
    time.sleep(1)