def partition(arr, pivot):
    lt, e, gt = [], [pivot], []
    for i in arr:
        if i < pivot:
            lt.append(i)
        elif i == pivot:
            e.append(i)
        else:
            gt.append(i)
    return lt, e, gt


def quick_sort(arr):
    if arr.__len__() <= 1:
        return arr
    pivot = arr[0]
    lt, e, gt = partition(arr[1:], pivot)
    return quick_sort(lt) + e + quick_sort(gt)

array = [4, 5, 2, 4,5 , 10, 1, 241, 4,3, 14,2 ,12,12 ,412 ,1,24,1, 24,1,24 ,12, 4,12 ,412,5,1 ,4, 2]

import random
array = random.sample(list(range(1000000)), 100000)

print "start"
print quick_sort(array)
