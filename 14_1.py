import time, math, eulerlib
start_time = time.time()

def compute():
    limit = 10**4
    primes = eulerlib.primes(limit)[2:]
    print("done")
    total = 0
    for p in primes:
        p4 = p-4
        p3 = p4*(p-3)
        p2 = p3*(p-2)
        p1 = p2*(p-1)
        total += (pow(math.factorial(p-5),1,p) * (p4+p3+p2+p1+1) %p) % p
                  
    return total

def compute1():
    limit = 10**8
    primes = eulerlib.primes(limit)[2:]
    print("done")
    total = 0
    for p in primes:
        p5 = pow((p-2)*(p-3)*(p-4), -1, p)
        p4 = ((p-4)* p5) % p
        p3 = ((p-3)* p4) % p
        p2 = 1
        p1 = p-1
        total += (p1 + p2 + p3 + p4 + p5) % p
                  
    return total

def compute2():
    limit = 84070
    primes = eulerlib.primes(limit)[2:]
    # print("done")
    # print("--- %s seconds ---" % (time.time() - start_time))
    total = 0
    for p in primes:
        #S(p) = (p-5)![(p-1)(p-2)(p-3)(p-4) + (p-2)(p-3)(p-4) + (p-3)(p-4) + (p-4)] mod p
        #     = 9*(p-5)! mod p
        #(p-2)(p-3)(p-4)(p-5)! = 1 mod p
        #(p-5)! = inverse((p-2)(p-3)(p-4), mod p)

        total += (-3*pow(8, -1, p)) % p
                  
    return total

if __name__ == "__main__":
    #print(compute())
    print(compute2())
    print("--- %s seconds" % (time.time() - start_time))