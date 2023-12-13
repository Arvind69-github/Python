def solve(start, end, arr):
    mid = (start + end) // 2

    if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]):
        return mid

    elif mid == 0 or (mid != len(arr) - 1 and arr[mid] >= arr[mid + 1]):
        return mid

    elif mid == len(arr) - 1 or (mid != 0 and arr[mid - 1] <= arr[mid]):
        return mid

    elif mid != 0 and arr[mid - 1] > arr[mid]:
        return solve(start, mid - 1, arr)
    else:
        if mid + 1 <= len(arr) - 1:
            return solve(mid + 1, end, arr)

    return 0


def main():
    n = int(input('enter length= '))
    arr = list(map(int, input().split()))

    peak_index = solve(0, len(arr) - 1, arr)

    print("arr[]: {" + " ".join(map(str, arr)) + " }")
    print(f"Peak element is: {arr[peak_index]} found at index {peak_index}")


if __name__ == "__main__":
    main()
