#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum
# start.py

import config, time
import RPi.GPIO as GPIO

# Initialize the piezo pin.
def init():
    pin = config.piezo['pin']
    GPIO.setup(pin, GPIO.IN)
    GPIO.setup(pin, GPIO.OUT)
    return pin

# Create a buzz as part of a tune.
def buzz(pin, pitch, duration):

    if (pitch == 0):
        time.sleep(duration)
        return

    # In physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec).
    # After determining the period, we calcuate the time for half of the wave.
    # After that, we know the number of waves to produce is the duration, times the frequency.
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)

    # We start a loop from 0 to the variable cycles calculated above.
    # We then set the pin to high, wait with the pin on high and then
    # set the pin to low again, and wait with the pin on low.
    for i in range(cycles):
        GPIO.output(pin, True)
        time.sleep(delay)
        GPIO.output(pin, False)
        time.sleep(delay)

# Play the given tune using a preset format of pitches.
# We loop through the pitches and then create short buzzes.
# When we play those buzzes fast enough, a melody will be heard.
def play(tune):

    pin = init()
    x = 0

    if (tune == 1):
        pitches = [ 262, 294, 330, 349, 392, 440, 494, 523, 587, 659, 698, 784, 880, 988, 1047 ]
        duration = 0.1

        for p in pitches:
            buzz(pin, p, duration)
            time.sleep(duration * 0.5)

        for p in reversed(pitches):
            buzz(pin, p, duration)
            time.sleep(duration * 0.5)

    elif (tune == 2):
        pitches = [ 262, 330, 392, 523, 1047 ]
        duration = [ 0.2, 0.2, 0.2, 0.2, 0.2, 0,5 ]

        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] * 0.5)
            x += 1

    elif (tune == 3):
        pitches = [ 392, 294, 0, 392, 294, 0, 392, 0, 392, 392, 392, 0, 1047, 262 ]
        duration = [ 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.4 ]

        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] * 0.5)
            x += 1

    elif (tune == 4):
        pitches = [ 1047, 988, 659 ]
        duration = [ 0.1, 0.1, 0.2 ]

        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] * 0.5)
            x += 1

    elif (tune == 5):
        pitches = [ 1047, 988, 523 ]
        duration = [ 0.1, 0.1, 0.2 ]

        for p in pitches:
            buzz(pin, p, duration[x])
            time.sleep(duration[x] * 0.5)
            x += 1
