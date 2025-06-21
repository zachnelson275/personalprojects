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

print (f"A(10): {funA(10)}")
print (f"B(10): {funB(10)}")
print (f"C(10): {funC(10)}")
print (f"4(10): {funD(10)}")