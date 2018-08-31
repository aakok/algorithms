import random


def shuffle(arr):
    for i in range(arr.__len__() - 1, 0, -1):
        j = random.randrange(0, i+1)
        arr[j], arr[i] = arr[i], arr[j]
