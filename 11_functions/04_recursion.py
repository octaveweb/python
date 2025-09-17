"""
# Fibonachi Sequence
# 0 1 1 2 3 5 8 13 
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1) => 1
fib(3) = fib(1) + fib(2) => 2
fib(4) = fib(2) + fib(3) => 3 
fib(5) = fib(3) + fib(4) => 5
fib(6) = fib(4) + fib(5) => 8
fib(7) = fib(5) + fib(6) => 5
fib(8) = fib(6) + fib(7) => 8

fib(n) = fib(n-2) + fib(n-1) # formula
"""

def fib(n):
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)


a = int(input("Enter range: "))
if(a > 25):
    print("Warnning!\nTry (1 - 25) ")
else:
   for i in range(1,a+1):
     print(f"fib({i}) = ", fib(i))

"""
def fib(n):
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)


fib(6)
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
0 + 1 + fib(3) + fib(5)
0 + 1 + 1 + fib(2) + fib(5)
0 + 1 + 1 + 0  + 1 + fib(5)
0 + 1 + 1 + 0  + 1 + fib(5)
0 + 1 + 1 + 0  + 1 + fib(3) + fib(4)
0 + 1 + 1 + 0  + 1 + 1 + fib(2) + fib(4)
0 + 1 + 1 + 0  + 1 + 1 + 0 + fib(1) + fib(4)
0 + 1 + 1 + 0  + 1 + 1 + 0 + 1 + fib(4)
0 + 1 + 1 + 0  + 1 + 1 + 0 + 1 + 0 + fib(3)
0 + 1 + 1 + 0  + 1 + 1 + 0 + 1 + 1 + fib(3)
0 + 1 + 1 + 0  + 1 + 1 + 0 + 1 + 1  + 1 + fib(2)
0 + 1 + 1 + 0  + 1 + 1 + 0 + 1 + 1  + 1 + 0 + 1

0 + 1 + 1 + 0  + 1 + 1 + 0 + 1 + 1  + 1 + 0 + 1 = 8 = fib(6)
"""
