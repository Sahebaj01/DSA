def insertfirst(arr,x):
    arr.insert(0,x)
    return arr
arr=[2,4,6,1]
x=5
arr=insertfirst(arr,x)
print(arr)

def insertlast(arr,x):
    arr.append(x)
    return arr
arr=[3,2,6,4]
x=8
arr=insertlast(arr,x)
print(arr)

def insertposition(arr,pos,x):
    arr.insert(pos,x)
    return arr
arr=[3,1,4,6]
x=4
pos=2
arr=insertposition(arr,pos,x)
print(arr)