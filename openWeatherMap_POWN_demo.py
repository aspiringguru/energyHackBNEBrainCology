'''

https://stackoverflow.com/questions/1474489/python-weather-api
http://openweathermap.org/appid

'''

import pyowm
owm = pyowm.OWM('698d67c5bed3089c18e103c453c2a698')  # You MUST provide a valid API key
#observation = owm.weather_at_place('London,uk')
observation = owm.weather_at_place('Brisbane,au')
w = observation.get_weather()
print (type(w), w)
wind =  w.get_wind()
print (type(wind), wind, wind['speed'], wind['deg'])
humidity =  w.get_humidity()
print (type(humidity), humidity)
temp = w.get_temperature('celsius')
print (type(temp), temp, temp['temp'])


weatherReport = "the wind is "+str(wind['speed'])+" km/hr from " + str(wind['deg'])+" degrees."
weatherReport += " The temperature is "+str(temp['temp'])
weatherReport += " The humidity is "+str(humidity)

print (weatherReport)
