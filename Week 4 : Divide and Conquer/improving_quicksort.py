#Improving Quicksort
#3-way partition quicksort

import random

def partition3(a, l, r):
    x, j, k = a[l], l, r
    i = j

    while i<=k:
        if a[i] < x:
            a[i], a[j] = a[j], a[i]
            j += 1
        elif a[i] > x:
            a[i], a[k] = a[k], a[i]
            k -= 1
            i -= 1
        i += 1
    return j,k

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, n + 1, r)



n = int(input())
a = list(map(int, input().split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
