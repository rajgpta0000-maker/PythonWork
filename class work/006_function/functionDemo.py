# Function definition
# 
# def message():
#     print("Hello World")
# message() # function call

#
# def square(a):
#     print(a*a)
# square(5) # function call with argument

# def add(a,b):
#     print(a+b)
# add(10,20) # function call with arguments

# def cube(a):
#     q = a*a*a
#     return q # function return value
# result = cube(3) # function call with argument and return value
# print(result)  

# Default arguments
# def person(name,email,age):
#     print(name,email,age)
# person("Raj","raj@example.com",25)

# keyword arguments
# def person(name,email="raj@example.com",age=0):
#     print(name,email,age)
# person(name="Raj",age=25)

# arbitrary arguments
# def add(*a):
#     sum = 0
#     for i in a:
#         sum += i
#     print(sum)
# add(10,20,30) # function call with arbitrary arguments

# arbitrary keyword arguments
# def person(**k):
#     print(k)
# person(name="Raj",email="raj@example.com",age=25) # function call with arbitrary keyword arguments

# lambda function
# function without name is called lambda function
add = lambda x,y: x+y # lambda function to add two numbers
square = lambda x: x*x # lambda function to find square of a number
print(add(10,20)) # function call with arguments
print(square(5)) # function call with argument
