class Solution:
    def frequency(self,arr,n):
        freq_map=dict()
        for i in range(n):
            if arr[i] in freq_map:
                freq_map[arr[i]]+=1
            else:
                freq_map[arr[i]]=1
        for key, value in freq_map.items():
            print(key, value)
if __name__ == "__main__":
    # Input array
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)

    # Create Solution instance
    sol = Solution()

    # Call the function to count frequencies
    sol.frequency(arr, n)