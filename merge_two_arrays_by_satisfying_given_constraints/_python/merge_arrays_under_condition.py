"""
haha implementation
"""
# print (lambda arr1, arr2: sorted(filter(lambda x: x, arr1) + arr2))([0, 2, 0, 3, 0, 5, 6, 0, 0], [1, 8, 9, 10, 15])


"""
May be implementation
"""


array1 = [2, 3, 5, 6, 9, 0, 0, 0, 0]
array2 = [1, 8, 10, 15]


def _shift(arr, idx, direction):
    if arr[idx+direction]:
        _shift(arr, idx + direction, direction)
    arr[idx+direction], arr[idx] = arr[idx], 0


def _shift_left(arr, idx):
    _shift(arr, idx, -1)


def _shift_right(arr, idx):
    _shift(arr, idx, +1)


def _is_left_shiftable(arr, idx):
    for i in range(idx):
        if not arr[i]:
            return True
    return False


def _is_right_shiftable(arr, idx):
    for i in range(idx, arr.__len__()):
        if not arr[i]:
            return True
    return False


def _merge(arr1, arr2, j):
    if j >= arr2.__len__():
        return
    num2 = arr2[j]
    for i, num1 in enumerate(arr1):
        if num1:
            if num1 >= num2:
                if _is_left_shiftable(arr1, i):
                    if arr1[i-1]:
                        _shift_left(arr1, i - 1)
                    arr1[i-1] = num2
                else:
                    _shift_right(arr1, i)
                    arr1[i] = num2
                _merge(arr1, arr2, j + 1)
                return
    last = arr1.__len__() - 1
    if arr1[last]:
        _shift_left(arr1, last)
    arr1[last] = num2
    _merge(arr1, arr2, j + 1)


def merge(arr1, arr2):
    return _merge(arr1, arr2, 0)


merge(array1, array2)
print array1