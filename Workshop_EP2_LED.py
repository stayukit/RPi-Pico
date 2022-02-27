from machine import Pin
import utime
import math

led_order = [13, 14, 15, 17, 19]
loop = 5

# 0.7 s per round
def Blink(no, on=0.10):
    led = Pin(no, Pin.OUT)
    led.on()
    utime.sleep(on)
    led.off()
    utime.sleep(0.04)
    
def Blink2(n1, n2):
    led1 = Pin(n1, Pin.OUT)
    led2 = Pin(n2, Pin.OUT)
    led1.on()
    led2.on()
    utime.sleep(0.10)
    led1.off()
    led2.off()
    utime.sleep(0.04)
    
def LeftToRight(r=loop):
    for i in range(r):
        for N in led_order:
            Blink(N)

def Reflex():
    for i in range(loop):
        if i%2 == 1:
            for N in reversed(led_order):
                Blink(N)
        elif i%2 == 0:
            for N in led_order:
                Blink(N)

def Reflex_con():
    for i in range(loop):
        if i%2 == 1:
            for N in reversed(led_order[:-1]):
                Blink(N)
        elif i%2 == 0:
            for N in led_order[1:]:
                Blink(N)

def Edge_to_Center(n=2):
    qty = len(led_order)
    for i in range(loop*n):
        for N, P in enumerate(led_order, start=1):
            pos = abs(N - math.ceil(qty/2))
            if  pos == 2:
                Blink2(led_order[0], led_order[4])
            elif pos == 1:
                Blink2(led_order[1], led_order[3])
            elif pos == 0:
                Blink(led_order[2])

def two_step():
    for i in range(5):
        #LeftToRight(1)
        for n in led_order:
            Pin(n, Pin.OUT).on()
            for t in led_order:
                led = Pin(t, Pin.OUT)
                led.on()
                utime.sleep(0.10)
                if n != t:
                    led.off()
                utime.sleep(0.04)

            #utime.sleep(0.1)
            Pin(n, Pin.OUT).off()
            utime.sleep(0.01)
 
LeftToRight(2)
Reflex()
Reflex_con()
Edge_to_Center()
two_step()
