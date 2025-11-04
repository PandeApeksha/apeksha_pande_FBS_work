def generate_dict(n):
    d = {}
    x = 1
    while (x <= n):
        d[x] = x * x
        x = x + 1
    
    return d

n = int(input("Enter the value of n :"))
res = generate_dict(n)
print(f'generated dictionary :{res}')
