#binary search

n = list(map(int,input().split()))
length = n[0]
n.pop(0)
k = list(map(int,input().split()))

def binarySearch(key,low,high):
    if low>high:
        return -1
    else:
        mid = (low+high)//2
        if key == n[mid]:
            return mid
        elif key < n[mid] :
            return binarySearch(key,low,mid-1)
        else:
            return binarySearch(key,mid+1,high)

ans = []
for i in range(1,k[0]+1):
    ans.append(binarySearch(k[i],0,len(n)-1))
print(*ans)