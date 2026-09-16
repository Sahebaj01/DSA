def power(x,n):
    ans=1
    if n<0:
        x=1/x
        n=-(n+1)
        ans=ans*x
    while n>0:
        if n%2==1:
            ans=ans*x
            n=n-1
        else:
            n=n//2
            x=x*x
    print(ans)
power(x=2,n=21)
