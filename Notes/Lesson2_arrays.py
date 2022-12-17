Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Grade1=97
Grade2=98
Grade3=78
print(Grade2)
98
print(Grade2 + Grade3)
176
grades=[97,98,76,54,99,85,67]

print(grades)
[97, 98, 76, 54, 99, 85, 67]
# grades=[ ] in square brackets is an array
# access individual array elements, address items in an array
print(grades[1])
98
print(grades[2])#counting in an array starts at 0
76
#this means 97 is position 0, 98 is position 1, 76 is position 2, etc.
print(grades[1])
98
#make a var and assign it a value based on adding grades
x=grades[0]+grades[6] #should be 97+67
print(x)
164
print(grades[0,1])
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(grades[0,1])
TypeError: list indices must be integers or slices, not tuple
print(grades[0],[1])
97 [1]
print(grades[0][1])
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    print(grades[0][1])
TypeError: 'int' object is not subscriptable
grades[3]
54
picture=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(picture)
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
picture
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(picture[1])#print positon 1
[5, 6, 7, 8]
picture[0]
[1, 2, 3, 4]
>>> print(picture[2])
[9, 10, 11, 12]
>>> picture[2]
[9, 10, 11, 12]
>>> # Now, address an individual number in these arrays
>>> # Put an index on the array to get an individual number
>>> # Put an index on the array to get an individual number
>>> # Example: get row 1, column 2
>>> print(picture[1][2])#should return 7
7
>>> # strings in arrays, not just numbers
>>> fruits=['apple','banana','orange','grape']
>>> fruits
['apple', 'banana', 'orange', 'grape']
>>> print(fruits[1])#should get banana
banana
>>> fruits[1]
'banana'
>>> print(fruit[1][2])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(fruit[1][2])
NameError: name 'fruit' is not defined. Did you mean: 'fruits'?
>>> fruits([1][2])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    fruits([1][2])
IndexError: list index out of range
>>> print(fruits[1][2])
n
>>> # So, what happened above? fruits[1] is banana, but [2] interpreted as element 2 in banana, which is letter n.
>>> # This 'indexed' the string "banana"
>>> # Test with input grades
>>> grades=[97,98,76,54,99,85,67]
>>> print(grades)
[97, 98, 76, 54, 99, 85, 67]
>>> # Now, change a grade
>>> grades[1]=25 #should change 98 to 25
>>> grades[1]=25 #should change 98 to 25
print(grades)
[97, 25, 76, 54, 99, 85, 67]
# empty array
x=[]
# try to add a number to the array
x=[1]=97
SyntaxError: cannot assign to literal
x[1]=97
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x[1]=97
IndexError: list assignment index out of range
print(x)
[]
# Use 'append' function to add to the array
x.append(97)
print(x)
[97]
# Now you can fill up the x array
x.append(85)
print(x)
[97, 85]
print(x[1])#print position 1 in x array
85
print(x[1][1])
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print(x[1][1])
TypeError: 'int' object is not subscriptable
