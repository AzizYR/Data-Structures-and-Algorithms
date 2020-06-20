#Edit Distance

a = input()
b = input()
n = len(a)
m = len(b)
a = '0' + a
b = '0' + b
d = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(m+1):
    d[0][i] = i
for i in range(n+1):
    d[i][0] = i

for j in range(1,m+1):
    for i in range(1,n+1):
        insertion = d[i][j-1] + 1
        deletion = d[i-1][j] + 1
        match = d[i-1][j-1]
        mismatch = d[i-1][j-1] + 1
        if a[i] == b[j] :
            d[i][j] = min(insertion,deletion,match)
        else:
            d[i][j] = min(insertion,deletion,mismatch)
# print(d)
print(d[n][m])