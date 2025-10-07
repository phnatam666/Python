def serach_rotated_sorted_array(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
            
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                

    return -1



arr = [ 9, 12, 15, 17, 8, 8, 19, 1, 3, 5, 7 ,0]
target = 8
print(serach_rotated_sorted_array(arr, target))  # Output: 3