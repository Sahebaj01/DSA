def primefactors(n):
    prime=[]
    if n%2==0:
        prime.append(2)
        while n%2==0:
            n//=2
    i=3
    while i<=int(n**0.5):
        if n%i==0:
            prime.append(i)
            while n%i==0:
                n//=i
        i+=2
    if n>1:
        prime.append(n)
    print(prime)
n=60
primefactors(n)
# to get repeted factors put the append line inside while codition this code it to get ditinct factors