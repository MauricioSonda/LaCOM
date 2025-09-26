import RPi.GPIO as GPIO
import time

LED_PIN = 4
BUTTON_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def punto():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(0.333)  
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.333) 

#main
try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH: 
            if not punto():
                continue
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
