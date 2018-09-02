def rearrange(arr):
    length = arr.__len__()
    for i in range(1, length, +2):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if i+1 < length and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

