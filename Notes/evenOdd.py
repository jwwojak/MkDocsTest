# Get input from user, tell them if it is even or odd
# Use the modulus operator %.
# This gives you the remainder of a division operator (if a number / 2 has a remainder of 0 it is even)

myNumber=float(input('Input a number: '))
if(myNumber % 2==0): # Says if the remainder of a number / 2 is 0, then it is even.
    print('The number is even.')
if(myNumber % 2 !=0): # Says if the remainder of a number / 2 is not 0, then it is odd.
    print('The number is odd.')

# Another way: set new var for the remainder and check if it is 0 or 1

#myNumber=float(input('Input a number: '))
#rem=myNumber%2
#if(rem==0):
#    print('The number is even.')
#if(rem!=0):
#    print('The number is odd.')
