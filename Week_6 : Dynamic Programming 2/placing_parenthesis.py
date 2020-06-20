import sys
def calc(a,b,op):
    if op == "+":
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        return 'wrong op'

def find_min_max(i,j):
    minimum = sys.maxsize
    maximum = -sys.maxsize
    for k in range(i,j):
        a = calc(max_table[i][k],max_table[k+1][j],operators[k])
        b = calc(max_table[i][k],min_table[k+1][j],operators[k])
        c = calc(min_table[i][k],max_table[k+1][j],operators[k])
        d = calc(min_table[i][k],min_table[k+1][j],operators[k])
        minimum = min(minimum,a,b,c,d)
        maximum = max(maximum,a,b,c,d)
    return minimum, maximum

def parenthesis(expression):
    for i in range(len(digits)):
        min_table[i][i] = digits[i]
        max_table[i][i] = digits[i]
    
    for s in range(len(digits)):
        for i in range(len(digits) - s - 1):
            j = i + s + 1
            minVal, maxVal = find_min_max(i,j)
            min_table[i][j] = minVal
            max_table[i][j] = maxVal

    return max_table[0][len(digits) - 1]


expression = input()
digits = list(map(int,expression[::2]))
operators = list(expression[1::2])
min_table = [[0 for i in range(len(digits)) ] for j in range(len(digits)) ]
max_table = [[0 for i in range(len(digits)) ] for j in range(len(digits)) ]
print(parenthesis(expression))