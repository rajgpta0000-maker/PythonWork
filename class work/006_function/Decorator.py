# decorates:- 

# def after(func):
#     def execute():
#         func()
#         print("calling after test")
#     return execute


# def before(func):
#     def execute():
#         print("calling before test")
#         func()
#     return execute

# @after
# @before
# def test():
#     print("Hello World")
    
# test()


# create a decorator for functions with parameter

# def add(func):
#     def execute(*a):
#         print("Addition below")
#         sum = 0 
#         for i in a:
#             sum+=i
#         print("Addition is sum =",sum)
#         func(*a)
#     return execute

# @add
# @mul
# def calc(a,b):
#     pass
# calc(20,30)


# def mul(func):
#     def execute(*a):
#         print("Multiplication below")
#         sum = 1
#         for i in a:
#             sum*=i
#         print("Multiplication is =",sum)
#         func(*a)
#     return execute


# @mul
# @add
# def calc(a,b):
#     pass
# calc(10,20)


# def numbersOnly(func):
#     def execute(a):
#         if str(a).isdigit():
#             func(a)
#         else:
#             print("Invalid Input")
#     return execute

# def onlyalpha(func):
#     def execute(a):
#         if str(a).isalpha():
#             func(a)
#         else:
#             print("Invalid Input")
#     return execute


# # @numbersOnly
# @onlyalpha
# def get(a):
#     print(a)

# get("Raj10")