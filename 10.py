import eulerlib

ans = 0

for i in range(20):
	for j in range(100):
		if(len(str(i**j)) == j):
			print(i**j, i, j)
			ans += 1

print(ans)