def armstrong(num):
    total=0
    n=num
    N=len(str(n))
    while n>0:
        l_d=n%10
        total=total+(l_d**N)
        n=n//10
    return num==total
num=153
print(armstrong(num))