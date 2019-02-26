#A dictionary is an unordered, changeable and indexed collection, similiar to map in C++ STL
#like set, dictionary is also using {} instead of ()
#It's a key-value storage architecture

dict_new = {
    "brand" :   "Ford",
    "model" :   "mustang",
    "year"  :   "1964"
}

print(dict_new)

#Accessing item, using key to access value or using the get("key") function
print(dict_new["brand"])
print(dict_new.get("model"))
#Use dict.values() to access the values in the dictionary in a loop
for x in dict_new.values():
    print(x)
#Use items to access both key and value in the dictionary


#Change values also using the key
dict_new["year"] = 2018
print(dict_new["year"])

#Add items. Directly use new key to insert an item
dict_new["color"] = "red"
print(dict_new)

#Remove item. Use pop() with specific key.
dict_new.pop("color")
print(dict_new)
#popitem() remove last inserted item in version 3.7 and after
#del dict["key"] to remove item with specific key,
#the same with other container, using del could directly delete the container






