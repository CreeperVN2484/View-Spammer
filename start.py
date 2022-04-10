#imports
import pyautogui
import webbrowser
import time
from numpy.random import randint
from threading import Thread
import os

#configs
url = "https://www.youtube.com/watch?v=VaZ_jEX3Tok&ab_channel=GrayStillPlays" #url of the video
totaltabeachloopmin = 1 #default is 10
totaltabeachloopmax = 2 #default is 30 #WARNING! If 2 values are the same, python get an error
sleeptimeeachtabopens = randint(1, 3)


#random views each time to prevent human verification
spamseachloops = randint(totaltabeachloopmin, totaltabeachloopmax)
#random waiting time to prevent human verification
waitingtime = randint(4, 7)
sleeptimeeachloop = spamseachloops * sleeptimeeachtabopens + 0 #if below this is below 35, view wont count #config

#main code

def clear():
    os.system('cls')

def timer():
    nexttime = 0
    while True:
     time.sleep(0.1)
     global times
     times = nexttime + 0.1
     nexttime = times
    



def maincode():
  window = 0
  views = 0
  while True:
    window = window + 1
    webbrowser.open('google.com') #prevent video from not loading
    time.sleep(sleeptimeeachtabopens)
    webbrowser.open('google.com')
    time.sleep(sleeptimeeachtabopens)


    #loop
    for x in range(spamseachloops):
        time.sleep(sleeptimeeachtabopens)
        webbrowser.open(url)


    #close all tabs to prevent computer to crash
    time.sleep(sleeptimeeachloop)
    pyautogui.moveTo(1260, -130)
    pyautogui.click(button='left')

    newviews = views + spamseachloops
    views = newviews

    clear()
    timetaken = round(times, 2)
    print("Total views: " + str(views))
    print("Elapsed: " + str(timetaken))
    print("Tabs opened: " + str(views))
    print("browser window opened: " + str(window))
    time.sleep(waitingtime)


t1 = Thread(target = timer)
t2 = Thread(target = maincode)

t1.start()
t2.start()