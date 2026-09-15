def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
def leftrotate(nums,k):
    n=len(nums)
    k=k%n
    if k==0:
        return
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    reverse(nums,0,n-1)
def rightrotate(nums,k):
    n=len(nums)
    k=k%n
    if k==0:
        return
    reverse(nums,n-k,n-1)
    reverse(nums,0,n-k-1)
    reverse(nums,0,n-1)
#example
nums=[1,2,3,4,5]
leftrotate(nums,2)
print("left:",nums)
rightrotate(nums,3)
print("right:",nums)
#for left remember 0 se leke k then k se leke ending then whole reverse
#for right k se leke ending then 0 se leke k then whole reverse
# and also if there is (0,4) that means it has 4 inclusive in slicing it is exclusive 