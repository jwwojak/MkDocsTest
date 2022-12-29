# Compound Conditionals

#myColor=input('Specify a color: ')
#if (myColor=='red' or myColor=='red' or myColor=='RED'): # Using the OR conditional. Any of these can be true.
#    print('Your color is red.')
#if (myColor!='red' and myColor!='red' and myColor!='RED'): #All of these must be true, i.e. not equal to ...
#    print('Your color is not red.')

# Homework
# Ask user for a number.
# Tell them if it is between 5 and 10.
# If it is not between 5 and 10, tell them it is not in that range.

myNumber=float(input('Input a number: '))
if (myNumber>=5 and myNumber<=10):
    print('Your number is between 5 and 10.')
if (myNumber<5 or myNumber>10):
    print('Your number is less than 5 or greater than 10.')


# Homework 2
# Ask user for a number.
# Tell them the number is positive and even.
# Tell them the number is an odd positive number.
# Tell them the number is negative and even.
# Tell them the number is negative and odd.
# Create a condition for 0. Just say, "your number is 0."
