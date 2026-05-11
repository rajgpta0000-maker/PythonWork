# try :- problematic code
# except :- handle the problem
# else :- try executed successfully
# finally :- always executed

print("Program Started")
try :
    a = 10 
    b = a/0
    print(b)
except ZeroDivisionError as e:
    print(e)
else:
    print("something went wrong")
finally:
    print("Always executed")
print("Program Ended")