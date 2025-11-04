def sort_second_element(data):
    n = len(data)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] [1] < data[min_index][1]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]
    return data

data = [[1, 5], [2, 3], [4, 1]]
res = sort_second_element(data)
print(res)
