# Input the elements as a list
arr = list(map(int, input('Enter the elements separated by space: ').split()))

# Input the element to find
element_to_find = int(input('Enter the element to find: '))

# Initialize a flag to check if the element is found
found = False

# Iterate through the array to find the element
for i in range(len(arr)):
    if arr[i] == element_to_find:
        found = True
        print(f"Element {element_to_find} found at index {i}")
        break  # Exit the loop once the element is found

# If the element is not found, print a message
if not found:
    print(f"Element {element_to_find} not found in the array.")

