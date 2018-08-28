def duplicate(arr):
    d = dict()
    for i in arr:
        if i in d:
            return i
        d[i] = None
    return -1


print duplicate([1, 2, 3, 4, 4])
print duplicate([1, 2, 3, 4, 2])
