# Use == check if 2 things are equal
# Check if not =, use !=
#  Less than: <
#  Greater than: >

# If statement with a string

#myColor=input('Please input a color: ')
#if(myColor=='red'):
#    print('Your color is red.')
#if(myColor!='red'):
#    print('Your color is not red.')

# If statement with a number

#myNumber=float(input('Please input a number: '))
#if(myNumber==7):
#    print('Your number is 7')
#if(myNumber!=7):
#    print('Your number is not 7')

# Comparing with < >

#myNumber=float(input('Please input a number: '))
#if(myNumber==7):
#    print('Your number is 7')
#if(myNumber<7):
#    print('Your number is less than 7')
#if(myNumber>7):
#    print('Your number is greater than 7')

# Get input from user, tell them if it is even or odd
# Use the modulus operator %.
# This gives you the remainder of a division operator (if a number / 2 has a remainder of 0 it is even)

myNumber=float(input('Input a number: '))
if(myNumber % 2==0): # Says if the remainder of a number / 2 is 0, then it is even.
    print('The number is even.')
if(myNumber % 2 !=0): # Says if the remainder of a number / 2 is not 0, then it is odd.
    print('The number is odd.')
