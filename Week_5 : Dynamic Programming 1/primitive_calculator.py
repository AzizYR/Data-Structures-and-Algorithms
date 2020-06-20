#Primitive CaLculator

n = int(input())

min_operations = [None]*(n+1)
min_operations[0] = 0
min_operations[1] = 0
operations = []
arr = [1]
def print_list(min_operations,n):
    res = []
    while n>0:
        res.append(n)
        if n%2 != 0 and n%3 != 0:
            n = n-1
        elif n%3 == 0:
            if min_operations[n-1]<min_operations[n//3]:
                n-=1
            else:
                n = n//3
        elif n%2 == 0:
            if min_operations[n-1]<min_operations[n//2]:
                n-=1
            else:
                n = n//2
    return res   

for i in range(2,n+1):
    if i>=3 and i%3==0:
        min_operations[i] = min(min_operations[i-1]+1,
                            min_operations[i//3]+1    
        )
    elif i%2 == 0:
        min_operations[i] = min(min_operations[i-1]+1,
                            min_operations[i//2]+1    
        )
    else:
        min_operations[i] = min_operations[i-1]+1

res = print_list(min_operations,n)
res.sort()
print(min_operations[n])
print(*res)

