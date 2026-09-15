def average(nums):
    total=0.0
    n=len(nums)
    for i in range(n):
        total+=float(nums[i])
    average1=round(total/n,2)
    return average1
nums=[1,2,3,34,23,2]
s=average(nums)
print("average",s)
