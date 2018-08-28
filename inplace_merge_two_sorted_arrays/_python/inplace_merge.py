def mini(arr1, arr2, pivot, length):
    idx = pivot
    if pivot < arr1.__len__():
        _min = arr1[pivot]
    else:
        _min = arr2[pivot - arr1.__len__()]
    for i in range(pivot+1, length):
        if i < arr1.__len__():
            if arr1[i] < _min:
                _min = arr1[i]
                idx = i
        else:
            index = i - arr1.__len__()
            if arr2[index] < _min:
                _min = arr2[index]
                idx = i
    return _min, idx


# print mini([1, 2, 3, 4, 7], [8, 9, 10], 7, 8)


def inplace_merge(arr1, arr2):
    length = arr1.__len__() + arr2.__len__()
    for i in range(length):
        _min, idx = mini(arr1, arr2, i, length)
        if i < arr1.__len__():
            arr1[i], tmp = _min, arr1[i]
            if idx < arr1.__len__():
                arr1[idx] = tmp
            else:
                arr2[idx - arr1.__len__()] = tmp
        else:
            index = i - arr1.__len__()
            arr2[index], tmp = _min, arr2[index]
            arr2[idx - arr1.__len__()] = tmp
    return arr1, arr2


print inplace_merge([1, 4, 7, 8, 10], [2, 3, 9])
print inplace_merge(
    sorted([1,3,2, 4,6,4,2,12,323,1,3,12]),
    sorted([1,4122,12,412,4213,15,3,54,7,56,86,45,6,25,42,34,4,523,4,234,132,523,45,234,23,42,34,234,23,42])
)
