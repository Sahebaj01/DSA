def repeatelements(arr):
    hash_map={}
    for num in arr:
        if num in hash_map:
            hash_map[num]+=1
        else:
            hash_map[num]=1
    
    print("repeatating elements are=",end=" ")
    for key,value in hash_map.items():
        if value>1:
            print(key,end=" ")
            
arr=[1,1,2,3]
repeatelements(arr)
#assessment
def repeatelements(arr):
    hash_map={}
    for num in arr:
        if num in hash_map:
            hash_map[num]+=1
        else:
            hash_map[num]=1
    found=False
    print("repeatating elements are=",end=" ")
    for key,value in hash_map.items():
        if value>1:
            print(key,end=" ")
            found=True
    if not found:
        print("NONE")
arr=[1,2,3]
repeatelements(arr)