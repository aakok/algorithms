def non_constant_space_move_zeros(arr):
    length = arr.__len__()
    non_zero_idx = 0
    zero_idx = length - 1
    res = [None for _ in range(length)]
    for i in arr:
        if i == 0:
            res[zero_idx] = 0
            zero_idx -= 1
        else:
            res[non_zero_idx] = i
            non_zero_idx += 1
    return res


def shift(arr, idx):
    if idx+1 >= arr.__len__():
        return
    if arr[idx+1] == 0:
        shift(arr, idx + 1)
    arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


def move_zeros(arr):
    for i, num in enumerate(arr):
        if num == 0:
            shift(arr, i)


def move_zeros_partition(arr):
    j = 0
    for i in range(arr.__len__()):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
