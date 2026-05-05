# Iterator :- ek ek item ko ek time par access karne ke liye use kiya jata hai.
# l = [10,20,30,40,50,60,70]
# itr = iter(l) # iter function se ek iterator object banata hai jisme list ke sabhi items ko store karega
# print(next(itr)) # next function se iterator object ke next item ko print karega
# print(next(itr)) # next function se iterator object ke next item ko print karega
# print("Hello World") # print karega
# print(next(itr)) # next function se iterator object ke next item ko print karega

# generator :- ek ek item ko ek time par access karne ke liye use kiya jata hai. generator function ke andar yield keyword ka use kiya jata hai.
# using yeild keyword generator function ke andar ek item ko return karta hai aur generator function ko pause kar deta hai. next function se generator object ke next item ko print karega. generator function se ek generator object banata hai jisme generator function ke sabhi items ko store karega.
# def gen():
#     yield 10 # yield keyword se generator function ke andar ek item ko return karta hai aur generator function ko pause kar deta hai
#     yield 20 # yield keyword se generator function ke andar ek item ko return karta hai aur generator function ko pause kar deta hai
#     yield 30 # yield keyword se generator function ke andar ek item ko return karta hai aur generator function ko pause kar deta hai
# g = gen() # generator function se ek generator object banata hai jisme generator function ke sabhi items ko store karega
# print(next(g)) # next function se generator object ke next item ko print karega
# print(next(g)) # next function se generator object ke next item ko print karega
# print("Hello World") # print karega


# def test():
#     yield "Hello"
#     yield "World"
# itr = test() # generator function se ek generator object banata hai jisme generator function ke sabhi items ko store karega
# print(next(itr)) # next function se generator object ke next item ko print karega
# print(next(itr)) # next function se generator object ke next item ko print karega

# square generator
def square(a):
    for i in range(a):
        yield i*i # yield keyword se generator function ke andar ek item ko return karta hai aur generator function ko pause kar deta hai
itr = square(5) # generator function se ek generator object banata hai jisme generator function ke sabhi items ko store karega
print(next(itr)) # next function se generator object ke next item ko print karega
print(next(itr)) # next function se generator object ke next item ko print karega
print(next(itr)) # next function se generator object ke next item ko print karega
print(next(itr)) # next function se generator object ke next item ko print karega
print(next(itr)) # next function se generator object ke next item ko print karega

