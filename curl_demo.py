import subprocess
import json

import time
import calendar

print time.gmtime()
currEpoch = calendar.timegm(time.gmtime())
yesterdayEpoch = calendar.timegm(time.gmtime()) - 24*60*60
lastWeekEpoch = calendar.timegm(time.gmtime()) - 24*60*60*7
print "current epoch time:", currEpoch
print "yesterdayEpoch:", yesterdayEpoch
print "lastWeekEpoch:", lastWeekEpoch

curl = ['curl', '-X', 'GET', '-H', "Authorization: Bearer key_328566e680a6f194c68a1f01d337be2b", "https://api.wattwatchers.com.au/v2/devices"]

with open('output.json', 'w') as file:
    status = subprocess.call(curl, stdout=file)


with open('output.json', 'r') as f:
     data = json.load(f)
print (type(data), len(data), data[0])


for i in range(len(data)):
    print (i, data[i])
    url = "https://api.wattwatchers.com.au/v2/long-energy/"+data[i]+"?fromTs="+str(yesterdayEpoch)+"?toTs="+str(currEpoch)+"?granularity=5m"
    print url
    curl = ['curl', '-X', 'GET', '-H', "Authorization: Bearer key_328566e680a6f194c68a1f01d337be2b", url]
    fileName = str(data[i])+"last24Hrs.json"
    print ("fileName:", fileName)
    with open(fileName, 'w') as file:
        status = subprocess.call(curl, stdout=file)
    break




'''
curl = ['curl', '-X', 'GET', '-H', "Authorization: Bearer key_328566e680a6f194c68a1f01d337be2b", "https://api.wattwatchers.com.au/v2/long-energy/D800000000000?fromTs=1451779200"]
with open('output2.json', 'w') as file:
    status = subprocess.call(curl, stdout=file)
with open('output2.json', 'r') as f:
     data = json.load(f)
print (type(data), len(data), data)
'''
