def symmetricpairs(arr):
    mp={}
    for i in range(0,len(arr)):
        first,second=arr[i]
        if second in mp and mp[second]==first:
            print(f"({first} {second})",end=" ")
        else:
            mp[first]=second
arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]  # Example input
symmetricpairs(arr)  # Call function to find symmetric pairs