# freq in desecending and numner in ascending
def sortByFrequency(arr):
    freq={}
    for num in arr:
        if num  not in freq:
            freq[num]=1
        else:
            freq[num]+=1
    arr.sort(key=lambda x:(freq[x],x))
    print(arr)
arr = [1, 2, 3, 2, 4, 3, 1, 2]
sortByFrequency(arr)
# same if we want sort freq in ascending and number in desencding then 
def sortByFrequency(arr):
    freq={}
    for num in arr:
        if num  in freq:
            freq[num]+=1
        else:
            freq[num]=1
    arr.sort(key=lambda x:(freq[x],-x))
    print(arr)
arr = [1, 2, 3, 2, 4, 3, 1, 2]
sortByFrequency(arr)