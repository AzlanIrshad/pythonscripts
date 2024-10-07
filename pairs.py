def findNumOfPairs(a, b):
    a.sort()
    b.sort()

    i, j = 0, 0
    count = 0

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            count += 1
            j += 1
        i += 1

    return count
a = [1, 2 ,3, 9, 8]
b = [5, 6, 7]
result = findNumOfPairs(a, b)
print(result)
