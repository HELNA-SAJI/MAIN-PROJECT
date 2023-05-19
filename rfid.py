import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pyttsx3
engine = pyttsx3.init()
from time import sleep
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522()
while True:
        

            id, text = reader.read()
            print(id)
            if id==1015621761125:
                engine.say("EC Department arrived")
                engine.runAndWait()
            if id==458254561393:
                engine.say(" CS Department arrived")
                engine.runAndWait()
