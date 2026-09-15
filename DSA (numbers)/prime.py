def prime(n):
    cnt=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            cnt+=1
            if n//i!=i:
                cnt+=1
    if cnt==2:
        print("no.is prime")
    else:
        print("no. is not prime")
n=17
prime(n)
