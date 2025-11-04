def findMaxProductPairs(numbers):

    max_prod = numbers[0] * numbers[1]
    pair = (numbers[0], numbers[1])
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            prod = numbers[i] * numbers[j]
            if prod > max_prod:
                max_prod = prod
                pair = (numbers[i], numbers[j])
    
    return pair, max_prod

nums = [2, 3, 5, 7, 1, 9]
pair, product = findMaxProductPairs(nums)
print(f"Pair with maximum product: {pair}")
print(f"Maximum product: {product}")
