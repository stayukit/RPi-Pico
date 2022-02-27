from machine import Pin, I2C
from pico_i2c_lcd import I2cLcd
import utime as time

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16) # LCD 16x2 # class run lcd

######## TEST ########
def loop(n, tset=0.3, tblank=0.5):
    #lcd.backlight_on()
    lcd.clear()
    a = ' '
    for i in range(n):
        if i%2 == 0:
            a = str(int(i/2))
            t = tset
        elif i%2 != 0:
            a = ' '
            t = tblank
        #lcd.clear()
        lcd.putstr('BOOTCAMP_IoT_EP{}\nRPi_Pico+LCD16x2'.format(a))
        time.sleep(t)
    lcd.putstr('BOOTCAMP_IoT_EP{}\nRPi_Pico+LCD16x2'.format('0'))
#lcd.blink_cursor_on()      
#loop(20, tset = 0.5)
#loop(20, tblank=0.1)


######## LCD 16x2 ########
text_for_cir = '  BOOTCAMP_IoT  RPi_Pico+LCD16x2'
line1 = '  BOOTCAMP_IoT  '
line2 = 'RPi_Pico+LCD16x2'
blank = '                '

#for x in reversed(line2):
#    print(x)
def rev(data=''):
    dt = ''
    for x in reversed(data):
        dt += x
    return dt

lcd.clear()
time.sleep(2)
#lcd.putstr('{}\n{}'.format(line1, line2))

for i in range(len(text_for_cir)):
    print('i',i)
    status = 'run'
    if i == 16:
        pass
        #line2 = rev('  BOOTCAMP_IoT  ') # flip left-right
        #line1 = rev('RPi_Pico+LCD16x2')
    elif i > 16 and i <= 31:
        i = (i)%16
    elif i == 32:
        i = 16
        status = 'end'
    l1to2 = ''
    l1 = ''
    l2to1 = ''
    l2 = ''
    print('i-2',i)
    for n in range(16):
        print(i, n)
        # line2
        val2 = n - i
        if val2 < 0:
            l2to1 += line2[int(abs(val2+1))]
        elif val2 >= 0:
            l2 += line2[n] #line2[val2]
        # line1
        val1 = n + i
        if val1 > 15:
            l1to2 += line1[15 - val1]
        else:
            l1 += line1[n]
    if l2to1 != '':
        #l2to1 = rev(l2to1)
        #l1to2 = rev(l1to2)
        pass
    showl1 = l2to1 + l1
    showl2 = l2 + l1to2
    lcd.putstr('{}\n{}'.format(showl1, showl2))
    time.sleep(1.5)
    #lcd.putstr('{}\n{}'.format(blank, blank))
    if i == 16 and status == 'run':
        #pass
        line2 = rev('  BOOTCAMP_IoT  ') # flip left-right
        line1 = rev('RPi_Pico+LCD16x2')
    #time.sleep(0.3)

line1 = '  BOOTCAMP_IoT  '
line2 = 'RPi_Pico+LCD16x2'
lcd.putstr('{}\n{}'.format(line1, line2))