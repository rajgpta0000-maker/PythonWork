# recursion is a function that calls itself
def square(a):
    print(a*a)
    a+=1
    if a <= 10:
        square(a) # function call itself
square(1) # function call with argument

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) # function call itself with argument n-1
result = factorial(5) # function call with argument and return value
print(result)
