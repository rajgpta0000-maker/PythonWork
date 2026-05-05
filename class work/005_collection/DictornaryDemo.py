# person = {
#     "Name" : "Raj",
#     "Age" : 25,
#     "City" : "Delhi",
#     "lang" : ["Hindi", "English"],
#     123 : "abc",
#     True : "boolean",
#     (10,20,30) : "tuple"
#     [10,20,30] : "list"
# }
# print(person)

# other way to create dictionary
# d=dict(name="Raj", age=25, city="Delhi")
# print(d)

cn = {
    "india" : "IN",
    "usa" : "US",
    "australia" : "AUS",

}
# print(cn)
# print(cn.get("india")) # returns None if key is not found
# # print(cn['usa1']) # raises KeyError if key is not found
# print("Hello") # will be printed even if key is not found

# print(cn.keys()) # shows all keys in the dictionary
# print(cn.values()) # shows all values in the dictionary
# print(cn.items()) # shows all key-value pairs in the dictionary

# for i,j in cn.items(): # i ma key ko store karega aur j value ko store karega
#     print(i,j)

# cn["india"] = "INR" # update hota hai
# cn.update({"abc":"xyz","india" : "INR"}) # update or add hota hai
# print(cn)

# cn.pop("india")  # key ko remove karta hai
# cn.popitem() # last item ko remove karta hai
# cn.clear() # sabhi items ko remove karta hai
# del cn # dictionary ko delete kar deta hai
# print(cn)

# k = cn.copy() # dictionary ka copy banata hai
# k= cn # k aur cn dono same dictionary ko point kar rahe hai
# k.update({"abc":"xyz"}) # update karta hai to dono dictionary update ho jati hai
# print(k)
# print(cn)



# for i,j in students["marks"].items(): # nested dictionary me loop lagane ke liye
#     print(i,j)

#     x = ('key1', 'key2', 'key3')
#     y = 0
#     print(dict.fromkeys(x,y)) # fromkeys method se ek naya dictionary banata hai jisme keys x ke elements honge aur unki value y hogi

#     thisdict = dict.fromkeys(x,y)
#     print(thisdict)
# # print(students) # all items print karega
# # print(students["name"]) # specific key ka value print karega
# # print(students["marks"]["python"]) # nested dictionary me specific key ka value print karega

x = ("key1", "key2", "key3")
y = (10,20,30)

d = zip(x,y) # zip function se do list ko ek saath zip kar sakte hai
print(list(d)) # zip object ko list me convert kar ke print karega
print(tuple(d)) # zip object ko tuple me convert kar ke print karega
print(set(d)) # zip object ko set me convert kar ke print karega

k = {"a":1, "b":2, "c":3}
k.setdefault("d",4) # setdefault method se agar key exist nahi karti hai to usko add kar deta hai aur uski value set kar deta hai
k['b'] = 20 # agar key exist karti hai to uski value update kar deta hai
print(k)