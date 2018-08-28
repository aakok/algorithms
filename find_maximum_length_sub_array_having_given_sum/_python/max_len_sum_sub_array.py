def max_len_sum_sub_array(arr, _sum):
    start, end = 0, 1
    for i in range(arr.__len__()):
        for j in range(i+1, arr.__len__() + 1):
            if sum(arr[i:j]) == _sum:
                if end - start < j - i:
                    start, end = i, j
    return arr[start:end]


print max_len_sum_sub_array([5, 6, -5, 5, 3, 5, 3, -2, 0], 8)
