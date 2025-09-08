amount = int(input('Enter the Amount :'))

for note in range(2000, 0, -1):
    if (note == 2000 or note == 500 or note == 200 or note == 100 or note == 50 or note == 20 or note == 10):
        count = 0
        count = amount // note
        if (count > 0):
            print(f'{note} : {count}')
        amount = amount % note
