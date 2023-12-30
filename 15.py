import eulerlib, time

start_time = time.time()

divisors = eulerlib.Divisors(1000000)

def check(n, m):
	if(sorted(str(n)) == sorted(str(m))):
		return True
	else:
		return False

mn = 2

for i in range(2, 100000):
	# print(i, int(divisors.phi(i)))
	if(check(i, int(divisors.phi(i)))):
		print(i, int(divisors.phi(i)), i/divisors.phi(i))
		mn = min(mn, i/divisors.phi(i))

print(f"Minimum is {mn}")
print("%s seconds" % (time.time() - start_time))

