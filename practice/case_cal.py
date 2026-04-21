a = int(input("Enter a number: "))
print(a)
B = int(input("Enter b number: "))
print(B)

choice = "yes"
while choice != "no":
    ch=int(input("Enter your choice: "))
    match ch:
match choice:
        case 1:
            print("Addition is: ", a + B)
        case 2:
            print("Subtraction is: ", a - B)
        case 3:
            print("Multiplication is: ", a * B)
        case 4:
            print("Division is: ", a / B)
        case _:
            print("Invalid choice")

