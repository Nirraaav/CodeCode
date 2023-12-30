import eulerlib

ans = 0

for i in range(12, 985):
	s = str(i)
	odd = 0
	even = 0
	for j in range(len(s)):
		if(int(s[j])%2 == 1):
			odd += 1
		else:
			even += 1
	# print(i, odd, even)
	if(odd%2 == 0 and even%2 == 1):
		ans += 1
		print(i, odd, even)

print(ans)
