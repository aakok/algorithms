def duplicate(arr):
    d = dict()
    for i in arr:
        if i in d:
            return i
        d[i] = None
    return -1

