def find_combinations(arr, n):
    combs = []
    if n == 1:
        return map(lambda x: [x], arr)
    for i, num in enumerate(arr):
        for comb in find_combinations(arr[i+1:], n-1):
            combs.append([num] + comb)
    return combs


def max_product(arr):
    max_product = 0
    res = []
    for comb in find_combinations(arr, 2):
        product = comb[0] * comb[1]
        if product > max_product:
            res = [comb]
            max_product = product
        elif product == max_product:
            res.append(comb)
    return res
