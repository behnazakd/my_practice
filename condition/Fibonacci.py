number=int(input("enter number plz:\n"))
previous_number=1
current_number=1
numbers=2
print(previous_number)
print(current_number)
while numbers != number:
    next_number = (previous_number) + (current_number)
    previous_number = current_number
    current_number = next_number
    print(next_number)
    numbers += 1