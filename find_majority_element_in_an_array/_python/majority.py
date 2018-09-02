def majority(arr):
    h = {}
    max_count = 0
    num = None
    for i in arr:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1
        if h[i] > max_count:
            num = i
            max_count = h[i]
    if max_count > arr.__len__() // 2:
        return num
    return None
