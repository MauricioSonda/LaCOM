import RPi.GPIO as GPIO
import time

PIN = 4 

def setup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.OUT)

def set_high():
    GPIO.output(PIN, GPIO.HIGH)  

def set_low():
    GPIO.output(PIN, GPIO.LOW)

def loop()

    set_high()       
    time.sleep(0.5) 
    set_low()        
    time.sleep(0.5)  
    

if __name__ == "__main__":
    setup()
    try:
        while (1):
            loop()
    except KeyboardInterrupt:
        print ("Proceso Finalizado")
        GPIO.cleanup() 

    
