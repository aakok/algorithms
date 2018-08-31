import copy


def find_perms(arr, n):
    if n <= 0:
        return [[]]
    else:
        res = []
        for i, item in enumerate(arr):
            cp = copy.copy(arr)
            del cp[i]
            res += [[item] + sml for sml in find_perms(cp, n-1)]
        return res


def find_combs(arr, n):
    if n <= 0:
        return [[]]
    else:
        res = []
        for i, item in enumerate(arr):
            res += [[item] + sml for sml in find_combs(arr[i+1:], n-1)]
        return res


def sum_zero(arr):
    """
    :param arr:
    :return:

    this function finds the sum zeros in all possible combinations.
    """
    res = []
    for i in range(1, arr.__len__()):
        for comb in find_combs(arr, i):
            if sum(comb) == 0:
                res.append(comb)
    return res


def sum_zero_sub_arr(arr):
    """
    :param arr:
    :return:

    this function finds the sum zero sub_arrays. not combinations.
    """
    res = []
    for i in range(arr.__len__()):
        for j in range(i+1, arr.__len__() + 1):
            if sum(arr[i:j]) == 0:
                res.append((i, j))
    return res

