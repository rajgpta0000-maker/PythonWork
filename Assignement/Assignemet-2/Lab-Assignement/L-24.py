# Write a Python program to merge two lists into one dictionary using a loop. 
keys = ["name", "age", "city"]
values = ["Alice", 30, "New York"]
# Create an empty dictionary
merged_dict = {}
# Merge the lists into a dictionary
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]
# Print the merged dictionary
print("Merged Dictionary:", merged_dict)