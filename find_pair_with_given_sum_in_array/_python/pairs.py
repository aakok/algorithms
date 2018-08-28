import pickle


def find_pairs_naive(arr, _sum):
    res = 0
    for i in range(arr.__len__()):
        for j in range(i+1, arr.__len__()):
            if _sum - arr[i] == arr[j]:
                res += 1
    return res


def find_pairs_hash(arr, _sum):
    table = {}
    res = 0
    for v in arr:
        if _sum-v in table:
            res += 1
        table[v] = 0
    return res


array = []
with open("array.pickle") as f:
    array = pickle.load(f)

total = 1000

print(find_pairs_hash(array, total))
