def maxmin(N):
    maxN=0
    minN=9
    while N>0:
        digit=N%10
        if digit>maxN:
            maxN=digit
        if digit<minN:
            minN=digit
        N=N//10
    print(maxN)
    print(minN)
N=7483
maxmin(N)