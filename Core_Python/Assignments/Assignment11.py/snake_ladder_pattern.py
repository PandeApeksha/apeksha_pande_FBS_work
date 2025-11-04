def snake_ladder_pattern(n=100):
    cols = 10  
    rows = n // cols

    for i in range(rows, 0, -1):   
        start = (i - 1) * cols + 1
        end = i * cols

        row_numbers = list(range(start, end + 1))

        if i % 2 == 0:
            row_numbers.reverse()

        for num in row_numbers:
            print(f"{num:3}", end=" ")
        print()

snake_ladder_pattern()
