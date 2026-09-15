def palindrome(m,n):
    result=[]
    for num in range(m,n+1):
        temp=num
        rev=0
        while temp>0:
            l_d=temp%10
            rev=(rev*10)+l_d
            temp=temp//10
        if num ==rev:
            result.append(num)
    print(result)
m=122
n=322
palindrome(m,n)