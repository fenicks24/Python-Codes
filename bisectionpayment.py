# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:16:13 2018

@author: Ricardo Roberts
"""

"""
Biscetion search to calculate lowest monthly payment amount on a given principal balance

"""

annualInterestRate = 0.05
balance = 40000

annualInterestRate = float(input("What is the annual interest rate?\n"))

balance = float(input("How much money are you borrowing?\n"))

low = balance/12
high = (balance*((1+ (annualInterestRate / 12))**12))/12
guess = (high + low)/2.0
i = 0
bal = balance
while i < 12:
    
    for i in range(12):
        monbal = round((balance - guess) + ((balance - guess)* (annualInterestRate/12)), 2)
        balance = monbal
#        print(i, guess, balance, bal)
    if balance > 0:
        low = guess
    elif balance < 0:
        high = guess
    else:
        print('\nLowest Monthly Payment: $', float(round(guess, 2)))
        break
    guess = (high + low)/2.0   
    balance = bal