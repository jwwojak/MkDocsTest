# Homework: Getting input and summing it

# assignment
# ask user for a number
# ask user for 2nd number
# x = number, y = number, z=x+y
# format output, include equation with a sum

# This doesn't work:
# x=input('Enter a first number: ')
# y=input('Enter a second number: ')
# z=x+y
# print(z)
# The results aren't a sum. They're a concatinaton of the 2 numbers.
# To sum, you nee to change what Python sees as a string to a number
# with float or int.

# This works, tell Python to see the string as a number with float or int

#x=input('Type a number: ')
#y=input('Type another number: ')
#x=int(x) #turn the string to a number
#y=int(y) #could also use float
#z=x+y #now you can add numbers
#print(x,' + ',y,' = ',z)

# Can also do this

x=float(input('Type a number: ')) #or use an int for this simple example
y=float(input('Type another number: '))
z=x+y #now you can add numbers
print(x,' + ',y,' = ',z)
