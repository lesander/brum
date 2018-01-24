import config
import RPi.GPIO as GPIO

def get():
    liveSensors = [
        GPIO.input(config.sensors[0]['pin']) ^ 1,
        GPIO.input(config.sensors[1]['pin']) ^ 1,
        GPIO.input(config.sensors[2]['pin']) ^ 1
    ]
    return liveSensors
