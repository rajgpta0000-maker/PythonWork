# Assessment:
# • Create a mini-project where students combine conditional statements, loops, and functions
# to create a basic Python application, such as a simple calculator or a grade management
# system.
a = int(input("Enter a number: "))
print(a)
B = int(input("Enter b number: "))
print(B)

choice = "yes"
while choice != "no":
    ch=int(input("Enter your choice: "))
    match ch:
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

    choice = input("Do you want to continue? (yes/no): ")