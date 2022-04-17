#https://wiki.seeedstudio.com/LAN_Communications/

import network
import usocket
from machine import Pin, I2C, ADC, UART, SPI, PWM
from time import sleep
 
N1 = network.WLAN_SPI(network.STA_IF)
N1.active(True)
 
print("API list:")
dir(N1)
 
print("wifi list:")
lis = N1.scan()
for q in lis:
    print(q)
# https://docs.micropython.org/en/v1.9.3/wipy/library/network.html
N1.connect("password","ssid")
if N1.isconnected():
    print("    ip               gateway           netmask            MAC            ssid")
    N1.ifconfig(config=('dhcp'))
    print(N1.ifconfig())
    s=usocket.socket()
    addr=('192.168.1.23',9999)
    s.connect(addr)
    s.send('Hello! Wio RP2040')
