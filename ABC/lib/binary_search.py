def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val < x:
            low = mid + 1
        elif mid_val > x:
            high = mid - 1
        else:
            return mid  # xが見つかった場合

    return -1  # xが配列内に存在しない場合

# 使用例
arr = [1, 3, 5, 7, 9, 11]
x = 7
print(binary_search(arr, x))  # 出力: 3
