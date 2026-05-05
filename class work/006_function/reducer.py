# reducer = writen a single value return by applying a function to an iterabl0
# manually way to add all items in a list
l = [10,20,30,40,50,60,70]
def sum(a,b):
    return a+b;
k = 0
for i in l:
    k = sum(k,i) # sum function ke through list ke sabhi items ko add karega
print(k) # list ke sabhi items ka sum print karega

#reducer automatic way to add all items in a list
# from functools import reduce
# l = [1,2,3,4,5]
# def sum(a,b):
#     print(a,b) # reduce function ke through list ke sabhi items ko add karne ke process ko print karega
#     return a+b;
# r = reduce(sum, l) # reduce function se ek single value return karta hai jisme list ke sabhi items ko sum function ke through add karega
# print(r) # reduce object ko print karega


# from functools import reduce

# l = [10,20,30,40,50,60,70,41,58,68]
# r = reduce(lambda a,b: a+b, l) # reduce function se ek single value return karta hai jisme list ke sabhi items ko lambda function ke through add karega
# r = reduce(lambda a,b: a if a>b else b, l) # reduce function se ek single value return karta hai jisme list ke sabhi items ko lambda function ke through compare karega aur jo bada hoga usko return karega
# r = reduce(lambda a,b: a if a<b else b, l) # reduce function se ek single value return karta hai jisme list ke sabhi items ko lambda function ke through compare karega aur jo chota hoga usko return karega
# print(r) # reduce object ko print karega
