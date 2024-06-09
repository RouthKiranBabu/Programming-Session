import datetime
import pytz

#Describing the date,weekday and isoweekday for monday
d=datetime.date(2019,5,13)
print(d)
#Output
#2019-05-13

#Monday starts for count as 0 and sunday as 6
print(d.weekday())
#Output
#0

#Monday as 1 and sunday as 7
print(d.isoweekday())
#Output
#1

#Shows today date and time
d=datetime.datetime.today()
print(d)
#Output
#2024-05-24 15:52:21.986055

#Shows today date,day,month and year
d=datetime.date.today()
print(d)
print(d.day)
print(d.month)
print(d.year)
#Output
'''
2024-05-24
24
5
2024
'''

tdel=datetime.timedelta(days=7)
print("today:",d,". After 7days: ",d+tdel)
#Output
#today: 2024-05-24 . After 7days:  2024-05-31

#date=date+timedelta
#timedelta=datea+dateb
bday=datetime.date(1998,9,14)
till_date=d-bday
print(till_date)
print(till_date.days)
print(till_date.total_seconds())
#Output
'''
9384 days, 0:00:00
9384
810777600.0
'''

#Time formatting
t=datetime.time(9,50,59,1000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
#Output
'''
09:50:59.001000
9
50
59
1000
'''

#Datetime formatting
dt=datetime.datetime(2019,5,1,20,31,20,10000)
print(dt.date())
print(dt.time())
print(dt.year)
print(dt)
#Output
'''
2019-05-01
20:31:20.010000
2019
2019-05-01 20:31:20.010000
'''

delt=datetime.timedelta(days=7,hours=12)
adddt=dt+delt
print(adddt)
print()
#Output
#2019-05-09 08:31:20.010000

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()
'''
#New way
val3 = datetime.datetime.now(datetime.UTC)'''

print(dt_today)
print(dt_now)
print(dt_utcnow)
#Output
'''
  dt_utcnow=datetime.datetime.utcnow()
2024-05-24 15:58:16.899431
2024-05-24 15:58:16.899430
2024-05-24 10:28:16.899430
'''

#This shows at microseconds like 20+00:00 which is utc offset
dt=datetime.datetime(2019,5,1,20,31,20, tzinfo=pytz.UTC)
print(dt)
#Output
'''
ow(datetime.UTC).
  dt_utcnow=datetime.datetime.utcnow()
2019-05-01 20:31:20+00:00
'''

#Shows the current utc time where milisecond added like 42.484065+00:00 
#and timezone aware
dt_now=datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
#Output
'''
(datetime.UTC).
  dt_utcnow=datetime.datetime.utcnow()
2024-05-24 10:54:35.316353+00:00
'''

#Almost the same as before but better to prefer above ones
dt_utcnow=datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
#Output
'''
re version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
2024-05-24 10:55:41.815416+00:00
  dt_utcnow=datetime.datetime.utcnow()
c:\Users\kiran\One
'''

#To set timezone into our location zone like 2019-05-13 11:31:22.968456-04:00
#minus sign show the difference between mine and us/eastern
dt_mtn=dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print(dt_mtn)
#Output
'''
    ^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 182-183: truncated \UXXXXXXXX esc
'''

#Shows all the timezones location as above like 'US/Eastern'
for timezones in pytz.all_timezones:
	print(timezones)
#Output
'''
Error: (unicode error) 'unicodeescape' codec can't decode bytes in position 182-183: truncated \UXXXXX
'''

#Timezone aware
dt_nowtz=datetime.datetime.now(tz=pytz.UTC)
print(dt_nowtz)
#Output
'''
xError: (unicode error) 'unicodeescape' codec can't decode bytes in position 182-183: truncated \UXXXXXXXX 
'''

#Timezone unaware
dt_now=datetime.datetime.now()
print(dt_now)
#Output
'''

SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 182-183: truncated \UXXXX
'''

#Naive datetime whice is unavaired of utc
dt_now=datetime.datetime.now()
print(dt_now)
mnt=pytz.timezone('US/Eastern')
#Output
#w(datetime.UTC).
#  dt_utcnow=datetime.datetime.utcnow()
#2024-05-24 17:26:21.882271

#Making the unavariable naive into local pytz timezone
mnt=pytz.timezone('US/Eastern')
dt_nowtz=mnt.localize(dt_now)
print(dt_nowtz)
#Output
#now(datetime.UTC).
#  dt_utcnow=datetime.datetime.utcnow()
#2024-05-24 17:28:10.194185-04:00

#strftime converts datetime into string
dt=datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
print(dt.strftime('%B %d,%Y'))
#Output
#atetime.UTC).
#  dt_utcnow=datetime.datetime.utcnow()
#May 24,2024

#strptime converts string to datetime
str_dt='May 13,2019'
dt=datetime.datetime.strptime(str_dt,'%B %d,%Y')
print(dt)
#Output
#(datetime.UTC).
  #dt_utcnow=datetime.datetime.utcnow()
#2019-05-13 00:00:00
