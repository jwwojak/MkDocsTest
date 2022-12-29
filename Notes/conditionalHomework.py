# Homework 2
# Ask user for a number.
# Tell them the number is positive and even.
# Tell them the number is an odd positive number.
# Tell them the number is negative and even.
# Tell them the number is negative and odd.
# Create a condition for 0. Just say, "your number is 0."

#myNumber=float(input('Input a number: '))
#if(myNumber % 2==0): # Says if the remainder of a number / 2 is 0, then it is even.
#    print('The number is even.')
#if(myNumber % 2 !=0): # Says if the remainder of a number / 2 is not 0, then it is odd.
#    print('The number is odd.')


myNumber=float(input('Input a number: '))
if (myNumber % 2==0 and myNumber<0):
    print('Your number is negative and even.')
if (myNumber % 2==0 and myNumber>0):
    print('Your number is positive and even.')
if (myNumber % 2!=0 and myNumber<0):
    print('Your number is negative and odd.')
if (myNumber % 2!=0 and myNumber>0):
    print('Your number is positive and odd.')
if (myNumber==0):
    print('Your number equals 0.')

