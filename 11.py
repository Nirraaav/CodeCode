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
    
    result = f(n-2) % (1e9 + 7) + f(n-3) % (1e9 + 7) + f(n-4) % (1e9 + 7) + f(n-1) % (1e9 + 7)
    memo[n] = result % (1e9 + 7)
    return result

print(f(70) % (1e9+7))
