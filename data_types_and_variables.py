# numbers as variables
little_mermaid_rental = 3
brother_bear_rental = 5
hercules_rental = 1

cost_per_day = 3

total_rental = little_mermaid_rental + brother_bear_rental + hercules_rental

total_spent = total_rental * cost_per_day

print(total_spent)

# weekly pay for tech work
hourly_rate_google = 400
hourly_rate_amazon = 380
hourly_rate_facebook = 350

hours_google = 6
hours_amazon = 4
hours_facebook = 10

total_pay_google = hourly_rate_google * hours_google
total_pay_amazon = hourly_rate_amazon * hours_amazon
total_pay_facebook = hourly_rate_facebook * hours_facebook

total_pay = total_pay_google + total_pay_amazon + total_pay_facebook

print(total_pay)

#7420

# Able to Enroll?
class_is_full = True
schedule_conflict = False

student_may_enroll = (not class_is_full) and (not schedule_conflict)

print(student_may_enroll)

#
offer_has_expired = True
premium_member = False
number_of_items_bought = 3
items_needed_for_offer = 2

offer_can_be_applied = (not offer_has_expired) and (premium_member or (number_of_items_bought > items_needed_for_offer))

print(offer_can_be_applied)

#B-B-Bonus!
username = 'codeup'
password = 'notastrongpassword'

five_or_more_char = len(password) >= 5
five_or_more_char

twenty_or_less_char = len(username) <= 20
twenty_or_less_char

not_the_same = password != username
not_the_same
