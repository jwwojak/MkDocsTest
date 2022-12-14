# Lesson 1 Notes

## Starting

- Downloaded Python
- Configured `PATH`

## Variables

Hello World exercise.

Created "greeting" as a variable: `greeting=('Hello World')`. It is a string variable.

Print to screen: `print(greeting)`

Created 3 other variables:

- `name='Joe'`
- `msg1='Hello'`
- `msg2='welcome to Python'`

Combine them: `print(msg1,name,msg2)` returns `Hello Joe welcome to python`.

## Exponents and formulas

Multiplication: Set variable values and print.

```python
x=2
y=3
z=x*y
print(z)
6
```

Calculate radius and circumference, generate text output.

```python
radius=3 #set the radius value
circumference=2*3.14*radius #formula is 2 x pi x radius

# generate output
print(circumference)
18.84
```

Now area.

```python
radius=3
area=3.14*radius**2 #formula is pi x radius^2. These ** give the square

#generate output
print(area)
28.26
```

Add descriptive text.

```python
print('A circle of radius',radius,'has an area of',area,'and circumference of',circumference)

A circle of radius 3 has an area of 28.26 and circumference of 18.84
```
