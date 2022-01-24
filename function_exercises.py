# 1. is_two

def is_two(x):
    '''verify if something is 2'''

    if x == 2 or x == '2':
        return True
    else:
        return False

#or alternatively, after a bit of research another method
    
def is_two(x):
    return x in ['2', 2]

is_two('4')


# 2.

def is_vowel(string):
    '''Determines if a string a vowel'''

    return string.lower() in ['a','e','i','o', 'u']

#  is_vowel('a')


# 3. 

def is_consonant(string):
    '''Determines if a string a consonant'''

    #I can use my last function to save some time
    return not is_vowel(string) 

#  is_consonant('g')


# 4. 

def cap_cons(string):
    '''Capitolizes the first letter in a string IF it is a consonant'''

    #same as last, I used is_consonant to verify
    if is_consonant(string[0]) == True:
        string = string.capitalize()   
    return string

cap_cons('toaster')


# 5.

def calculate_tip(tip, bill):
    '''Finds the total of a bill including the percentage you wish to tip'''

    total = (tip * bill) + bill
    return total

calculate_tip(.20, 10)


# 6.

def apply_discount(og_price, discount):
    '''Apply a discount to find total cost'''

    #Similar to the last problem, but skipping a step 
    # by just casting the equation with the return 
    return og_price - (og_price * (discount / 100))

apply_discount(10, 20)


# 7.

def handle_commas(string):
    '''Removes all commas from a string'''

    #So I know how to add stuff together, and add items to a list
    # so I am going to use both of these concepts on a new list
    no_commas = ('')
    for digit in string:
        if digit not in ',':
            no_commas += digit
    return int(no_commas)

handle_commas('8,,,6,7,,5,,3,,0,,,,,9')


# 8.

def get_letter_grade(number):
    '''What letter does your grade translate to?'''

    #I actually pulled this code from our last
    # exercise and just adjusted it for the function
    if number >= 99:
        return('A+')
    elif number >= 88:
        return('A')
    elif number >= 80:
        return('B')
    elif number >= 67:
        return('C')
    elif number >= 60:
        return('D')
    else:
        return('F')

get_letter_grade(98)


# 9.

def remove_vowels(string):
    '''This will remove all vowels from a string'''

    # Same concept as exercise #7, different application
    new_string = ('')
    for letter in string:

        # I couldve also applied the is_vowel() 
        # function made for question #2
        if letter.lower() not in 'aeiou':
            new_string += letter
    return new_string

remove_vowels('discombobulated')


# 10.

# Ok, wow. A lot to unpack here. One step at a time

# First I'll make sure its a valid python identifier

def is_vaid_id(string):
    while string[0].isalpha() == False:
        string = string[1:]
    while string[-1].isalnum() == False:
        string = string[:-1]
    return string

# Then remove unwanted string

def take_out_garbage(string):
    fixed_string = ('')
    for char in string:
        if char.isalnum() == True:
            fixed_string += char
        elif char in ' _':
            fixed_string += '_'
    return fixed_string

#Then put it together in the function requested

def normalize_name(string):
    string = is_vaid_id(string)
    string = take_out_garbage(string)
    return string.lower()

normalize_name('Name')
normalize_name('First Name')
normalize_name('% Completed')

# 11.

def cumulative_sum(the_list):
    the_list = int
    list_of_sums = []
    sum = 0
    for number in the_list:
        sum += number
        list_of_sums.append(sum)
    return list_of_sums

the_list = [8, 6, 7, 5, 3, 0, 9]
cumulative_sum(the_list)

# alternative shown in class review

def cumulative_sum(the_list):
    output = []
    for i, num in enumerate(the_list):
        sum_so_far = sum(the_list[:i + 1])

        output.append(sum_so_far)
    return output


# B-B-Bonus!!!

# change data to intergers
#account for the AM or PM in military time

def twelveto_int(the_time):
    if 'am' in the_time:
        starting_time = 0
    else:
        starting_time = 12

        
    the_time = the_time[0:-2]
    the_time = int(the_time)



twelveto_int('10:45pm')