

def moveZeros(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    for i in range(j, len(arr)):
        arr[i] = 0
    return arr


arr = [0, 1, 0, 3, 12]
arr = [0, 0, 0]
print(moveZeros(arr))  # [1, 3, 12, 0, 0]
