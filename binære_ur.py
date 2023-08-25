#!/usr/bin/env python
"""
Det Binære Ur- Det viser binære uret i 12timers og 24 timers i både seks søjler lodret og i tre rækker vandret.
LEDerne er brugt til at vise uret som timer, minutter og sekunder 

"""

import argparse
from sense_hat import SenseHat
import time, datetime
import sys
import signal

hat = SenseHat()



hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
off = (0, 0, 0)




hat.clear()

def signal_term_handler(signal, frame):
     """Funktion til at afslutte programmet"""
     hat.show_message("Programmet slutter",scroll_speed=0.05)
     print ('got SIGTERM')
     sys.exit(0)

def signal_int_handler(signal, frame):
    """Funktion til at afslutte programmet"""
    hat.show_message("Programmet slutter",scroll_speed=0.05)
    print('got SIGTINT, fra keyboard')
    sys.exit(0)
 
signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_int_handler)



def twelve_timer(value):
   if value >= 13:
      value=value -12
      return value
   else:
      return value 

def display_binary(value, row, color):
    """Funktion til at sætte binære uret i vandret """
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)
   
def display_vertical(value, column, color):
    """Funktion til at sætte binære uret i lodret """
    binary_str = "{0:8b}".format(value)
    for y in range(0, 8):
        if binary_str[y] == '1':
            hat.set_pixel(column, y,color)
        else:
            hat.set_pixel(column, y,off)



def vandret(event):
   """Funktion til at vise uret i vandret  og i 24 timer format"""
   global direction, timer
   direction="vandret"
   timer=24
   hat.clear()



def lodret(event): 
   """Funktion til at vise uret i lodret  og i 24 timer format"""

   global direction, timer
   direction="lodret"
   timer=24
   hat.clear()


def vandret_12(event):
   """Funktion til at vise uret i vandret  og i 12 timer format"""
   global direction, timer
   direction="vandret"
   timer=12
   hat.clear()
   print('12 timer visning')


    
def lodret_12(event):
   """Funktion til at vise uret i lodret  og i 12 timer format"""
   global direction, timer
   direction="lodret"
   timer=12
   hat.clear()
   print('12 timer visning')


"""funktionerne er lagt til joystick direktion.
    Når joysticket er trykket så er funktion kaldt """
hat.stick.direction_up = vandret
hat.stick.direction_down =lodret
hat.stick.direction_left= vandret_12
hat.stick.direction_right= lodret_12




def main():
    global direction, timer
    timer=12
    direction="vandret"
    
    parser=argparse.ArgumentParser(description="Det binære ur viser tiden i binære form i 4 forskellige format ")

    parser.add_argument('-d',action='store', dest='direction',default='vandret',help='vandret eller lodret ')
    parser.add_argument('-t',action='store', dest='timer',default='24',help='12 hr eller 24 hr ')
    args=parser.parse_args()

    print(args.direction)
    print(args.timer)


    direction=args.direction
    timer=args.timer



    hat.clear()


    hat.show_message("Programmet Starter", scroll_speed=0.05)
    hat.clear()
    
    
    while True:
          t=datetime.datetime.now()
          if(timer==12):
            h=twelve_timer(t.hour)
          else:
              h=t.hour

          if(direction=="vandret"):
             """Viser binære uret i tre rækker i vandrettet direktion"""
             display_binary(h, 3, hour_color)
             display_binary(t.minute, 4, minute_color)
             display_binary(t.second, 5, second_color)
             time.sleep(0.0001)
          
          if(direction=="lodret"):
           """Viser binære uret i seks søjler vandret"""

           display_vertical((int(h//10)), 2, hour_color)
           display_vertical((int((h%10)//1)), 3, hour_color)
           display_vertical((int(t.minute//10)), 4, minute_color)
           display_vertical((int((t.minute%10)//1)), 5, minute_color)
           display_vertical((int(t.second//10)), 6, second_color)
           display_vertical((int((t.second%10)//1)), 7, second_color)
           time.sleep(0.0001)
 
   

if __name__ == "__main__":
    main()



   
   
