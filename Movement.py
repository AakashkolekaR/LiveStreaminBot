#Code for a bot as well as calculating distances


import RPi.GPIO as gpio
import time
import tkinter as tk
from picamera import PiCamera
from measure import *

gpio.setwarnings(False)

def init():
    i=0
    gpio.setmode(gpio.BOARD)
    gpio.setup(8,gpio.OUT)#1st pin a enable
    gpio.setup(10,gpio.OUT)#2nd pin a enable
    gpio.setup(13,gpio.OUT)#1st pin b enable
    gpio.setup(15,gpio.OUT)#2nd pin b enable
    gpio.setup(3,gpio.OUT)#pin 1 forward rear rightssss
    gpio.setup(12,gpio.OUT)#pin 2 backward rear right
    gpio.setup(7,gpio.OUT)#pin 3 backward rear left
    gpio.setup(11,gpio.OUT)#pin 4 forward rear left

    gpio.setup(35,gpio.OUT)#a enable pins
    gpio.setup(37,gpio.OUT)
    gpio.setup(19,gpio.OUT)#b enable
    gpio.setup(21,gpio.OUT)
    gpio.setup(29,gpio.OUT)#left front reverse
    gpio.setup(31,gpio.OUT)#left front forward
    gpio.setup(33,gpio.OUT)#right front reverse
    gpio.setup(36,gpio.OUT)#right front forward

    gpio.output(35,True)
    gpio.output(37,True)
    gpio.output(19,True)
    gpio.output(21,True)

    gpio.output(8,True)
    gpio.output(10,True)
    gpio.output(13,True)
    gpio.output(15,True)

def forward(st):
    gpio.output(12,False)
    gpio.output(3,True)
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(29,False)
    gpio.output(31,True)
    gpio.output(33,False)
    gpio.output(36,True)
    time.sleep(st)
    
def reverse(st):
    gpio.output(12,True)
    gpio.output(3,False)
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(29,True)
    gpio.output(31,False)
    gpio.output(33,True)
    gpio.output(36,False)
    time.sleep(st)
    
def left(st):
    gpio.output(12,False)
    gpio.output(3,True)
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(29,False)
    gpio.output(31,False)
    gpio.output(33,False)
    gpio.output(36,True)
    time.sleep(st)
    
def right(st):
    gpio.output(12,False)
    gpio.output(3,False)
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(29,False)
    gpio.output(31,True)
    gpio.output(33,False)
    gpio.output(36,False)
    time.sleep(st)
    
def stop(st):
    gpio.output(12,False)
    gpio.output(3,False)
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(29,False)
    gpio.output(31,False)
    gpio.output(33,False)
    gpio.output(36,False)
    time.sleep(st)
    gpio.cleanup()
    
def record():
    camera=PiCamera()
    camera.start_recording('/home/pi/project/video.h264')
    time.sleep(6)
    camera.stop_recording()

def keyinput(event):
    init()
    print("Key:",event.char)
    keypress=event.char
    sleeptime=0.060
    
    if keypress.lower()=="f":
        forward(sleeptime)
    elif keypress.lower()=="b":
        reverse(sleeptime)
    elif keypress.lower()=="r":
        right(sleeptime)
    elif keypress.lower()=="l":
        left(sleeptime)
    elif keypress.lower()=="s":
        stop(sleeptime)
    elif keypress.lower()=="c":
        record()
    else:
        pass
    
    dist=distance()
    print("Distance:",dist)
    if dist<15:
        init()
        reverse(0.5)

command=tk.Tk()
command.bind("<KeyPress>",keyinput)
command.mainloop()


gpio.cleanup()
