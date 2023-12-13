# Input the elements as a list
arr = list(map(int, input('Enter the elements separated by space: ').split()))

# Check if the array is not empty
if arr:
    # Initialize max_element with the first element of the array
    max_element = arr[0]

    # Iterate through the array to find the maximum element
    for element in arr:
        if element > max_element:
            max_element = element

    # Display the result
    print("Maximum element of the array:", max_element)
else:
    print("Error: The array is empty.")
