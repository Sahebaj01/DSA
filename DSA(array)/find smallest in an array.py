def SmallestElement(arr,n):
    min=arr[0]
    for i in range(1,n):
        if arr[i]<min:
            min=arr[i]
    return min
if __name__ == "__main__":
    # Initialize an array with elements
    arr1 = [2, 5, 1, 3]
    n = len(arr1)  # Size of the array

    # Call the function to find the smallest element and output the result
    min = SmallestElement(arr1, n)
    print(f"The smallest element in the array is: {min}")
#same for largest and max and min in max and min two loops are required