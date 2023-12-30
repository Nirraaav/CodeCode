import eulerlib, math

primes = eulerlib.primes_wheel_fact(84070)
primes.remove(2)
primes.remove(3)

ans = 0

for i in range(len(primes)):
	print(primes[i])
	sum = (math.factorial(primes[i]-1) % primes[i]) + (math.factorial(primes[i]-2) % primes[i]) + (math.factorial(primes[i]-3) % primes[i]) + (math.factorial(primes[i]-4) % primes[i]) + (math.factorial(primes[i]-5) % primes[i])
	ans += (sum % primes[i])

print(ans)