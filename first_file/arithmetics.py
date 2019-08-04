import math

print(10/3)
print(10//3)
print(10**3)

x = 2.9
print(round(x))
print(math.ceil(x))

is_night = True

if (math.floor(x) > 1):
    print("x is big")
elif is_night:
    print("night")
else:
    print("day" + "*" * 20)

if is_night and x:
    print("shit")