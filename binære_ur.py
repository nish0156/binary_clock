#!/usr/bin/env python
"""
Det Binære Ur- Det viser binære uret i 12timers og 24 timers i både seks søjler lodret og i tre rækker vandret.
LEDerne er brugt til at vise uret som timer, minutter og sekunder 

"""

import sys
from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundrefths_color = (127, 127, 0)
off = (0, 0, 0)
t = datetime.datetime.now()



hat.clear()



def twelve_timer(value):
   if value >= 13:
      value=value -12
      return value
   else:
      return value 

def display_binary(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)
   
def display_vertical(value, row, color):
    binary_str = "{0:8b}".format(value)
    for y in range(0, 8):
        if binary_str[y] == '1':
            hat.set_pixel(row, y,color)
        else:
            hat.set_pixel(row, y,off)



def vandret():
 while True:
    t = datetime.datetime.now()

    display_binary(t.hour, 3, hour_color)
    display_binary(t.minute, 4, minute_color)
    display_binary(t.second, 5, second_color)
    time.sleep(0.0001)






def lodret(): 
 
 while True:
    t = datetime.datetime.now()
    display_vertical((int(t.hour//10)), 2, hour_color)
    display_vertical((int((t.hour%10)//1)), 3, hour_color)
    display_vertical((int(t.minute//10)), 4, minute_color)
    display_vertical((int((t.minute%10)//1)), 5, minute_color)
    display_vertical((int(t.second//10)), 6, second_color)
    display_vertical((int((t.second%10)//1)), 7, second_color)
    time.sleep(0.0001)

def twelve_timer_visning(use_24_hour_format):
    t = datetime.datetime.now()
    if not use_24_hour_format:
        t.hour = twelve_timer(t.hour)
    lodret
    hat.clear()
    



def main():
    hat.show_message("Programmet Starter", scroll_speed=0.05)
    hat.clear()
    
    try:
        while True:
            for event in hat.stick.get_events():
                if event.action == 'pressed':
                    if event.direction == 'up':
                        lodret()
                    elif event.direction == 'down':
                         vandret()

        
            
    except KeyboardInterrupt:
        hat.show_message("Programmet slutter")
        hat.clear()

if __name__ == "__main__":
    main()



   
   











