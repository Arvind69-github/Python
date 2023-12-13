def is_increasing_sequence(lst):
    # Check if the list is empty or has only one element
    if len(lst) <= 1:
        return True

    # Iterate through the list to check if it is in increasing order
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False

    return True

# Example usage
sequence = list(map(int, input("Enter a sequence of numbers separated by space: ").split()))

if is_increasing_sequence(sequence):
    print("The sequence is an increasing sequence.")
else:
    print("The sequence is not an increasing sequence.")
