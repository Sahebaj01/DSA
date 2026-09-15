class Solution:
    def rearrangeArray(self,arr,n):
        arr.sort()
        
        arr[n//2:]=reversed(arr[n//2:])
# Driver code
if __name__ == "__main__":
    arr = [5, 2, 9, 1, 6, 3]
    n=len(arr)
    sol = Solution()
    sol.rearrangeArray(arr,n)
    print(arr)

