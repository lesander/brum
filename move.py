import config, sensors
import RPi.GPIO as GPIO
from time import sleep

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

def _sequenceReverse(seq):
    return list(reversed(seq))

def _forward(motors, sequence, step):

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
        if (sequenceReverse[step][pin] != 0):
            GPIO.output(motorPin, 1)
        else:
            GPIO.output(motorPin, False)

def move(requiredSensors, action):

    motors = [ config.motors[0]['pins'],
               config.motors[1]['pins'] ]
    sequence = _sequence()
    step = 0

    while True:

        # Get the live sensor values
        liveSensors = sensors.get()

        #print liveSensors

        # If the arrays do not match, we stop.
        if (liveSensors != requiredSensors):
            #print '[D] !liveSensors'
            break

        # Determine the action to complete based on
        # the parameter given.
        _forward(motors, sequence, step)

        # After four pins of each motor have been set,
        # we go to the next instruction set.
        step = step + 1
        if (step > 7): step = 0
        sleep(config.stepTiming)
