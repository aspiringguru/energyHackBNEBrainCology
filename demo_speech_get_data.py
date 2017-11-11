

import speech_recognition as sr
import pyttsx
import pyowm
import datetime
import n2w
import json
import numpy as np
import subprocess
import json
import os

import time
import calendar


#set constants
ISROBOT = False
IDENTITY = "robot"
WATTKEY = "Authorization: Bearer key_328566e680a6f194c68a1f01d337be2b"
#
currEpoch = calendar.timegm(time.gmtime())
yesterdayEpoch = calendar.timegm(time.gmtime()) - 24*60*60
#lastWeekEpoch = calendar.timegm(time.gmtime()) - 24*60*60*7
#
curl = ['curl', '-X', 'GET', '-H', WATTKEY, "https://api.wattwatchers.com.au/v2/devices"]



#initialize
owm = pyowm.OWM('698d67c5bed3089c18e103c453c2a698')  # You MUST provide a valid API key
observation = owm.weather_at_place('Brisbane,au')
fileName = 'output.json'
try:
    os.remove(fileName)
except OSError:
    pass

with open(fileName, 'w') as file:
    status = subprocess.call(curl, stdout=file)
with open(fileName, 'r') as f:
     data = json.load(f)
print ("ID we are using:", data[0])

#engine = pyttsx.init()
# Record Audio
while True:
    r = sr.Recognizer()
    spoken = ""
    output = "nothing"
    engine = pyttsx.init()


    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print("heard something.", type(audio))

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        spoken = r.recognize_google(audio).lower()
        print("You said: " + spoken)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        output = "   "#silence message until work out how to handle standby.
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        output = "Request Error. try again."
    if "time" in spoken:
        output = "get time"
        nowTime = datetime.datetime.now()
        ampm = " A M "
        hour = int(nowTime.hour)
        if hour>12:
            hour -= 12
            ampm = " P M "
        timeInWords = str(hour)+" " + str(nowTime.minute)+ ampm
        print (timeInWords)
        output = timeInWords
    elif "date" in spoken:
        nowTime = datetime.datetime.now()
        dateInwords = nowTime.strftime('%A %d %B') + " " + n2w.convert(2017)
        print (dateInwords)
        output = dateInwords
    elif "power" in spoken:
        try:
            fileName = 'output.json'
            try:
                os.remove(fileName)
            except OSError:
                pass
            curl = ['curl', '-X', 'GET', '-H', WATTKEY, "https://api.wattwatchers.com.au/v2/devices"]
            with open(fileName, 'w') as file:
                status = subprocess.call(curl, stdout=file)
            with open(fileName, 'r') as f:
                 data = json.load(f)
            print ("ID we are using:", data[0])
            currEpoch = calendar.timegm(time.gmtime())
            yesterdayEpoch = calendar.timegm(time.gmtime()) - 24*60*60
            print ("currEpoch:", currEpoch, ", yesterdayEpoch:", yesterdayEpoch)
            output = "calculate power rate"
            print ("data[0]:", data[0])
            url = "https://api.wattwatchers.com.au/v2/long-energy/"+str(data[0])+"?fromTs="+str(yesterdayEpoch)+"?toTs="+str(currEpoch)+"?granularity=5m"
            print ("in power: url=", url)
            curl = ['curl', '-X', 'GET', '-H', "Authorization: Bearer key_328566e680a6f194c68a1f01d337be2b", url]
            fileName = "last24Hrs.json"
            try:
                os.remove(fileName)
            except OSError:
                pass
            print ("fileName:", fileName)
            with open(fileName, 'w') as file:
                status = subprocess.call(curl, stdout=file)
            #xxxxx
            with open(fileName, 'r') as f:
                 data = json.load(f)
            #print type(data), len(data), data[0], type(data[0]), data[0]['eReal']
            eReal = []
            for d in data:
                eReal.append(d['eReal'])
            eReal = np.array(eReal)
            #print np.sum(eReal[:,0])/1000., np.sum(eReal[:,1])/1000., np.sum(eReal[:,2])/1000.
            #print np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.
            #print int(round((np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.)/3600.))
            powerUsed = str(int(round((np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.)/3600.)))
            output = "you have consumed "+powerUsed+ " kilowatt hours of power in the last 24 hours."
        except:
            print ("error caught in power. try again.")
            output = "error, try again."
    elif "cost" in spoken:
        try:
            fileName = 'output.json'
            try:
                os.remove(fileName)
            except OSError:
                pass
            curl = ['curl', '-X', 'GET', '-H', WATTKEY, "https://api.wattwatchers.com.au/v2/devices"]
            with open(fileName, 'w') as file:
                status = subprocess.call(curl, stdout=file)
            with open(fileName, 'r') as f:
                 data = json.load(f)
            print ("ID we are using:", data[0])
            print ("cost recognised.")
            currEpoch = calendar.timegm(time.gmtime())
            output = "calculate power rate"
            print ("data[0]:", data[0])
            url = "https://api.wattwatchers.com.au/v2/long-energy/"+str(data[0])+"?fromTs="+str(currEpoch-20*60)+"?toTs="+str(currEpoch)+"?granularity=5m"
            print url
            curl = ['curl', '-X', 'GET', '-H', "Authorization: Bearer key_328566e680a6f194c68a1f01d337be2b", url]
            fileName = "currentPower.json"
            try:
                os.remove(fileName)
            except OSError:
                pass
            print ("cost, opening fileName:", fileName)
            with open(fileName, 'w') as file:
                status = subprocess.call(curl, stdout=file)
            #xxxxx
            with open(fileName, 'r') as f:
                 data = json.load(f)
            #print type(data), len(data), data[0], type(data[0]), data[0]['eReal']
            eReal = []
            for d in data:
                eReal.append(d['eReal'])
            eReal = np.array(eReal)
            print eReal
            print eReal.shape
            #print np.sum(eReal[:,0])/1000., np.sum(eReal[:,1])/1000., np.sum(eReal[:,2])/1000.
            #print np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.
            #print int(round((np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.)/3600.))
            #powerUsed = 0.5
            powerUsed = round( (( eReal[0,0]/1000. + eReal[0,1]/1000. + eReal[0,2] ) /1000./300.), 2)
            costUsed = powerUsed * 0.25
            #powerUsed = str(int(round((np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.)/3600.)))
            output = "you are using "+str(powerUsed) + " kilowatt of power at a cost of "+ str(costUsed) + " dollars per hour."
            print ("in cost:", output)
        except:
            print ("error caught in cost. try again.")
            output = "error, try again."
    elif "weather" in spoken:
        output = "get weather"
        print (output)
        w = observation.get_weather()
        #print (type(w), w)
        wind =  w.get_wind()
        #print (type(wind), wind, wind['speed'], wind['deg'])
        humidity =  w.get_humidity()
        #print (type(humidity), humidity)
        temperature = w.get_temperature('celsius')
        #print (type(temp), temp, temp['temp'])
        weatherReport = "the wind is "+str(wind['speed'])+" km per hour from " + str(wind['deg'])+" degrees."
        weatherReport += " The temperature is "+str(temperature['temp']) + " degrees."
        weatherReport += " The humidity is "+str(humidity) + " percent."
        output = weatherReport
        print (weatherReport)
    elif IDENTITY in spoken:
        output = "I am robot"
        print (output)
    engine.say(output)
    engine.runAndWait()

print ("end")
