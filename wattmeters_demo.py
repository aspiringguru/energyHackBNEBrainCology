import requests
import os
import json

#stmt = """curl -b "email=XXX; password=YYY\" https://storkcloud.org/api/stork/ls?uri=ftp://ftp.mozilla.org >> input.json"
stmt = """curl -X GET -H "Authorization: Bearer key_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" "https://api.wattwatchers.com.au/v2/devices"

returnValue = os.system(stmt)

print (type(returnValue))
print (returnValue)
