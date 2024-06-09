import datetime
import calendar

balance=5000
interest_rate=13*0.01
monthly_payment=500

today=datetime.datetime.today()

#Prints monday as 1,tuesday as 2 ... and month number of days
days_in_current_month=calendar.monthrange(today.year,today.month)
days_in_current_month1=calendar.monthrange(today.year,today.month)[1]
print(days_in_current_month)
print('this month total number of days: ',days_in_current_month1)

days_till_end_month=days_in_current_month1-today.day
print('total number of days until this end of month: ',days_till_end_month)

start_date=today+datetime.timedelta(days=days_in_current_month1+1)
print('today day increment by one of next month: ',start_date)

end_date=start_date

while balance>0:
	interest_charge=(interest_rate/12)*balance#to get total interest of the month
	balance+=interest_charge
	balance-=monthly_payment

	balance=round(balance,2)#two decimal places

	if balance<0:
		balance=0
	#you can write above code as balance= 0 if balance<0 else round(balance,2)

	print(end_date,balance)

	days_in_current_month1=calendar.monthrange(end_date.year,end_date.month)[1]
	end_date=end_date+datetime.timedelta(days=days_in_current_month1)

#Case study a person has a weight of 220 and he wants to loose to 180 he make a 
#goal of loosing a weight of 1.5 per week
current_weight=220
goal_weight=180
avg_lbs_week=1.5

start_date=datetime.date.today()
end_date=start_date

while current_weight>goal_weight:
	end_date+=datetime.timedelta(days=7)
	current_weight-=avg_lbs_week
print(start_date,end_date)
print(f"Reached goal in {(end_date-start_date).days // 7} weeks.")#lowround division

import math

#Case study a person wants a subscriber of goal 100000 but current subscribers is 85000
goal_subs=100000
current_subs=85000
subs_to_go=goal_subs-current_subs

avg_subs_day=200

days_to_go=math.ceil(subs_to_go/avg_subs_day)#round to next value

today=datetime.date.today()

print(f'the takes to reach the goal subscriber {today+datetime.timedelta(days=days_to_go)}')

