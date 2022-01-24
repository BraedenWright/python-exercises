
# 1. a. import practice on ipython terminal

#   b.  

import function_exercises

# 2.

# How many different ways can you combine the letters 'abc' with the numbers 123

import itertools

len(list(itertools.product('abc', [1, 2, 3])))

     # 9 different combos


# How many different combinations are there of 2 letters from 'abcd'

len(list(itertools.combinations('abcd', 2)))

    # 10 different combos


# How many different permutations are there of 2 letters from 'abcd'

len(list(itertools.permutations('abcd', 2)))

    # 12 different permutations

# 3. profiles.json


import json

json.load(open('profiles.json'))

# total number of users
# number of actice users
# number of inactive users
# grand total of balances for all users
# avg balance per user
# user with lowest balance
# user with highest balance
# most common fav fruit
# least common
# total number of unread massages for all users


#ok, gotta do some set up with the data
    # make it easier to reference the dataset
    # find a way to convert the data to the proper type I need
        #float, string, int?
    # do i need to import anything else?

dataset = json.load(open('profiles.json'))

def converted_balance(balance):
    balance = balance.replace('$', '')
    balance = balance.replace(',', '')
    return float(balance)


    # apply across the dataset
for data in dataset:
    data['balance'] = converted_balance(data['balance'])

# back to the questions at hand
    # total number of users - 19

len(dataset)
        # itertools.count(dataset) - overthinking it

    # number of active users - 9

active_user = [data for data in dataset if data['isActive']]
len(active_user)
        #  len(data in dataset if data['isActive']) - did not work

    ## number of inactive users - 10

inactive_user = (len(dataset) - len(active_user))

print(inactive_user)

    ## grand total of balances for all users

grand_total = sum([data['balance'] for data in dataset])

grand_total

# grand_total  of $52,667.02

    ## avg balance per user

avg_balance = (grand_total / len(dataset))

print(round(avg_balance, 2))

# 2771.95 is the avg balance

    ## user with lowest balance

balance_list = ([data['balance'] for data in dataset])

min(balance_list)

lowest_balance = min(dataset, key=lambda data: data['balance'])

lowest_balance

#the user with the lowest balance is user 7 with $1,214.1

    # user with highest balance

max(balance_list)

highest_balance = max(dataset, key=lambda data: data['balance'])

highest_balance

#the user with the highest balance is user 4 with $3,919.64

    # most common fav fruit

from statistics import mode

fav_fruit = ([data['favoriteFruit'] for data in dataset])

mode(fav_fruit)

# strawberry is the most liked fruit

    # least common

min(fav_fruit)

# apple is the less commonly liked fruit

    # total number of unread massages for all users


