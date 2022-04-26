import network
import usocket
from machine import Pin, I2C, ADC, UART, SPI, PWM
from time import sleep
 
N1 = network.WLAN_SPI(network.STA_IF)
N1.active(True)
print(N1.ifconfig())

print("API list:")
dir(N1)
 
print("wifi list:")
lis = N1.scan()
for q in lis:
    print(q)
 
N1.connect("name_ssid_ohkod","key_____")
if N1.isconnected():
    print("    ip               gateway           netmask            MAC            ssid")
    print(N1.ifconfig())
    s=usocket.socket()
    addr=('192.168.1.46',9999)
    s.connect(addr)
    s.send("wio avec ohkod")
