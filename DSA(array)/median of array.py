def median(arr):
    n=len(arr)
    arr.sort()
    if n%2==0:
        #even hai matlab
        ind1=n//2-1
        ind2=n//2
        print((arr[ind1]+arr[ind2])/2)
    else:
        print(arr[n//2])
arr=[4,7,1,2,5,6]
print("median")
median(arr)
