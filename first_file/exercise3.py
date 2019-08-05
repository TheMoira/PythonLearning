numbers = [5,2,5,2,2]

for quantity in numbers:
    print("x" * quantity)

print(numbers)

for item in numbers:
    for index in range(numbers.__len__()):
        if item == numbers[index]:
            numbers.remove(index)

print(numbers)
?????????