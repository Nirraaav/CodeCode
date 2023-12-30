import eulerlib

memo = {}

def f(n):
    if n in memo:
        return memo[n]
    
    if n < 2:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 8
    
    result = f(n-2) % (10**9 + 7) + f(n-3) % (10**9 + 7) + f(n-4) % (10**9 + 7) + f(n-1) % (10**9 + 7)
    memo[n] = result % (10**9 + 7)
    return result

print(f(70) % (10**9+7))
