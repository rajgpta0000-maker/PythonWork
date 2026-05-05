# Write a Python program that filters out even numbers using the filter() function.
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use the filter() function to filter out even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# Convert the filter object to a list and print the even numbers
even_numbers_list = list(even_numbers)
print(even_numbers_list)
