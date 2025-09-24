

def fact():
    num = int(input("Enter Number :"))
    f = 1
    for i in range(1, num + 1):
        f = f * i
    return f
res = fact()
print("Factorial is", res)    