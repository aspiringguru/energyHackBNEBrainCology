
import datetime
import n2w
nowTime = datetime.datetime.now()
print (nowTime)
print (nowTime.hour)
print (nowTime.minute)
print (nowTime.day)
print (nowTime.month)
print (nowTime.strftime("%B"))
print (nowTime.year)

print (nowTime.strftime('%A %d %B %Y'))
print (nowTime.strftime('%A %d %B'))

print(n2w.convert(2017))

ampm = " A M "
hour = int(nowTime.hour)
if hour>12:
    hour -= 12
    ampm = " P M "

timeInWords = str(hour)+" " + str(nowTime.minute)+ ampm
print (timeInWords)
dateInwords = nowTime.strftime('%A %d %B') + " " + n2w.convert(2017)
print (dateInwords)
