# create a file and open it in write mode
# f = open("test.txt", "w")
# f.write("Hello World\n")
# f.writelines(["Welcome\n", "To\n", "Tops\n"])
# f.close()

# Append mode : koi file ke end me data add karna ho to use append mode
# f = open("test.txt", "a")
# f.write("Hello Raj\n") # single line add karne ke liye
# f.writelines(["Welcome\n", "To\n", "Tops\n"]) # multiple line add karne ke liye
# f.write("Python\n") # single line add karne ke liye
# f.close()

# Read mode : file ke data ko read karne ke liye use hota hai
# f = open("test.txt", "r")
# data = f.read() # pura file ka data read karne ke liye
# print(data)
# f.close()

# Readline() : file ke data ko line by line read karne ke liye use hota hai
# f = open("test.txt", "r")
# data = f.readline() # single line read karne ke liye
# print(data)
# f.close()

# f = open("test.txt", "r")
# while True:
#     data = f.readline()
#     print(data)
#     if not data:
#         break

# f = open("test.txt", "r")
# while True:
#     data = f.readline()
#     if 'e'  in data:
#         print(data)
#     if not data:
#         break
    
# f = open("test.txt", "r")
# while True:
#     data = f.readline()
#     if data.startswith('p'):
#         print(data)
#     if not data:
#         break

# with open("home.txt", "w") as f:
#     f.write("Write Something")

# # Seek And Tell : file ke pointer ko move karne ke liye use hota hai
# with open("home.txt", "r") as f:
#     print(f.tell()) # current position of pointer
#     f.seek(5) # move pointer to 10th position
#     data = f.read() # read data from 10th position
#     print(f.tell()) # current position of pointer
#     print(data)

# a+ mode : file me data ko read aur write dono karne ke liye use hota hai
# with open("abc.txt", "a+") as f:
#     f.write("Hello World")
#     f.seek(0) # move pointer to the beginning of the file
#     data = f.read() # read data from the file
#     print(data)

# # rb mode : file ko binary mode me read karne ke liye use hota hai
# rb mode : image file ko read karne ke liye use hota hai
# with open("abc.png", "rb") as f:
#     data = f.read() # read data from the file
#     print(data)

# json file handling : json file me data ko store karne ke liye use hota hai
import json
# d = {"name": "Raj", "age": 25, "city": "Delhi"}
# with open("data.json", "w") as f:
#     json.dump(d, f) # json file me data ko store karne ke liye use hota hai

# read mode me json file ko read karne ke liye use hota hai
with open("data.json", "r") as f:
    data = json.load(f) # json file se data ko read karne ke liye use hota hai
    print(data)


