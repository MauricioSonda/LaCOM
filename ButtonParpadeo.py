import RPi.GPIO as GPIO
import time

LED_PIN = 4
BUTTON_PIN = 14

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

def punto():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.333)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.333)

if __name__ == "__main__":
    setup()
    try:
        while True:
            if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                punto()
            else:
                GPIO.output(LED_PIN, GPIO.LOW)   
                time.sleep(0.1)    
    except KeyboardInterrupt:
        print("Proceso Finalizado")
        GPIO.cleanup()
