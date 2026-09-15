class Solution:
    def arraySum(self,arr):
        # total=0
        # for num in arr:
        #     total+=num
        # return total
        return sum(arr)


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.arraySum(arr))
