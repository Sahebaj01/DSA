def sortarray(arr1,arr2):
    order={}
    for i in range(len(arr2)):
        order[arr2[i]]=i
    arr1.sort(key=lambda x:(order.get(x,len(arr2)),x))
    return arr1
arr1=[2,1,2,5,7,1,9,3,3,8,8]
arr2=[2,1,8,3]
print(sortarray(arr1,arr2))    