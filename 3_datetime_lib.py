from datetime import datetime
now=datetime.now()
print(now)
print( now.date)
print("%02d/%02d/%04d" % (now.day, now.month, now.year))
print("%02d:%02d:%02d" % (now.hour,now.minute, now.second))
print("%02d/%02d/%04d %02d:%02d:%02d" % (now.month, now.day, now.year, now.hour, now.minute, now.second))