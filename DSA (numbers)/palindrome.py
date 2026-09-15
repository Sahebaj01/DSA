def prime(n):
    num=n
    result=0
    while num>0:
        l_d=num%10
        result=(result*10)+l_d
        num=num//10
    if n==result:
        print("True")
    else:
        print("False")
n=54658
prime(n)