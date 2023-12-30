import time
start_time = time.time()

def sum_digits(x):
    totalsum = 0
    while x != 0:
        totalsum += (x % 10)**2
        x = x // 10
    return totalsum

def square_digit_terminal_finder(x):
    while True:
        x = sum_digits(x)
        if x == 89:
            return 89
        if x == 1:
            return 1

def compute(limit):
    count = 0
    values = [0] + [square_digit_terminal_finder(x) for x in range(1,len(str(limit)) * 9**2)]     
    for y in range(1,limit + 1):
        temp_var = values[sum_digits(y)]
        if temp_var == 89:
            count += 1    
    return count

if __name__ == "__main__":
    print(compute(84070))
    print("--- %s seconds ---" % (time.time() - start_time))