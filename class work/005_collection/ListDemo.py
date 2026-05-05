# l = [10, 20, 30, 40, 50, 50, "abc", True, 10.5]
# l = list((10, 20, 30, 40, 50, 50))
# print(l)
# print(type(l))
# print(l[0])
# print(len(l))

# Accessing list items
# l = [10, 20, 30, 40, 50, 50]
# print(l[0]) # first item
# print(l[-1]) # last item
# print(l[1:4]) # slice of list from index 1 to 3
# print(l[:3]) # slice of list from start to index 2
# print(l[3:]) # slice of list from index 3 to end
# print(l[::2]) # slice of list with step 2

# Changing list items
# l = [10, 20, 30, 40, 50, 50]
# l[0] = 100 # change first item to 100
# l[1:4] = [200, 300, 400] # change slice of list from index 1 to 3
# l.append(60) # add 60 at the end of the list
# l.insert(2, 25) # insert 25 at index 2
# l[:5] = [45,46,78,98,98,74,85,41]   # change slice of list from index 0 to 4 and add more items than the original slice
# print(l)   

# a = [10, 20, 30]
# b = [40, 50, 60]
# a.extend(b) # extend method se ek list ke items ko dusre list me add kar sakte hai
# print(a)

# remove items from list
l = [10, 20, 30, 40, 50, 50]
# l.remove(20) # remove method se list me se pehli occurrence of 50 ko remove karega
# l.pop() # pop method se list me se last item ko remove karega
# l.pop(1) # pop method se list me se index 1 ke item ko remove

# l.clear() # clear method se list me se sabhi items ko remove karega
# del l # del statement se list ko delete kar dega
# print(l)

# for i in l:
#     print(i) # loop se list ke sabhi items ko print karega

# for i in range(len(l)):
#     print(l[i]) # loop se list ke sabhi items ko index ke through print karega

# i=0
# while i < len(l):
#     print(l[i])
#     i += 1 # while loop se list ke sabhi items ko index ke through print karega

# s = ["python", "java", "c++", "c", "javascript"]
# l = []
# for i in s:
#     if "a" in i: # if statement se check karega ki string me "a" hai ya nahi
#         l.append(i) # if condition true hone par list me string ko add karega
# print(l)

# l = [i for i in s if "a" in i] # list comprehension se ek naya list banata hai jisme string me "a" hone par usko add karega
# print(l)

# k = [i for i in s if i.startswith("c")] # list comprehension se ek naya list banata hai jisme string "c" se start hone par usko add karega
# print(k)

# s = ["python", "java", "c++", "c", "javascript"]
# s.sort() # sort method se list ke items ko ascending order me sort karega
# s.sort(reverse=True) # sort method se list ke items ko descending order me sort karega
# s.reverse() # reverse method se list ke items ko reverse order me sort karega
# print(s)

# k = sorted(s) # sorted function se list ke items ko ascending order me sort karega aur ek naya list banayega
# print(k)

# k = s
# k = s.copy() # copy method se list ka ek naya copy banayega
# k = list(s) # list function se list ka ek naya copy banayega
# k = s[:] # slicing se list ka ek naya copy banayega

# k.append("ruby") # list ke items ko add karega
# print(k)
# print(s) # original list me koi change nahi hoga kyunki k ek naya copy hai s ka

l = [10, 20, 30, 40, 50, 50]
# print(l.count(50)) # count method se list me 50 ki occurrence count karega
# print(max(l)) # max function se list me sabse bada item print karega
# print(min(l)) # min function se list me sabse chhota item print karega
# print(l.index(30)) # index method se list me 30 ki index print karega

# for i in range(len(l)):
#     if l[i] == 30: # loop se list ke items ko check karega ki 30 hai ya nahi
#         print(i,l[i]) # agar 30 milta hai to uski index print karega

# l = [10, 2, 30, 4, 50, 50]
# k = ["abc" for i in l if i%2!=0] # list comprehension se ek naya list banata hai jisme list ke items ko string me convert kar ke add karega
# print(k)

l = [1,2,10,20]
print(l[2][0])