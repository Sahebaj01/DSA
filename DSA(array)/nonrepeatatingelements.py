def repeatelements(arr):
    freq={}
    for element in arr:
        if element in freq:
            freq[element]+=1
        else:
            freq[element]=1
    print("the non-repeating elements are:",end=" ")
    for element,count in freq.items():
        if count==1:
            print(element,end=" ")
arr=[1, 1, 2, 3, 4, 4, 5, 2]
repeatelements(arr)