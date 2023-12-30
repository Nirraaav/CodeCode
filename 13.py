import time

def right_angle_checker(B, C):
    AB = (B[0]**2 + B[1]**2)
    AC = (C[0]**2 + C[1]**2)
    BC = (B[0] - C[0])**2 + (B[1] - C[1])**2
    
    if BC > AB and BC > AC:
        if BC == AB + AC:
            return True
    elif AB > BC and AB > AC:
        if AB == BC + AC:
            return True
    elif AC > AB and AC > BC:
        if AC == AB + BC:
            return True
    return False
    
def compute(limit):
    
    points = [(x, y) for y in range(0,limit+1) for x in range(0,limit+1)]
    points.pop(0)
    
    count = 0
    for B in range(len(points)):
        for C in range(B+1, len(points)):
            if right_angle_checker(points[B], points[C]):
                #print(points[B], points[C])
                count += 1
    return count

if __name__ == "__main__":
    print(compute(58))
