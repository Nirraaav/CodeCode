a = 1
b = 2

sum = 2

# for i in range(499999):
while(True):
    temp = a + b
    a = b
    b = temp
    # print(a, b)
    if temp <= 4000000:
        if temp%2 == 0:
            # print(temp)
            sum += temp
    else:
        break

print(sum)