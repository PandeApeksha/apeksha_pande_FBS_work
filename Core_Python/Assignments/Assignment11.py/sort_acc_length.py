def bubbleSort(li):
    for i in range(1, len(li)):
        for j in range(0, len(li) - 1):
            if len(li[j]) > len(li[j + 1]):  
                li[j], li[j + 1] = li[j + 1], li[j]
                   
    return li

words = ["apple", "kiwi", "banana", "cherry", "fig", "grape"]
print("Original list:", words)

sorted_list = bubbleSort(words)
print("Sorted by length:", sorted_list)
