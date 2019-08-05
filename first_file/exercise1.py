weight = int(input("Weight: "))
jed = input("(L)bs or (K)g: ")


if jed.upper() == 'K':
    weight *= 2.2
    print(f"You are {weight} pounds")
elif jed.upper() == 'L':
    weight //= 2.2
    print(f"You are {weight} kilos")
else:
    print("Bad format")