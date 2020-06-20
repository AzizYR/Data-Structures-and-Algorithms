n = int(input())
arr = list(map(int,input().split()))
arr.insert(0,0)
if n < 3:
    print(0)
else:
    W = sum(arr)//3
    cnt = 0 
    if sum(arr) % 3 != 0:
        print(0)
    else:
        #find subset whose sum is subset_val
        sum_subset = [[0 for i in range(n+1)] for j in range(W+1)]
        for i in range(1,W+1):
            for j in range(1,n+1):
                sum_subset[i][j] = sum_subset[i][j-1]
                if arr[j] <= i:
                    sum_subset[i][j] = max(sum_subset[i][j], sum_subset[i-arr[j]][j-1] + arr[j])
                if sum_subset[i][j] == W:
                    cnt += 1

        if cnt < 3:
            print(0)
        else:
            print(1)


