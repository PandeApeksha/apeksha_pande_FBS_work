def ele_Present(li1, Element):
    count = 0
    for ele in li1:
        if (ele == Element):
            count += 1
        
    if (count == 0):
        print(f'{Element} is not present in the list.')
    else:
        print(f'{Element} is present in the list {count} times')    

li1 = [10, 20, 30, 40, 50, 60, 70, 50]
Element = int(input('Enter the element to check :'))
ele_Present(li1, Element)