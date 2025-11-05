def find_missing_coin(coins):
    missing = 0
    for num in coins:
        missing ^= num  
    return missing

n = int(input("Enter original number of coins: "))
coins = list(map(int, input("Enter numbers on the coins: ").split()))

result = find_missing_coin(coins)
print("The number on the missing coin is:", result)
