import time, math, eulerlib, itertools
# start_time = time.time()

#primes = eulerlib.primes(10**7)
   
def is_prime(x): #Test if giving value is a prime 
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True
    
def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: 
                factors.append(n)
            break
    return factors
    
def phi(n): #Eulers Totient Function requires primefactorization and isprime function
    total = n
    prime_factor = prime_factors(n)
    for p in prime_factor:
        total *= (1-1/p)
    return int(total)

def permutations(number): #Returns list containing strings of permutations, can be edited to suit need
    final_list = []
    string = str(number)
    temp_permutations = list(itertools.permutations(string))
    for y in range(len(temp_permutations)):
            temp_var = "".join(str(temp_permutations[y][i]) for i in range(len(temp_permutations[y])))
            final_list.append(int(temp_var))
            
    return final_list

def testingnumbers():
    primes_to_test = list(set(eulerlib.primes(5000)) - set(eulerlib.primes(2000)))
    numbers_to_check = []
    for i in range(len(primes_to_test)):
        for j in range(len(primes_to_test)):
            if primes_to_test[i] * primes_to_test[j] < 10000000:
                numbers_to_check.append(primes_to_test[i] * primes_to_test[j])

    return numbers_to_check
    
def compute():
    minimum = 100
    number_we_are_looking_for = 1
    
    for n in testingnumbers():
            
        if n/phi(n) < minimum:
            if phi(n) in permutations(n):
                minimum = n/phi(n)
                number_we_are_looking_for = n
                
    return number_we_are_looking_for, minimum

def compute1(limit):
    primes = eulerlib.primes(10000)
    minimum = 100000000
    n = 1
    for x in primes:
        for y in primes:
            if x*y < limit:
                if sorted(list(str(x*y))) == sorted(list(str((x-1)*(y-1)))):
                    if (x*y)/((x-1)*(y-1)) < minimum:
                        minimum = (x*y)/((x-1)*(y-1))
                        n = x*y
    return minimum, n
                
if __name__ == "__main__":
    start_time = time.time()
    print(compute1(100000))
    print("%s seconds" % (time.time() - start_time))