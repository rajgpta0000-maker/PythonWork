# map function ka use ek list ke sabhi items par ek function apply karne ke liye kiya jata hai.
# a = [1,2,3,4,5,6,7]
# k = map(lambda x: x*x, a) # map function se ek naya list banata hai jisme list ke sabhi items ko lambda function ke through square karega
# print(list(k)) # map object ko list me convert kar ke print karega

# other example
# a = [1,2,3,4,5,6,7]
# k = []


# length count karne ke liye
# sub = ["java", "python", "node", "php", "android"]
# length = map(len, sub) # map function se ek naya list banata hai jisme list ke sabhi items ke length ko add karega
# print(list(length)) # map object ko list me convert kar ke print karega

other example
sub = ["java", "python", "node", "php", "android"]
k = map(lambda a: len(a), sub) # map function se ek naya list banata hai jisme list ke sabhi items ke length ko lambda function ke through add karega
print(list(k)) # map object ko list me convert kar ke print karega