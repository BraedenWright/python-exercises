
# 1.Conditional Basics
# a.

day = input('What day of the week is it?')

if day.lower() in ['monday', 'mon']:
    print('Today is Monday')
else:
    print(f'It is {day.capitalize()}')


# b.
day = input('Please enter the day of the week: ')

while day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
    print('Nuh-uh-uh. Please enter the full name of the day')
    day = input('Please enter the day of the week: ')


if day.lower() in ['sunday', 'saturday']:
    print('It\'s currently the weekend')
else:
    print('It\'s a weekday')


# c.

weekly_hours = 60
hourly_rate = 17
overtime_rate = hourly_rate * 2

if weekly_hours <= 40:
    total_paycheck = weekly_hours * hourly_rate

else:
    standard_week = 40 * hourly_rate
    overtime_pay = (weekly_hours - 40) * overtime_rate
    total_paycheck = standard_week + overtime_pay

print(total_paycheck)


# 2. 
#  a.

i = 5

while i <= 15:
    print(i)
    i = i + 1