

def maxSum(arr, k):
    if len(arr) < k:
        print("invalid input")
        return -1

    # k: 0, 1 ; arr[i]: 80, -50 ; sum(): 30
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum

    for i in range(len(arr) - k):  # 0, 1, 2, 3, 4
        window_sum = window_sum - arr[i] + arr[i + k]  # 80 + 90 ; -50 + 100
        max_sum = max(max_sum, window_sum)

    return max_sum


k = 2
k = 3
arr = [80, 90, -50, 100]
arr = [80, -50, 90, 100, 10, 20, 30]
arr = [80, 90, -50]
print(maxSum(arr, k))  # 170
