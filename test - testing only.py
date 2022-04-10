#imports
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
waitingtime = randint(2, 8)
sleeptimeeachloop = spamseachloops * sleeptimeeachtabopens + 0 #if below this is below 35, view wont count #config

#main code

def clear():
    os.system('cls')

def timer():
    nexttime = 0
    while True:
      time.sleep(0.1)
      global timetaken
      timetaken = nexttime + 0.1
      nexttime = timetaken
    



def maincode():
  tabs = 0
  views = 0
  tabs = tabs + 1

  while True:
    newviews = views + spamseachloops
    views = newviews

    clear()
    print("Total views: " + str(views))
    print("Tabs opened: " + str(views))
    print("browser window opened: " + str(tabs))

t1 = Thread(target = timer)
t2 = Thread(target = maincode)

t1.start()
t2.start()