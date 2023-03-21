#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 10:19:06 2023

@author: ellieryan
"""

total_miles=5009
total_trips=580
percent_leisure=0.3
percent_shopping=0.2
percent_comuting=0.12
percent_other=0.28 # consider this 
percent_personal_business=0.1
total_percent=percent_leisure+percent_shopping+percent_comuting+percent_other+percent_personal_business

comuting_miles=1276*0.61 #15%
business_miles=555*0.72 #
a=1 # percent cars?
b=1 # percent cars?
shopping_miles=(626+771)/2*a
leisure_miles=2691*0.7
education_miles=340*b
total=comuting_miles+business_miles+shopping_miles+leisure_miles+education_miles
other_miles=total_miles-total

# fast charger
cost_fast=0.73 #cost per kWh
power_fast= 50

cost_medium=0.5 #guess
power_medium=9

cost_slow=0.32
power_slow= 1.6

battery_size=100
range_miles=400

starting_miles=400
forward_miles=350

time_spent=0.25
cost=time_spent*cost_fast*power_fast
miles_added=time_spent*power_fast*(range_miles/battery_size)
end_miles=forward_miles+miles_added
print('Car starts with:',starting_miles)
print('Drives to shop and has',forward_miles,'when it arrives')
print('Stays for:',time_spent)
print('Cost of charge:',cost)
print('The car now has',end_miles,'miles')










