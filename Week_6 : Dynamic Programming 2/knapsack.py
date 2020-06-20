W, n = map(int,input().split())
arr = list(map(int,input().split()))
arr.insert(0,0)
max_gold = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(1,n+1):
    for wt in range(1,W+1):
        max_gold[i][wt] = max_gold[i-1][wt]
        if arr[i] <= wt:
            val = max_gold[i-1][wt - arr[i]] + arr[i]
            if val > max_gold[i][wt]:
                max_gold[i][wt] = val

print(max_gold[n][W])
    