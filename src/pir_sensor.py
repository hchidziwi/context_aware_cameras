# pir_sensor.py
import RPi.GPIO as GPIO

def setup_pir_sensor(pin):
    """
    Sets up the PIR sensor on the specified pin.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def detect_motion(pin):
    """
    Detects motion using the PIR sensor.
    """
    return GPIO.input(pin)