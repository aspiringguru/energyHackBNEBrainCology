import json
import numpy as np


with open('D704206052134last24Hrs.json', 'r') as f:
     data = json.load(f)

print type(data), len(data), data[0], type(data[0]), data[0]['eReal']

eReal = []

for d in data:
    eReal.append(d['eReal'])

#print eReal

eReal = np.array(eReal)

#print eReal.shape
#print eReal[:,0]
print np.sum(eReal[:,0])/1000., np.sum(eReal[:,1])/1000., np.sum(eReal[:,2])/1000.

print np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.

print int(round((np.sum(eReal[:,0])/1000.+ np.sum(eReal[:,1])/1000.+ np.sum(eReal[:,2])/1000.)/3600.))
