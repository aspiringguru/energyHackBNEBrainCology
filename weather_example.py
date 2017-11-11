#api appears to be broken
#

from weather import Weather
weather = Weather()

# Lookup WOEID via http://weather.yahoo.com.

print ("started. Hellow world.")

lookup = weather.lookup(560743)
condition = lookup.condition()
print(condition['text'])

# Lookup via location name.

location = weather.lookup_by_location('dublin')
condition = location.condition()
print(condition['text'])

# Get weather forecasts for the upcoming days.

forecasts = location.forecast()
for forecast in forecasts:
    print(forecasts.text())
    print(forecasts.date())
    print(forecasts.high())
    print(forecasts.low())
