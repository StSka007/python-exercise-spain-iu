"""
попросите пользователя ввести имя и его возраст / распечатать сообщение, адресованное им, в котором говорится, в каком году ему исполнится 75 лет.
"""

import datetime


print('What is your name?')
name = input()

print('What is your age?')
age = int(input())

print('What age are you interested in? [75]')
age_interest = int(input() or 0) or 75

year = datetime.datetime.now().year
year_interest = (age_interest - age) + year

print("{n}, you will be {i} years old at {y}".format(n=name, y=year_interest, i=age_interest))
