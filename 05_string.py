
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



