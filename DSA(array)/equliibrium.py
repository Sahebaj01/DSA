def findEquilibriumIdx(nums):
    n=len(nums)
    total_sum=sum(nums)
    right=total_sum
    left=0
    for i in range(n):
        right -=nums[i]
        if left==right:
            print(i)
        left+=nums[i]
    return -1
arr = [2, 3, -1, 8, 4]
findEquilibriumIdx(arr)