import time
import calendar

print time.gmtime()
currEpoch = calendar.timegm(time.gmtime())
yesterdayEpoch = calendar.timegm(time.gmtime()) - 24*60*60
lastWeekEpoch = calendar.timegm(time.gmtime()) - 24*60*60*7
print "current epoch time:", currEpoch
print "yesterdayEpoch:", yesterdayEpoch
print "lastWeekEpoch:", lastWeekEpoch
