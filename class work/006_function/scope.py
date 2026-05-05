# Scope of Variables in Python
# simple example to understand the scope of variables in Python
# a = 10  # Global variable
# def test():
#     a = 20  # Local variable
#     print(a)
# print(a) # prints global variable
# test() # prints local variable
# print(a) # prints global variable


# global variable ko function ke andar modify karne ke liye global keyword ka use karte hai
a = 10  # Global variable
def test():
    global a  # to modify the global variable inside the function
    a = 20  # Local variable
    print(a)
print(a) # prints global variable
test() # prints local variable
print(a) # prints global variable