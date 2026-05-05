# filter function 
# normal example odd numbers find karne ke liye
# a = [1,2,3,4,5,6,7,8,9,10]
# k = [] # empty list banata hai jisme even numbers ko store karega
# def checkodd(a):
#     if a%2!=0: # check karega ki number odd hai ya nahi
#         return a
# for i in a:
#     if checkodd(i): # function call karega aur check karega ki number odd hai ya nahi
#         k.append(i) # agar number odd hai to usko list me add karega
# print(k) # odd numbers print karega

# # other example odd numbers find karne ke liye
# a = [1,2,3,4,5,6,7,8,9,10]
# def checkodd(a):
#     if a%2!=0: # check karega ki number odd hai ya nahi
#         return a
# k = filter(checkodd, a) # filter function se ek naya list banata hai jisme list ke sabhi items ko checkodd function ke through check karega ki wo odd hai ya nahi
# print(list(k)) # filter object ko list me convert kar ke print karega



# find even numbers from a list using filter function and lambda function
# a = [1,2,3,4,5,6,7,8,9,10]
# k = filter(lambda x: x%2==0, a) # filter function se ek naya list banata hai jisme list ke sabhi items ko lambda function ke through check karega ki wo even hai ya nahi
# print(list(k)) # filter object ko list me convert kar ke print karega

# # find odd numbers from a list using filter function and lambda function
# k = filter(lambda x: x%2!=0, a) # filter function se ek naya list banata hai jisme list ke sabhi items ko lambda function ke through check karega ki wo odd hai ya nahi
# print(list(k)) # filter object ko list me convert kar ke print karega

# find letter starting words from p list using filter function and lambda function
sub = ["java", "python", "node", "php", "android"]
# example
k = filter(lambda element : "a" in element, sub)
print(list(k)) # filter object ko list me convert kar ke print karega
# # first example
# k = filter(lambda a: a.startswith("p"), sub) # filter function se ek naya list banata hai jisme list ke sabhi items ko lambda function ke through check karega ki unka length 4 se bada hai ya nahi
# print(list(k)) # filter object ko list me convert kar ke print karega

#second example
def checklength(a):
    if a.startswith("p"): # check karega ki string "p" se start hoti hai ya nahi
        return a
k = filter(checklength, sub) # filter function se ek naya list banata hai jisme list ke sabhi items ko checklength function ke through check karega ki unka length 4 se bada hai ya nahi
print(list(k)) # filter object ko list me convert kar ke print karega

# # find letter inside words from a list using filter function and lambda function
# # first example
# k = filter(lambda a: "a" in a, sub) # filter function se ek naya list banata hai jisme list ke sabhi items ko lambda function ke through check karega ki unme "a" hai ya nahi
# print(list(k)) # filter object ko list me convert kar ke print karega

# #second example
# def checkletter(a):
#     if "a" in a: # check karega ki string me "a" hai ya nahi
#         return a
# k = filter(checkletter, sub) # filter function se ek naya list banata hai jisme list ke sabhi items ko checkletter function ke through check karega ki unme "a" hai ya nahi
# print(list(k)) # filter object ko list me convert kar ke print karega
