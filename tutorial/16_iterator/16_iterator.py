#iterator is an object that contains a countable number of values
#python containers are all iterable
#__iter__() and __next__() are built-in functions for iterators

mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

#string is also iterable
#using for loop through a string
mystring = "string"
for x in mystring:
    print(x)

class Myclass:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Myclass()
myiter = iter(myclass)

for x in myiter:
    if x > 10:
        break
    print(x)