#This function returns a list of tuples. The i th tuple contains the i th element from each argument sequences or iterables.
#If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the 
#shortest argument sequence
#---https://www.hackerrank.com/challenges/zipped/problem?h_r=next-challenge&h_v=zen
result = zip([1, 2, 3, 4, 5], "iterable")
print(result)
for i in result:
    print(i)        #Only print 5 tuples

array_1 = [1, 2, 3]
array_2 = [4, 5, 6]
array_3 = [7, 8, 9]

array_4 = array_1 + array_2 + array_3
print(*result)
pass
