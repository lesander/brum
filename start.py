#!/usr/bin/env python
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum
# start.py

import config, sound, time, sys, os
import RPi.GPIO as GPIO
from move import move

print '--- BRUM STARTING!!! ---'

"""""""""""""""""""""""""""""
 Initialize GPIO & Settings
"""""""""""""""""""""""""""""

# Go to the root of the brum repository.
os.chdir('/home/brum/repo')

# Reset the status file.
with open('status.txt', 'w') as file:
    file.write('in-transit')

# Clean gpio states before we continue.
print '[*] Cleaning GPIO states and setting mode..'
GPIO.setwarnings(config.warnings())
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Print the sleep configuration.
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

# Register piezo audio.
GPIO.setup(config.piezo['pin'], GPIO.OUT)

# Connect to the bluetooth speaker.


"""""""""""""""""""""""""""""""""
  Let's get this party started!
"""""""""""""""""""""""""""""""""

# The start script gets executed once the webhook has written
# the destination to disk. We can now start moving!

print '[*] Ready for some action!'

# Open the file the webhook has just written to
# and read the destination.
file = open('destination.txt', 'r')
storeName = file.readlines()[0].replace("\n", '')
destination = config.ways[storeName]

print '[*] The destination is ' + str(destination)

try:
    while True:

        # Stop everything if the panic button is pressed.
        # BUG: this only runs at the beginning of every round!
        bumperStatus = GPIO.input(Buttons['panic'])
        if (bumperStatus==0):
            print '[!] Panic button pressed, stopping..'
            sound.play(5)
            sys.exit(0)

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

        # The final crossing destination
        move([1, 1, 1], destination, destination)

        # Wait until next round.
        time.sleep(config.sleep())

# When we press CTRL+C in the console, we should clean up our GPIO states
# before exiting the script.
except KeyboardInterrupt:
  GPIO.cleanup()
