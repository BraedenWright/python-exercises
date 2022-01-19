# Movie Rentals

little_mermaid = 3
brother_bear = 5
hercules = 1

cost_per_day = 3

cost_of_rentals = (little_mermaid + brother_bear + hercules) * cost_per_day


# Weekly Pay for Tech
hourly_rate_google = 400
hourly_rate_facebook = 350
hourly_rate_amazon = 380

hours_worked_google = 8
hours_worked_facebook = 3
hours_worked_amazon = 6

total_pay_google = hourly_rate_google * hours_worked_google
total_pay_facebook = hourly_rate_facebook * hours_worked_facebook
total_pay_amazon = hourly_rate_amazon * hours_worked_amazon

total_pay = total_pay_amazon + total_pay_facebook + total_pay_google

total_pay

# Available for Class
class_is_full = True
schedule_conflict = False

student_can_enroll = (not class_is_full) and (not schedule_conflict)

student_can_enroll

#
offer_expired = True
premium_member = False
number_of_items_bought = 3
items_needed_for_offer = 2

can_be_applied = (not offer_expired) and (premium_member or (number_of_items_bought > items_needed_for_offer))

can_be_applied