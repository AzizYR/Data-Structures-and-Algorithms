# Majority element

from collections import Counter

n = int(input())
arr = list(map(int,input().split()))
count = Counter(arr)

if max(count.values())>n//2:
    print(1)
else:
    print(0)