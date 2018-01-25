#!/usr/bin/env python
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum
# move.py

import config, sensors
import RPi.GPIO as GPIO
from time import sleep
import sound
import sys

previousLiveSensors = False
hasHadCrossingBefore = False

def _sequence():
    seq = []
    seq = range(0, 8)
    seq[0] = [1,0,0,0]
    seq[1] = [1,1,0,0]
    seq[2] = [0,1,0,0]
    seq[3] = [0,1,1,0]
    seq[4] = [0,0,1,0]
    seq[5] = [0,0,1,1]
    seq[6] = [0,0,0,1]
    seq[7] = [1,0,0,1]
    return seq

def motorSequence(motors, sequence, step, movement):

    sequenceReverse = list(reversed(sequence))

    if (movement == 'left'):
        #motor0Sequence = sequence
        #motor1Sequence = sequenceReverse
        motor0Sequence = sequenceReverse
        motor1Sequence = sequenceReverse
    elif (movement == 'right'):
        motor0Sequence = sequence
        motor1Sequence = sequence
    elif (movement == 'forward'):
        motor0Sequence = sequence
        motor1Sequence = sequenceReverse
    else:
        print '[!] Unknown movement ' + str(movement) + '.'
        return

    # Start a loop for every pin of a single motor.
    for pin in range(0, 4):

        # TODO rewrite to more elegant solution
        #print 'step ' + str(step)

        # Motor 0
        motorPin = motors[0][pin]
        #print 'motorPin ' + str(motorPin)
        if (motor0Sequence[step][pin] != 0):
            GPIO.output(motorPin, 1)
        else:
            GPIO.output(motorPin, False)

        # Motor 1
        motorPin = motors[1][pin]
        #print 'motorPin ' + str(motorPin)
        if (motor1Sequence[step][pin] != 0):
            GPIO.output(motorPin, 1)
        else:
            GPIO.output(motorPin, False)

def _forward(motors, sequence, step):
    """
    motorSequence(motors, sequence, step, 'forward')
    """

def _left(motors, sequence, step):
    """
    sequenceReverse = _sequenceReverse(sequence)

    # Start a loop for every pin of a single motor.
    for pin in range(0, 4):

        # TODO rewrite to more elegant solution
        #print 'step ' + str(step)

        # Motor 0
        motorPin = motors[0][pin]
        #print 'motorPin ' + str(motorPin)
        if (sequence[step][pin] != 0):
            GPIO.output(motorPin, 1)
        else:
            GPIO.output(motorPin, False)

        # Motor 1
        motorPin = motors[1][pin]
        #print 'motorPin ' + str(motorPin)
        if (sequence[step][pin] != 0):
            GPIO.output(motorPin, 1)
        else:
            GPIO.output(motorPin, False)
    """
def move(requiredSensors, action, previousRequiredSensors = False, direction = False):

    degrees = False
    degreeTable = {
        'left': 512*3,
        'right': 512*11,
        'forward': 0
    }

    global previousLiveSensors
    global hasHadCrossingBefore

    motors = [ config.motors[0]['pins'],
               config.motors[1]['pins'] ]
    sequence = _sequence()
    step = 0

    while True:

        # Get the live sensor values
        liveSensors = sensors.get()

        # If the arrays do not match, we stop.
        if (liveSensors != requiredSensors):
            #print '[D] !liveSensors'
            if (degrees == False):
                break

        if (previousLiveSensors == False):
            previousLiveSensors = liveSensors
            print liveSensors
            #if (requiredSensors == [1, 1, 1] and hasHadCrossingBefore == True):
            #    print 'Finish?'
            #    break

        if (liveSensors != previousLiveSensors):
            print liveSensors

            if (hasHadCrossingBefore == False and liveSensors == [1, 1, 1]):
                hasHadCrossingBefore = True

                print 'direction? '
                #direction = raw_input()
                #direction = 'left'
                print 'degrees = ' + str(degreeTable[direction])
                degrees = degreeTable[direction]

                # first let's move a little forward.
                print 'moving forward a little first..'
                y = 0
                for x in range(0, 8*100):

                    motorSequence(motors, sequence, y, 'forward')
                    y = y + 1
                    if (y > 7):
                        y = 0
                    sleep(config.stepTiming)

                print 'moved forward a little.'

            elif (hasHadCrossingBefore == True and liveSensors == [1,1,1]):
                print 'FINISH'
                sound.play(5)
                sys.exit(0)
                break

        # Determine the action to complete based on
        # the parameter given.


        if (action == 'forward'):
            motorSequence(motors, sequence, step, 'forward')
        elif (action == 'left'):
            motorSequence(motors, sequence, step, 'left')
        elif (action == 'right'):
            motorSequence(motors, sequence, step, 'right')
        #elif (action == 'stop' and previousLiveSensors == previousRequiredSensors):
        #    print 'Finish?'
        #    break
        #elif (action == 'stop' and hasHadCrossingBefore and requiredSensors == [1,1,1]):
        #    print 'Finish??'
        #    break
        else:
            print '[!] Unknown action ' + str(action) +'.'
            break

        # After four pins of each motor have been set,
        # we go to the next instruction set.
        step = step + 1
        if (step > 7): step = 0

        # If we're moving based on degrees,
        # we've just completed one degree.

        if (degrees != False):
            degrees = degrees - 1
            #print 'degrees left ' + str(degrees)

            if (degrees < 0):
                print 'completed degrees'
                break

        previousLiveSensors = liveSensors

        sleep(config.stepTiming)