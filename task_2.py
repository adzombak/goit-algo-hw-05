def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations_count = 0

    while low <= high:
        iterations_count += 1
        mid = (high + low) // 2

        if target == arr[mid]:
            return iterations_count, arr[mid]
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    upper_bound = arr[low] if low < len(arr) else None
    return iterations_count, upper_bound


arr = [0.1, 0.5, 0.7, 1.2, 1.5, 2.0, 2.5, 3.0]
target_value = 1.1
result = binary_search(arr, target_value)

print(f"Iterations count:", result[0])
print(f"Upper bound:", result[1])
