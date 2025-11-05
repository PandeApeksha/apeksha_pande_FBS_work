def memoize(func):
    cache = {}  

    def wrapper(*args):
        if args in cache:
            print(f"Fetching from cache for {args}")
            return cache[args]
        print(f"Computing result for {args}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(10):", fibonacci(10))
