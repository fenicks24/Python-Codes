# -*- coding: utf-8 -*-
"""
Created on Mon May 28 01:56:27 2018

@author: Ricardo Roberts
"""
"""
Calculates balance owed after 12 month period on principal plus interest loans

"""
monthlyPaymentRate =0.02
annualInterestRate = 0.25
balance = 42

print("This calculator will provide an estimate of the balance oweing after a 12-month period")

balance = float(input("How much money to you owe? \n"))

annualInterestRate = float(input("What is the annual interest rate? \n"))

monthlyPaymentRate = float(input("At what rate monthly are you paying the principal balance? \n"))

i = 1
while i <=12:
    rb = balance - round((monthlyPaymentRate *balance), 2)
    balance = round(rb + (annualInterestRate/12)*rb, 2)
    i +=1
print('Remaining balance: $' + str(balance))