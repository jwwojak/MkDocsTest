# For loops lesson 9

#fruit=['apple','orange','banana','mango','kiwi']
#print(fruit[1:4]) # Note the : here. That lets you specify a range. Print array index 1 to 4.

# Result above is print orange to mango. Why?
# When counting in an array with 1:4, it stops at position 4 BUT DOESN'T PRINT IT!
# Instead, [1:4] prints "orange, banana, mango", which are array items 1-3. 
# It doesn't use the upper limit. Uses one below it. Weird.

#fruits=['apple','orange','banana','mango','kiwi']
#fruit=fruits[2]
#print(fruit)

#fruits=['apple','orange','banana','mango','kiwi']
#for fruit in fruits:
#    print(fruit) # 'fruit' in the FOR loop steps through 'fruits' and prints it as a list.
#print('Thats the entire list.')

#fruits=['apple','orange','banana','mango','kiwi']
#for fruit in fruits:
#    print(fruit) # 'fruit' in the FOR loop steps through 'fruits' and prints it as a list.
#    for letter in fruit:
#        print(letter)
#print('Thats the entire list.')

# The 2nd FOR loop prints each letter in each fruit or in each array item.
# The var 'letter' can be anything, e.g. 'l'. 

# Count numbers
myNumbers=[1,2,3,4,5,6,7,8,9,10]
for myNumber in myNumbers:
    print(myNumber)
print('End of list.')


# Range function so you don't have to type a whole list of numbers or items.
# Range function generates the list.
# Note below the range goes to 11 in order to get 10.

#for myNumber in range(1,11,1): # Range argument is 'start int', 'stop int', 'increment'

#    print(myNumber)
#print('End of list')

# Count even numbers in a range

#for myNumber in range(10,21,2):
#    print(myNumber)
#print('End of list.')

# Count backwards

for myNumber in range(10,-1,-1): # To get 0, we need to set the lower boundary at -1.
    print(myNumber)
print('End of list.')

# Homework
# Ask user for number of grades.
# Let them input each grade, e.g. 5 grades = 5 inputs
# Print grades, 2 FOR loops: one to read in, one to read out.
