"""
Assume that a Programmer works at the office from 09:00 am - 05:00 pm. We have to take care of his health & remind him
3 things,
-> To drink a total of 3.5 L of water after some time interval.
-> To do eye exercise after every 30 minutes.
-> To perform physical activity after every 45 minutes.

Instructions:-
The task is to create a program that reminds the programmer.
For Water, remind after - Every 40 min.
For Eye Exercise, remind after - Every 30 min.
For Physical Exercise, remind after - Every 45 min.
"""

from datetime import datetime
import pyttsx3

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
    if (_hour == 9 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 10 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 10 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 11 and _minute == 00):
        engine.say( "Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 11 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 12 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 12 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 13 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 13 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 14 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif(_hour == 14 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 15 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif (_hour == 15 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif(_hour == 16 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif(_hour == 16 and _minute == 30):
        engine.say("Dear Programmer, it's time for Eye Exercise.")

    elif(_hour == 17 and _minute == 00):
        engine.say("Dear Programmer, it's time for Eye Exercise.")
    engine.runAndWait()

def physicalExercise():
    if(_hour == 9 and _minute == 45):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 10 and _minute == 31):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 11 and _minute == 15):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 12 and _minute == 1):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 12 and _minute == 45):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 13 and _minute == 31):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 14 and _minute == 15):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 15 and _minute == 1):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 15 and _minute == 45):
        engine.say("Dear Programmer, it's time for Physical Exercise.")

    elif(_hour == 16 and _minute == 31):
        engine.say("Dear Programmer, it's time for Physical Exercise.")
    engine.runAndWait()

def drinkWater():
    if(_hour == 9 and _minute == 40):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 10 and _minute == 20):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 11 and _minute == 2):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 11 and _minute == 40):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 12 and _minute == 20):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 13 and _minute == 2):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 13 and _minute == 40):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 14 and _minute == 20):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 15 and _minute == 2):
        engine.say("Dear Programmer, it's time to drink water.")

    elif(_hour == 16 and _minute == 40):
        engine.say("Dear Programmer, it's time to drink water.")
    engine.runAndWait()

if __name__ == '__main__':
    check()
    eyeExercise()
    physicalExercise()
    drinkWater()
