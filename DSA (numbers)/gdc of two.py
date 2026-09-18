# There is two ways to solve the gcd of Two numbers either by built in function or by Euclidean Algorithm
#By built-in function
import math 
def gcd1(a,b):
    return math.gcd(a,b)
a=52
b=2
print(gcd1(a,b))

#By euclidean Algorithm
def euclidean(a,b):
    while a>0 and b>0:
        if a>b:
            a%=b
        else:
            b%=a
        if a==0:
            return b
    return a
a=52
b=2
print(euclidean(a,b))