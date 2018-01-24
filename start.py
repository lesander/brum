#!/usr/bin/env python
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum

import config, sound
import RPi.GPIO as GPIO
import time, sys
from move import move

print '--- BRUM STARTING ---'

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
        move([0, 1, 0], 'forward')
        #move([1, 1, 1], 'forward')
        move([0, 0, 0], 'forward')

        #move.forwardIf([0, 0, 0])

        # 2. Adjust to the right if we've strayed off to the left.
        #move.adjustToRightIf([0, 0, 1])

        # 3. Adjust to the left if we've strayed off to the right.
        #move.adjustToLeftIf([1, 0, 0])

        # x. Make a decision: move forward on the crossing?
        #move.forwardIf([1, 1, 1])

        # Wait until next round.
        time.sleep(config.sleep())

except KeyboardInterrupt:
  GPIO.cleanup()
