def min_notes(amount):
 
    D = [2000, 500, 200, 100, 50, 20, 10, 5]
    count = 0
    for note in D:
        num = amount // note           
        count += num
        amount = amount % note         
    if amount != 0:
        print("Remaining amount that cannot be represented:", amount)
    return count


amt = int(input("Enter the amount: "))
notes_needed = min_notes(amt)
print("Minimum number of notes needed:", notes_needed)
