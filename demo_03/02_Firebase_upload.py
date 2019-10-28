import RPi.GPIO as GPIO
import time
import pyrebase
import subprocess
from datetime import datetime
import requests
from pprint import pprint
import sys
import time


config = {
  "apiKey": "AIzaSyD4sEe-0Imu85ls7YUM4828ufJAg1eKC28",
  "authDomain": "raspbucket-9eba3.firebaseapp.com",
  "databaseURL":"https://test--20a6d.firebaseio.com",
  "proyectId":"raspbucket-9eba3",
  "storageBucket": "raspbucket-9eba3.appspot.com",
    "messagingSenderId":"429750919523"
}
#firebase
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

#button camera
chanel = 10
#led_pin
led_pin=12

flagFood = False

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(chanel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(led_pin, GPIO.OUT)

def callbackCamera(chanel):
        if GPIO.input(chanel) == GPIO.HIGH:
                #take a picture
                subprocess.call(['fswebcam -r 640x480 --no-banner /home/pi/Desktop/image.jpg', '-1'], shell=True)
                #firebase
                storage.child("/test.jpg").put("/home/pi/Desktop/image.jpg")                                               

GPIO.add_event_detect(chanel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(chanel, callbackCamera) #Setup camera event
