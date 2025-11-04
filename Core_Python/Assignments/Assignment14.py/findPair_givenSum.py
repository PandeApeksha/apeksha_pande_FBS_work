def find_pairsEle(li1, sum):
    for i in range(0, len(li1)):
        for j in range(i + 1, len(li1)):
            if li1[i] + li1[j] == sum:
                print("pair :", li1[i],",", li1[j])


numbers = [1, 4, 5, 3, 2, 6]
value = int(input("Enter the sum value :"))
find_pairsEle(numbers, value)