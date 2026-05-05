# Write a Python program to apply the map() function to square a list of numbers.
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]
# Use the map() function to square each number in the list
squared_numbers = map(lambda x: x ** 2, numbers)
# Convert the map object to a list and print the squared numbers
squared_numbers_list = list(squared_numbers)
print(squared_numbers_list)
