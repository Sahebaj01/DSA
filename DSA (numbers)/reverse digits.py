def reverse(num):
    rev=0
    while num>0:
        l_d=num%10
        rev=(rev*10)+l_d
        num=num//10
    print(rev)
num=123
reverse(num)