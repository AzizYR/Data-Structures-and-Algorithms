#Money Change DP

n = int(input())
coins = [1,3,4]
min_coins = [10**3] * (n+1)
min_coins[0] = 0

for i in range(1,n+1):
    for coin_value in coins:
        if i >= coin_value:
            num_coins = min_coins[i-coin_value] + 1
            if  num_coins < min_coins[i]:
                min_coins[i] = num_coins

print(min_coins[n])    