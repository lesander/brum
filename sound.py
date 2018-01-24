#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config, time
import RPi.GPIO as GPIO

def init():
    pin = config.piezo['pin']
    GPIO.setup(pin, GPIO.IN)
    GPIO.setup(pin, GPIO.OUT)
    return pin

def buzz(pin, pitch, duration):

    if(pitch==0):
        time.sleep(duration)
        return

    period = 1.0 / pitch                # in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
    delay = period / 2                  # calcuate the time for half of the wave
    cycles = int(duration * pitch)      # the number of waves to produce is the duration times the frequency

    for i in range(cycles):                 # start a loop from 0 to the variable “cycles” calculated above
        GPIO.output(pin, True)              # set pin to high
        time.sleep(delay)                   # wait with pin high
        GPIO.output(pin, False)             # set pin to low
        time.sleep(delay)                   # wait with pin low

def play(tune):
    pin = init()
    x=0

    print("Playing tune ",tune)
    if(tune==1):
        pitches=[262,294,330,349,392,440,494,523, 587, 659,698,784,880,988,1047]
        duration=0.1
        for p in pitches:
            buzz(pin, p, duration)
            time.sleep(duration *0.5)
        for p in reversed(pitches):
            buzz(pin, p, duration)
            time.sleep(duration *0.5)

    elif(tune==2):
        pitches=[262,330,392,523,1047]
        duration=[0.2,0.2,0.2,0.2,0.2,0,5]
        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] *0.5)
            x+=1
    elif(tune==3):
        pitches=[392,294,0,392,294,0,392,0,392,392,392,0,1047,262]
        duration=[0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.8,0.4]
        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] *0.5)
            x+=1

    elif(tune==4):
        pitches=[1047, 988,659]
        duration=[0.1,0.1,0.2]
        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] *0.5)
            x+=1

    elif(tune==5):
        pitches=[1047, 988,523]
        duration=[0.1,0.1,0.2]
        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] *0.5)
            x+=1
