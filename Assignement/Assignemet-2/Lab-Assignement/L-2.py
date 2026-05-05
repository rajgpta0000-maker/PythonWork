# Write a Python program that uses a custom iterator to iterate over a list of integers. 
class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
# Create a list of integers
numbers = [1, 2, 3, 4, 5]
# Create an instance of the custom iterator
iterator = CustomIterator(numbers)
# Iterate over the list using the custom iterator
for number in iterator:
    print(number)
    