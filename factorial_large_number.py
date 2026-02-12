def factorial_digits(n):
    import math
    return list(map(int, str(math.factorial(n))))
