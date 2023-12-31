import time, math, eulerlib

def fibonnaci(n): #Finds the nth fibonnaci number
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2

def Fibtill(x):
    fibnumbers = []
    n = 1
    while fibonnaci(n) <= x:
        fibnumbers.append(fibonnaci(n))
        n += 1
    return fibnumbers

def fib(x):
    f1 = 1
    f2 = 1
    fibnumbers = [1,1]
    while True:
        fn = f1 + f2
        if fn > x:
            break
        fibnumbers.append(fn)
        f1 = f2
        f2 = fn
    return fibnumbers
    
def compute(limit):
    fib = Fibtill(limit)
    total = 0
    for x in fib:
        if x % 2 == 0:
            total += x
    return total

if __name__ == "__main__":
    # start_time = time.time()
    print(compute(4*10**6))
    # print("--- %s seconds ---" % (time.time() - start_time))