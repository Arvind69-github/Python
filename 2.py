n = int(input('Enter the number of elements: '))
arr = list(map(int, input('Enter the elements separated by space: ').split()))

if len(arr) != n:
    print("Error: Number of elements entered does not match the specified count.")
else:
    array_sum = sum(arr)
    print("Sum of array elements:", array_sum)
