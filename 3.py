original_array = list(map(int,input('Enter the elements separated by space: ').split()))


subsequent_array = [x**2 for x in original_array]

# Display the arrays
print("Original array:", original_array)
print("Subsequent array (squared values):", subsequent_array)
