# Write a Python program to sort a list using both sort() and sorted(). 
# Create a list of unsorted numbers
unsorted_list = [5, 2, 9, 1, 5, 6]
# Sort the list using the sort() method (this will modify the original list)
unsorted_list.sort()
print("Sorted list using sort():", unsorted_list)
# Create another list of unsorted numbers
another_unsorted_list = [3, 8, 4, 2, 7]
# Sort the list using the sorted() function (this will return a new sorted list)
sorted_list = sorted(another_unsorted_list)
print("Sorted list using sorted():", sorted_list)
