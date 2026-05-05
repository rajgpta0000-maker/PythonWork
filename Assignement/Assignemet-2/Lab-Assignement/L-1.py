# Write a generator function that generates the first 10 even numbers. 
def even_numbers(n):
    for i in range(n):
        yield 2 * i
# Create a generator object
even_gen = even_numbers(10)
# Iterate through the generator and print the even numbers
for even in even_gen:
    print(even)
                    