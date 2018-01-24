#!/usr/bin/env python
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum

import config, sound
import RPi.GPIO as GPIO
import time, sys
from move import move

print '--- BRUM STARTING!!! ---'

"""""""""""""""""""""
  Initialize GPIO
"""""""""""""""""""""

# Clean gpio states before we continue.
print '[*] Cleaning GPIO states and setting mode..'
GPIO.setwarnings(config.warnings())
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

print '[*] Speed is set to ' + str(config.stepTiming)

# Register buttons.
Buttons = { 'panic': 26 }
GPIO.setup(Buttons['panic'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Register motor pins.
print '[*] Registering stepper pins..'
for i in config.motors:
    motor = i
    for pin in motor['pins']:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)

# Register sensors.
for i in config.sensors:
    sensor = i
    GPIO.setup(sensor['pin'], GPIO.IN)

# Register leds
# TODO

# Register audio
GPIO.setup(config.piezo['pin'], GPIO.OUT)

"""""""""""""""""""""""""""""""""
  Let's get this party started!
"""""""""""""""""""""""""""""""""

print '[*] Ready for some action!'

try:
    while True:

        # 0. Stop everything if the panic button is pressed.
        # BUG: this only runs at the beginning of every round!
        bumperStatus = GPIO.input(Buttons['panic'])
        if (bumperStatus==0):
            print '[!] Panic button pressed, stopping..'
            sound.play(5)
            sys.exit(0)

        # 1. Move forward on the condition that we see a black line in center.

        # Move forward if we're on the line.
        move([0, 1, 0], 'forward')

        # Move forward if we can't see anything.
        move([0, 0, 0], 'forward')

        # Adjust to the left or right.
        move([1, 0, 0], 'left')
        move([0, 0, 1], 'right')

        # Take a left or right turn.
        move([1, 1, 0], 'left')
        move([0, 1, 1], 'right')

        # Edge cases.
        move([1, 0, 1], 'forward')

        # The final crossing decision:
        #move([1, 1, 1], 'forward') # <- decision
        move([1, 1, 1], 'right', False, True) # <- decision

        # Wait until next round.
        time.sleep(config.sleep())

except KeyboardInterrupt:
  GPIO.cleanup()
