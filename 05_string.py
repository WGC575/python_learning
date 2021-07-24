
#single quatation is the same as double quatation
x = 'Word  '
y = "word"
print(x)
print(y)

#str[a]
#get specific character in the string with position
print(x[1]) #'o'

#str[a:b]
#get substring with position (left included, right excluded)
print(x[0:2])

#str.strip()
#remove the spaces in the beginning or the end
print(x.strip())

#len(str)
#return the length of the string
print(len(x))

#str.lower(), str.upper()
#return the string in lower case or upper case
print(x.lower())
print(x.upper())

#str.replace()
#replace the string with another string
print(x.replace("W", "C"))

#str.split("separator")
#spilt the string with specific separator if found in the string
print(x.split("o"))

#Single quotation marks will be included in double quotation marks.
print("I'm afraid I won't be able to make it")

#Use \" to include double quotation marks in strings.
print("\"Good!\", he said.")


#formatting
show = "GOT"
name_1 = "Daenerys"
name_2 = "Jon"
name_3 = "Tyrion"
seasons = 8
print(f"The show is called {show} had charaters like {name_1}, {name_2}, and {name_3} in all {seasons} seasons.")