#python itself is object-oriented
#using class is similiar to other languages.
class Person:
    #property:
    x = 5

    #Constructor (pre-built-in function)
    #the first parameter in __init__() is a special parameter as a reference to the instace itself, like "this" in C++
    #it may not be named self but anyway it is the first parameter
    def __init__(self, name, age):
        self.name   =   name
        self.age    =   age
    #method
    def myfun(self):
        print("My name is " + self.name)

#create a instance
p1 = Person("John", 36)
p1.myfun()

#modification can be made to properties using assignment
p1.age = 12
#deletion of properties or object itself could be completed by "del"

