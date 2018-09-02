def equilibrium(arr):
    right_total = sum(arr)
    left_total = 0
    res = []
    for i, num in enumerate(arr):
        if left_total == right_total - num:
            res.append(i)
        left_total += num
        right_total -= num
    return res
