#use open to open a file
#mode:
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#type:
#"t" - Text - Default. Treat the file as a text file
#"b" - Binary - Treat the file as a binary file

#use read() to read the file, the parameter could be the length you want to read
f = open("README.md", "rt")
print(f.read(5))

#read lines
print(f.readline())

#loop will take care of the file line by line
for x in f:
    print(x)

#"a" will append the content to the end of the file
#"w" will overwrite the whole file
#"x" only create a file without doing anything else

#all command is with open()

#check and delete file is included in a module called "os" (out stream)
import os
#use os.remove("filename") to delete a file
#use os.path.exists("filename") to check existence
#use os.rmdir("directoryname") to remove a directory
