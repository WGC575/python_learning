#x, y, z tuples whose sum is n

x = int(input())
y = int(input())
z = int(input())
n = int(input())

ar = [] 
p = 0 

#remember, range() include the left edge but not right
for i in range ( x + 1 ) : 
    for j in range( y + 1): 
        for k in range(z + 1):
            if i + j + k != n:
                #add and then use
                ar.append([]) 
                ar[p] = [ i , j, k ] 
                p+=1 
print(ar) 
