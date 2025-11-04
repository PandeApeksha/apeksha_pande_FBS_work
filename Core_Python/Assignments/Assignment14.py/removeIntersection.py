def remove_Intersection(set1, set2):
    new_set = set()
    for x in set1:
        for y in set2:
            if x == y:
                break
        else:
            new_set.add(x)
   
    return new_set

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6} 
res = remove_Intersection(set1, set2)
print(f'after removing the intersection of a set2 with set1 is :{res}')