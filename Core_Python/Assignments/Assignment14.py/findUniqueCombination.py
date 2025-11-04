def three_No_combination(numbers, target):
    result = []

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    combination = [numbers[i], numbers[j], numbers[k]]
                    combination.sort()
                    if combination not in result:
                        result.append(combination)

    return result

nums = [1, 2, 3, 4, 5, 6]
target_sum = 10

combinations = three_No_combination(nums, target_sum)
print('unique combinations of 3 numbers adding up to', target_sum, ":")
print(combinations)