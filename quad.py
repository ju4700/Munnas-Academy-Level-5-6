def quadratic(a, b, c):
    d = b**2 - 4*a*c
    r = d**(1/2)

    f1 = (-b + r)/(2*a)
    f2 = (-b - r)/(2*a)

    print(f'X1 = {f1:.3f}')
    print(f'X2 = {f2:.4f}')

def multiplication(a, b, c):
    return a*b*c

def summation(a, b, c):
    return a+b+c

