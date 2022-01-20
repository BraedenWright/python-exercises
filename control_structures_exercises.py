
# 1.Conditional Basics
# a.

from timeit import repeat


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
#  a.01

i = 5

while i <= 15:
    print(i)
    i = i + 1


#   a.02

i = 0 

while i <= 100:
    print(i)
    i = i + 2


#   a.03

i = 100

while i >= -10:
    print(i)
    i = i - 5


#  a.04

i = 2

while i < 1000000:
    print(i)
    i = i * i


#   a.05

i = 100

while i >= 5:
    print(i)
    i = i - 5


# b.
#  b.01

your_number = input('Pick a number, any number: ')

your_number = int(your_number)

for i in range(1, 11):
    print(f'{your_number} * {i} = {your_number * i}')


#   b.02

for i in range(1, 10):
    print(str(i) * i)


#  c.

odd_number = input('Pick any old odd number between 1 - 50: ')


while True:
    if (odd_number.isdigit() == False
        or int(odd_number) > 50
        or int(odd_number) <= 0
        or int(odd_number) % 2 == 0):
            print('Almost, but not an Odd Number')
            odd_number = input('Pick any old odd number between 1 - 50: ')
    else:
        break

odd_number = int(odd_number)
print(' The number to skip is ', odd_number)

for i in range(1, 50):
    if i % 2 == 0:
        continue
    elif i == odd_number:
        print('Avoiding number', i, 'like the plague')
    else:
        print('Here is an odd number', i)


#  d.

positive_number = input('Pick any positive integer: ')

while True:
    if (positive_number.isdigit() ==  False
       or int(positive_number) < 0):
        print('')
        positive_number = input('Pick any positive integer: ')
    else:
        break

for i in range(0, int(positive_number) + 1):
    print(i)


#  e.

positive_number = input('Pick any positive integer: ')

while True:
    if (positive_number.isdigit() ==  False
       or int(positive_number) < 0):
        print('')
        positive_number = input('Pick any positive integer: ')
    else:
        break

for i in reversed(range(1, int(positive_number) + 1)):
    print(i)


#  3. FizzBuzz Test

#  Write a program that prints the numbers from 1 to 100

#  For multiples of three print "Fizz" instead of the number

#  For the multiples of five print "Buzz"

#  For numbers which are multiples of both three and 
#  five print "FizzBuzz"




for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    

# 4. Table of Powers

#Prompt the user to enter an integer

#Display a table of squares and cubes from 1 to the value entered

#Ask if the user wants to continue

#Assume that the user will enter valid data

#Only continue if the user agrees to

your_number = input('Pick a number, any number!! ')

your_number = int(your_number)

print('Oh Snap! Your Table!')
print('--------------------')
print('number|squared|cubed')
print('------|-------|-----')

for i in range(1, your_number):
    print(f'  {i} |    {i ** 2}    |   {i ** 3}')

# 4.B-B-BONUS

your_number = input('Pick a number, any number!! ')

your_number = int(your_number)

print('Oh Snap! Your Table!')
print('--------------------')
print('number|squared|cubed')
print('------|-------|-----')

for i in range(1, your_number):
    print('{:^6}|{:^7}|{:^5}'.format(i, i ** 2, i ** 3))



# 5. Convert number grades to letter grades

#Prompt the user for a numerical grade from 0 to 100

#Display the corresponding letter grade

#Assume that the user will enter valid integers for the grades

#Grade Ranges:
    # A+ : 100 - 99
    # A  : 98 - 88
    # B  : 87 - 80
    # C  : 79 - 67
    # D  : 66 - 60
    # F  : 59 - 0

     

while True:
    your_grade = input('What was your score?')
    your_grade = int(your_grade)
    if your_grade >= 99:
        print('A+')
    elif your_grade >= 88:
        print('A')
    elif your_grade >= 80:
        print('B')
    elif your_grade >= 67:
        print('C')
    elif your_grade >= 60:
        print('D')
    else:
        print('F')
        
    choice = input('Anything Else? Enter y to continue:')
    if choice.lower() in ['Y', 'y']:
        continue
    else:
        break


# 6.

bookshelf = [
    {
        'title':'title1',
        'author': 'author1',
        'genre': 'Sci-Fi'
    },
    {
        'title':'title2',
        'author': 'author1',
        'genre': 'Horror'
    },
    {
        'title':'title3',
        'author': 'author2',
        'genre': 'Horror'
    },
    {
        'title':'title4',
        'author': 'author3',
        'genre': 'Fantasy'
    }
]

for book in bookshelf:
    print('What are you looking at?')
    [print(key, ': ', book[key]) for key in book]
    print('------')


what_genre = input('What genre are you feeling?')

matches = []
for book in bookshelf:
    if book ['genre'].lower() == what_genre.lower():
        matches.append(book['title'])
if matches == []:
    print('nothing to see here')
else:
    print(f'Here\'s what we got for {what_genre}')
    [print(match) for match in matches]