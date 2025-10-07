# Python program to find the largest element in an array

# Input: list of numbers
arr = [25, 11, 7, 75, 56]

# Assume first element is the largest
max_element = arr[0]

# Loop through the array to find the largest element
for i in range(1, len(arr)):
    if arr[i] > max_element:
        max_element = arr[i]

print("The largest element in the array is:", max_element)
