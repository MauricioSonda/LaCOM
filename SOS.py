import RPi.GPIO as GPIO
import time

PIN = 4 

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.OUT)

def punto():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(0.333)  
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.333)  

def raya():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(0.5)   
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.5)   


def sos():
    for _ in range(3):      
        for _ in range(3):
            punto()
        time.sleep(0.5)    

        
        for _ in range(3):
            raya()
        time.sleep(0.5)     

       
        for _ in range(3):
            punto()
        time.sleep(1)       

if __name__ == "__main__":
    setup()
    try:
        sos()              
    except KeyboardInterrupt:
        print("Proceso Finalizado")
        GPIO.cleanup()
