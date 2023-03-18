import sys

# CLI arguments, an array
args = sys.argv

# print the arguments
print("Number of arguments:", len(args))
print("The arguments are:", str(args))

# traverse arguments
arg_count = 0
for arg in args:
    print("argument #", arg_count, ": ", arg)
    arg_count += 1

# when using "python filename.py" to run the python script, the first (#0) argument is always the file directory. In this case, it could be ".\26_CLI_parameter.py"