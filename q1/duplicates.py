# Time Complexity => O(n)
# Space Complexity => O(n)
def getDuplicates(arr):
    dups = {}
    res = []
    for a in arr:
        if a not in dups:
            dups[a] = 1
        else:
            dups[a] += 1
    for k in dups.keys():
        if dups[k] > 1:
            res.append(k)
    return res


print(getDuplicates([1, 2, 2, 55, 3, 3, 4, 4, 4]))
