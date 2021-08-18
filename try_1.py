from datetime import datetime
import pyttsx3
import time

time = datetime.now()
_hour = time.hour
_minute = time.minute

engine = pyttsx3.init()

name = input("Enter your name: ")

def check():
    if(_hour <= 9 and _minute == 00):
        engine.say(f"{name}, you have reached the office on time.")

    elif(_hour >= 9):
        engine.say(f"{name}, you have reached the office late.")

    engine.runAndWait()

def eyeExercise():
    if _hour == 9 and _minute == 30:
        while _hour <= 17 and _minute <= 00:
            engine.say("Dear Programmer, it's time for eye exercise.")
            engine.runAndWait()
            time.sleep(1800)

def physicalExercise():
    if _hour == 9 and _minute == 45:
        while _hour <= 17 and _minute <= 00:
            engine.say("Dear Programmer, it's time for Physical Exercise.")
            engine.runAndWait()
            time.sleep(2700)

def drinkWater():
    if _hour == 9 and _minute == 40:
        while _hour <= 17 and _minute <= 00:
            engine.say("Dear Programmer, it's time to drink water.")
            engine.runAndWait()
            time.sleep(2400)

if __name__ == '__main__':
    check()
    eyeExercise()
    physicalExercise()
    drinkWater()