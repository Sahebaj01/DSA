def secondSmallest(arr,n):
    if n<2:
        return -1
    smallest=float('inf')
    sec_small=float('inf')
    for i in range(n):
        if arr[i]<smallest:
            sec_small=smallest
            smallest=arr[i]
        elif arr[i]<sec_small and arr[i]!=smallest:
                sec_small=arr[i]
    return sec_small
def secondLargest(arr,n):
    if n<2:
          return -1
    largest=float('-inf')
    sec_large=float('-inf')
    for i in range(n):
        if arr[i]>largest:
            sec_large=largest
            largest=arr[i]
        elif arr[i]>sec_large and arr[i]!=largest:
             sec_large=arr[i]
    return sec_large
if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]  # Array of elements
    n = len(arr)  # Size of the array

    # Find the second smallest and second largest elements
    sS = secondSmallest(arr, n)
    sL = secondLargest(arr, n)

    # Output the results
    print(f"Second smallest is {sS}")
    print(f"Second largest is {sL}")
        
        
        
          