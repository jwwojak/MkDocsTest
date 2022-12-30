# Homework
# Ask user for number of grades.
# Let them input each grade, e.g. 5 grades = 5 inputs
# Print grades, 2 FOR loops: one to read in, one to read out.

#numGrades=int(input('How many grades do you have: ')) # input tells code how many grades
#grades=[] # empty array to hold grades
#for i in range(0,numGrades,1): # i is just a var. can be anything. In parens, array counting starts at 0.
# Also, 'range' can't read float so numGrades has to be an int.
#    grade=float(input('Input your grades: ')) #accepts grades as a float
#    grades.append(grade) #puts grades in array 'grades'
#    print(grades) #show you the array getting populated, but you don't need it. Try this with and without to see difference.
#print('Your grades are as follows:')
#for i in range(0,numGrades,1): #print the vars (i) from the array.
#    print(grades[i])
#print('End of grades.')

# This works by putting numbers in an array
# You have to remember to create an array to hold the grades
# Review the array lesson

#Homework 2

# Ask user for number of grades
# Put in array
# Average the grades
# Print average and all grades
# Hint: requires 3 FOR loops - input, average, and print

numGrades=int(input('How many grades do you have: '))
grades=[]
sum=0
for i in range(0,numGrades,1):
    grade=float(input('Input your grades:'))
    grades.append(grade)
for i in grades:
    sum += i
    res = sum/len(grades)
for i in range(0,numGrades,1):
    print('Your grade is:', grades[i])
print('Your grade average is:' + str(res))
