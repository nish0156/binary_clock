#!/usr/bin/env python
"""
Det Binære Ur- Det viser binære uret i 12timers og 24 timers i både seks søjler lodret og i tre rækker vandret.
LEDerne er brugt til at vise uret som timer, minutter og sekunder 

"""

import sys
from sense_emu import SenseHat,ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time, datetime

hat = SenseHat()

x = True
y = True


hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundrefths_color = (127, 127, 0)
off = (0, 0, 0)



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



def vandret(event):
   global direction, timer
   direction="vandret"
   timer=24



def lodret(event): 
   global direction, timer
   direction="lodret"
   timer=24

def vandret_12(event):
   global direction, timer
   direction="vandret"
   timer=12
    
def lodret_12(event):
   global direction, timer
   direction="lodret"
   timer=12



hat.stick.direction_up = vandret
hat.stick.direction_down =lodret
hat.stick.direction_left= vandret_12
hat.stick.direction_right= lodret_12





def main():
    global direction, timer
    timer=12
    direction="vandret"
    hat.show_message("Programmet Starter", scroll_speed=0.05)
    hat.clear()
    
    try:
        while True:
          t=datetime.datetime.now()
          if(timer==12):
            twelve_timer(t.hour)

          if(direction=="vandret"):
             display_binary(t.hour, 3, hour_color)
             display_binary(t.minute, 4, minute_color)
             display_binary(t.second, 5, second_color)
             time.sleep(0.0001)
          
          if(direction=="lodret"):
           display_vertical((int(t.hour//10)), 2, hour_color)
           display_vertical((int((t.hour%10)//1)), 3, hour_color)
           display_vertical((int(t.minute//10)), 4, minute_color)
           display_vertical((int((t.minute%10)//1)), 5, minute_color)
           display_vertical((int(t.second//10)), 6, second_color)
           display_vertical((int((t.second%10)//1)), 7, second_color)
           time.sleep(0.0001)
 
    except KeyboardInterrupt:
        hat.show_message("Programmet slutter")
        hat.clear()

if __name__ == "__main__":
    main()



   
   
