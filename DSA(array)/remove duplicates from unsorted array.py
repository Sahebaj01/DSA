class Solution:
    def remove_duplicates(self,arr):
        seen={}
        result=[]
        for num in arr:
            if num not in seen:
                result.append(num)
                seen[num]=True
        return result
if __name__ == "__main__":
    arr = [4, 5, 4, 2, 2, 3, 1]
    sol = Solution()
    result = sol.remove_duplicates(arr)
    print("Array after removing duplicates:", result)