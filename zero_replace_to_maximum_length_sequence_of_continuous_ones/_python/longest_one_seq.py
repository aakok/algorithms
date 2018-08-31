def get_zero_index(arr, start, end):
    zero_count = 0
    idx = 0
    for i in range(start, end):
        if arr[i] == 0:
            zero_count += 1
            idx = i
    if zero_count != 1:
        return -1
    else:
        return idx


def longest_one_seq(arr):
    length = 0
    idx = -1
    for i in range(arr.__len__()):
        for j in range(i+1, arr.__len__()+1):
            zero_idx = get_zero_index(arr, i, j)
            if zero_idx < 0:
                continue
            else:
                if j - i > length:
                    idx = zero_idx
                    length = j - i
    return idx
