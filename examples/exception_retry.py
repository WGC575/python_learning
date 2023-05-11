import time

# times of retries
num_retries = 3

# loop for retries
for i in range(num_retries):
    try:
        # code to try
        result = 1 / 0
        print("Result:", result)
    # a specific type of the error/exception is required here
    except ZeroDivisionError:
        # catch exceptions
        print("Error: Division by zero")
        
        # wait before retrying
        time.sleep(1)
    else:
        # no exception, break
        break
else:
    # all failed, exit
    print("Error: Maximum number of retries reached")