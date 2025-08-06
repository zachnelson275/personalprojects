def funA(n):
    if n == 0:
        return 5
    return funA(n-1) + 3*n

def funB(n):
    if n == 0:
        return 1
    return n**3 + funB(n-1)

def funC(n):
    if n==0:
        return 1
    if n==1:
        return 3
    return funC(n-1) * funC(n-2)

def funD(n):
    if n==0:
        return 1
    if n==1:
        return 5
    return funD(n-1) + (funD(n-2)**2)

# print (f"A(10): {funA(10)}")
# print (f"B(10): {funB(10)}")
# print (f"C(10): {funC(10)}")
# print (f"4(10): {funD(10)}")

def euclid(x, y):
    """
    Implements the euclid algorithm to find the GCD
    of x and y in linear combination form. This
    function returns a tuple (gcd, s, t) where
    gcd = s*x + t*y.
    """
    if x == 0:
        return (y, 0, 1)
    (gcd, s, t) = euclid(y % x, x)
    return (gcd, t - (y // x) * s, s)

# print(euclid(19,28560))

# print((4099**9019) % 28907)

from math import factorial

def P(n, r):
    return factorial(n) // factorial(n - r)
def C(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print(P(100, 15))
print()
print(C(1000, 100))

# Function to find the greatest common denominator (GCD) of two numbers
def gcd(a, b):
    """
    Returns the greatest common denominator (GCD) of a and b using the Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(273,80))