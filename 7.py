import eulerlib

primes = eulerlib.primes(10000)

s = ""

a = 20

list1 = []

for i in range(len(primes)):
	if((primes[i] % 7 == 3 or primes[i] % 3 == 1) and primes[i] > 10):
		print(21-a, primes[i])
		list1.append(primes[i])
		# s += str(primes[i])
		a -= 1
	if(a == 0):
		break

a = 19

list2 = []

for i in range(len(primes)):
	if((primes[i] % 4 == 3 or primes[i] % 3 == 1) and primes[i] > 6):
		print(20-a, primes[i])
		list2.append(primes[i])
		# s += str(primes[i])
		a -= 1
	if(a == 0):
		break

# final_list = list1.merge(list2)
for i in range(len(list1)):
	if(list2.count(list1[i]) != 0):
		s += str(list1[i])
print(s)
ans = int(s)%(10**9+7)
print(ans)