#!/usr/bin/env python

from sense_hat import SenseHat
import time, datetime

hat = SenseHat()

hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
hundrefths_color = (127, 127, 0)
off = (0, 0, 0)

hat.clear()

hat.show_message("Programmet Starter", scroll_speed=0.05)

hat.clear()

def display_binary(value, row, color):
    binary_str = "{0:8b}".format(value)
    for x in range(0, 8):
        if binary_str[x] == '1':
            hat.set_pixel(x, row, color)
        else:
            hat.set_pixel(x, row, off)



def vandret():
 while True:
    t = datetime.datetime.now()
    display_binary(t.hour, 3, hour_color)
    display_binary(t.minute, 4, minute_color)
    display_binary(t.second, 5, second_color)
    time.sleep(0.0001)



def display_vertical(value, row, color):
    binary_str = "{0:8b}".format(value)
    for y in range(0, 8):
        if binary_str[y] == '1':
            hat.set_pixel(row, y,color)
        else:
            hat.set_pixel(row, y,off)

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
   
hat.clear()

lodret()
hat.clear()







