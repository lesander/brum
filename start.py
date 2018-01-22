import config
import RPi.GPIO as GPIO
import time
print 'Starting BRUM now. :)'
GPIO.setmode(GPIO.BCM)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
  print GPIO.input(32)
  time.sleep(1)
