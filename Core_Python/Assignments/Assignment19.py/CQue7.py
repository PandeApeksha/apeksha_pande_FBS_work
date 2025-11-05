numbers = [n for n in range(1, 1001) if any(n % d == 0 for d in range(2, 10))]

print(numbers)
