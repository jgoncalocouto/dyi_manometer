from machine import Pin, I2C, ADC, Timer
from ssd1306 import SSD1306_I2C
import framebuf
import time

WIDTH=128
HEIGHT=64
conversion_factor = 3.3 / (65535)


sensor_temp = machine.ADC(4)
i2c=I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)
oled=SSD1306_I2C(WIDTH,HEIGHT,i2c)
led = Pin(25, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=20, mode=Timer.PERIODIC, callback=blink)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    oled.poweroff()
    time.sleep(0.0001)
    oled.poweron()
    oled.fill(0)
    #oled.text("T = "+str(round(temperature,2))+" [degC]",0,0,1)
    oled.text("1234567890123456",0,1,1)
    oled.text("1234567890123456",0,9,1)
    oled.text("1234567890123456",0,17,1)
    oled.text("1234567890123456",0,25,1)
    oled.text("1234567890123456",0,33,1)
    oled.text("1234567890123456",0,41,1)
    oled.text("1234567890123456",0,49,1)
    oled.text("1234567890123456",0,57,1)

    oled.show()
    time.sleep(1)

    
    



