#while is basically used when there is a condition
i = 0
while i < 10:
    print(i)
    i+=1

#for is used when it concerns containers or ranges
for x in range(6):
    if x == 1:
        continue
    elif x == 3:
        break
    print(x)