'''
Steps to Create an OTP Verification Systel using Python

1. First,we will create a 6 digit random number.
2. Than we will store this number to a variable
3. Then we need to write a program to send the eamil 
4. When sending the email,we need to use the OTP as a message.
5. FInally we need to request 2 user input, first for the user's email and then for the OTP that the user has received
'''

import os
import math
import random
import smtplib

digits = "0123456789"
OTP = ""
for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
    otp = OTP + " is your OTP"
    msg = otp

s =smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("Your Gmail Account", "Your App Password")  # 
emailid = input("Please Enter your email : ")
s.sendmail('&&&&&&&&&&&', emailid, msg)
a = input ("Please Enter your OTP >> : ")

if a == OTP:
    print("Yes, Your OTP is Verified.")
else:
    print("Please check your OTP Again")