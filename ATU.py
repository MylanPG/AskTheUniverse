import time
import os
import  googletrans
from googletrans import Translator, constants
import pprint
from pprint import *
from datetime import datetime, timedelta
import random

def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')

def lang():
 while True:
  lang = input("\nWould you like to see a list of available languanges?  (Y/N): ")

  if lang.upper() == "Y":
   pprint(constants.LANGUAGES)

  if lang.upper() == "N":
   break

def lang2():
 while True:
  global q2
  q2 = input("\nWhat language do you want to send your request in? (Enter 2 characters I.E. English = en): ")
  if q2.lower() in constants.LANGUAGES:
   break 
  if q2.lower() not in constants.LANGUAGES:
   lang2 = input("\nYou have choosen an invalid language. Would you like to see a list of Languages? (Y/N): ")
   if lang2.upper() == "Y":
    pprint(constants.LANGUAGES)
   if lang2.upper() == "N":
    continue

def bins():
 while True:
  global q3
  global binout
  q3 = input("\nWhat you also like to send the request with binary? (Y/N): ")

  if q3.upper() == "Y":
   binout = (" ".join(f"{ord(i):08b}" for i in q1))
   break
  if q3.upper() == "N":
   binout = ' '
   break

def connecting():
   spaces = 0
   x = random.randint(3, 10)
   end_time = datetime.now() + timedelta(seconds=x)
   while True:
    print("\b "*spaces+"-", end="X",flush=True)
    spaces=spaces+1
    time.sleep(0.2)
    if spaces > 5:
     print("\b \b"*spaces, end="X")
     spaces = 0
     if end_time < datetime.now():
      break    

translator = Translator()

print("\n \"Positive words can bend your world in your favor.\" ― Stephen Richards\n\
  \nMany philosophers say that anything is possible, given that you make a request to the Universe.\
  \nBut what language does the Universe speak?\
  \nThis will submit your desires to the Universe in various languages.\nMaybe one of them is the language of the Universe.\n") 

time.sleep(1)

input("Press Any Key To Connect To The Universe")

clear_screen()

print(" \"People who do affirmations will have the sensation that they are causing the environment to conform to their will.\
  \nThis is an immensely enjoyable feeling because the illusion of control is one of the best illusions you can have.\"\
  \n-Scott Adams\n")

time.sleep(1)

print("Connecting\n")
connecting()

#time.sleep(2)

print("\nYou are now connected with the Universe")

name = input("\nWhat is your name?: ")

dob = input("\nWhat is your Date of Birth?: ")

question = input("\nWhat do you desire?: ")

lang()

q1 = name + ", who was born on: " + dob + " desires the following: " + question

lang2()

bins()

print("\nThe following request(s) will be sent to the Universe:","\n\n\nEnglish: ", q1, '\n\n', sep='')

if q3.upper() == "Y":
  print("Binary: ",binout, '\n\n', sep='')

translation = translator.translate(q1, dest=q2.lower())
print(q2 + ": ", translation.text + '\n', sep='')

time.sleep(2)

print("Sending Request to Universe\n")

connecting()

print("\n\nThe Universe has received your request. The time of receipt is:\n", datetime.utcnow(), sep='')

input("\nPress Any Key to Escape")