def is_consecutive(arr, mi, ma):
    if ma - mi + 1 != arr.__len__():
        return False
    visited = dict([(k, False) for k in range(arr.__len__())])
    for num in arr:
        idx = num - mi
        if idx in visited and visited[idx]:
            return False
        visited[idx] = True
    return True


def consecutive_sub_array(arr):
    length = 0
    start, end = 0, 0
    for i in range(arr.__len__()):
        for j in range(i + 1, arr.__len__() + 1):
            max_val, min_val = arr[i], arr[i]
            for k in range(i, j):
                max_val, min_val = max(arr[k], max_val), min(arr[k], min_val)
            if is_consecutive(arr[i:j], min_val, max_val):
                if length < j - i:
                    start, end = i, j
                    length = j - i
    return arr[start:end]


print consecutive_sub_array([2, 0, 2, 1, 4, 3, 1, 0])
