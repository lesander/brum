import config
import RPi.GPIO as GPIO
from time import sleep

def _sequence():
    seq = []
    seq = range(0, 8)
    """
    seq[0] = [1,0,0,0]
    seq[1] = [1,1,0,0]
    seq[2] = [0,1,0,0]
    seq[3] = [0,1,1,0]
    seq[4] = [0,0,1,0]
    seq[5] = [0,0,1,1]
    seq[6] = [0,0,0,1]
    seq[7] = [1,0,0,1]
    """
    seq[0] = [1,0,0,0]
    seq[1] = [1,1,0,0]
    seq[2] = [0,1,0,0]
    seq[3] = [0,1,1,0]
    seq[4] = [0,0,1,0]
    seq[5] = [0,0,1,1]
    seq[6] = [0,0,0,1]
    seq[7] = [1,0,0,1]
    return seq

def forwardIf(requiredSensors):

    motors = [ config.motors[0]['pins'],
               config.motors[1]['pins'] ]
    sequence = _sequence()
    step = 0

    while True:

        # Get the live sensor values
        liveSensors = [
            GPIO.input(config.sensors[0]['pin']) ^ 1,
            GPIO.input(config.sensors[1]['pin']) ^ 1,
            GPIO.input(config.sensors[2]['pin']) ^ 1
        ]

        print liveSensors

        # If the arrays do not match, we stop.
        if (liveSensors != requiredSensors):
            print '[D] !liveSensors'
            break

        # Start a loop for every pin of a single motor.
        for pin in range(0, 4):

            # TODO rewrite to more elegant solution
            print 'step ' + str(step)
            # Motor 0
            motorPin = motors[0][pin]
            print 'motorPin ' + str(motorPin)
            if (sequence[step][pin] != 0):
                GPIO.output(motorPin, -1)
            else:
                GPIO.output(motorPin, False)

            # Motor 1
            motorPin = motors[1][pin]
            print 'motorPin ' + str(motorPin)
            if (sequence[step][pin] != 0):
                GPIO.output(motorPin, -1)
            else:
                GPIO.output(motorPin, False)

        # After four pins of each motor have been set,
        # we go to the next instruction set.
        step = step + 1
        if (step > 7): step = 0
        sleep(.0007)
