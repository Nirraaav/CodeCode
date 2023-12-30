import eulerlib

sum = 0

for i in range(1, 1001):
	if(i%2 != 0 and i%7 != 0):
		sum += i

print(sum)