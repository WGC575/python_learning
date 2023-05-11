#exceptions 
#use "try", "except" and "finally" to complete processing exceptions
#just like other languages
#use build-in exception to customize the errorlog

#use try to test a code block
try:
    print(x)

#use except to handle the error
except:
    print("An exception occured")


#name exceptions to make it unique to other exceptions
try:
    x = 0
except NameError:
    print("The variable is not defined.")
except:
    print("Something other than undefined variable occurs.")
#use "else" to deal with normal execution 
else:
    print("No error occurs.")

#use finally to excute code regardless of the exceptions
finally:
    print("Exception test ends.")

