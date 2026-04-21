# number = 11
# flag = 0
# for i in range(2,number):
#     if number%i==0:
#         flag=1
#         break

# if flag==0:
#     print("prime number")
# else:
#     print(" not a Prime number")

# for j in range(3, 100):

#     number = j
#     flag = 0
#     for i in range(2, number):
#         if number % i == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(j, "prime number")
#     else:
#         pass


count = 0
for num in range(3, 101):
    for i in range(2, int (num*0.5+1)):
        if num % i == 0:
            break
        else:
            count += 1
        print("total prime numbers: ", count)

    
       

        


