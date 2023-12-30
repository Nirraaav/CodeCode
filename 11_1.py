import time, math, eulerlib, itertools
start_time = time.time()

def compute(y):
    a1 = 1
    a2 = 2
    a3 = 4
    a4 = 8
    
    for x in range(0,y-4):
        an = a1 + a2 + a3 + a4
        a1 = a2
        a2 = a3
        a3 = a4
        a4 = an
    
    return an

if __name__ == "__main__":
    print(compute(70) % (10**9 + 7))
    print("--- %s seconds ---" % (time.time() - start_time))