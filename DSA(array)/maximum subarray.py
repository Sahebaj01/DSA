def maximum(arr):
    n=len(arr)
    pre=1
    suf=1
    ans=float("-inf")
    for i in range(n):
        if pre==0:
            pre=1
        if suf==0:
            suf=1
        pre*=arr[i]
        suf*=arr[n-i-1]
        ans=max(ans,pre,suf)
    print(ans)
arr = [2, 3, -2, 4]
maximum(arr)