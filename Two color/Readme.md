Code:  
from machine import Pin  
import time  

ledR = Pin(16, Pin.OUT)  
ledG = Pin(17, Pin.OUT)  

while True:  
        ledR.toggle  

        print("Color change")  
        ledG.toggle()  
        time.sleep(3)  

https://www.loom.com/share/39dee081302e438d9db0027aab573069
