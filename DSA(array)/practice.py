# # # # # def average(nums):
# # # # #     n=len(nums)
# # # # #     total=0.0
# # # # #     for i in range(n):
# # # # #         total+=float(nums[i])
# # # # #         avg=round(total/n,2)
# # # # #     return avg
# # # # # nums=[1,2,3]
# # # # # print(average(nums))
# # # # def median(nums):
# # # #     nums.sort()
# # # #     n=len(nums)
# # # #     if n%2==0:
# # # #         ind1=(n//2)-1
# # # #         ind2=n//2
# # # #         print((nums[ind1]+nums[ind2])/2)
# # # #     else:
# # # #         print(n//2)
# # # # nums=[1,2,3,4,5]
# # # # # median(nums)
# # # def sort1(nums):
# # #     if not nums:
# # #         return 0
# # #     n=len(nums)
# # #     i=0
# # #     for j in range(1,n):
# # #         if nums[j]!=nums[i]:
# # #             i+=1
# # #             nums[j],nums[i]=nums[i],nums[j]
# # #     print(i+1)
# # # nums=[1,3,3,4]
# # # sort1(nums)       
# # def sort1(nums):
# #     seen={}
# #     result=[]
# #     for num in  nums:
# #         if num not in seen:
# #             result.append(num)
# #             seen[num]=True
# #     print(result)
# # nums=[2,1,3,2,1,5]
# # sort1(nums)
# def symmetric(arr):
#     mp={}
#     for i in range(0,len(arr)):
#         first,second=arr[i]
#         if second in mp and mp[second]==first:
#             print(f"({first} {second})",end="")
#         else:
#             mp[first]=second
# arr = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
# symmetric(arr)   
def subarray(arr):
    n=len(arr)
    pre=1
    suf=1
    ans=float("-inf")
    for i in range(n):
        if pre==0:
            pre==1
        if suf==0:
            suf==1
        pre*=arr[i]
        suf=arr[n-i-1]
        ans=max(ans,pre,suf)
    print(ans)
arr = [2, 3, -2, 4]
subarray(arr)