#List is a collection of ordered and unchangeable, duplicates allowed

list_a = ["Apple", "Banana", "Cherry"]
print(list_a[0])

#List should always be declared before using
list_ini = []

#In python, writing a loop is not like other language, which should be taken good care of
for x in list_a:
    print(x)

#Use * could output the content, similar to that of C++
print(*list_a)

#Access member with index
print(list_a[1])

#Searching for specific member
if "Apple" in list_a:
    print("Apple is in list_a")

#Length of the array
print(len(list_a))

#Add items, use append to add in the end of the list while using insert to add with specific index
list_a.append("Orange")
list_a.insert(3, "Pear")
print(list_a)

#Lists could be simply added together， even if the types are different
array_1 = ['1', '2', '3']
array_2 = [4, 5, 6]
array_3 = array_1 + array_2
print(array_3)

#Remove items
list_a.remove("Pear")   #use remove to delete with specific content
list_a.pop()            #use pop to delete with index or the end of the list
#use del(list[0]) to delete with specific index or delete the whole list
#use list.clear() to empty the list

#Constructor, list()
list_new = list(("apple", "banana", "cherry"))
print(list_new)

#Method list:
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	    Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	    Removes the element at the specified position
#remove()	Removes the item with the specified value
#reverse()	Reverses the order of the list
#sort()	    Sorts the list 





