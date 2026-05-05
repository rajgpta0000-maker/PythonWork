# Write a Python program to remove elements from a list using pop() and remove(). 
# Create a list of elements
my_list = [1, 2, 3, 4, 5]
# Use pop() to remove an element at a specific index
popped_element = my_list.pop(2)  # This will remove the element at index 2 (which is 3)
# Use remove() to remove a specific element by value
my_list.remove(4)  # This will remove the element with value 4
# Print the final list and the popped element
print("Final list:", my_list)
print("Popped element:", popped_element)
