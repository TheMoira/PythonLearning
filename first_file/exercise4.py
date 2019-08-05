coordinates = (1,2,3)
x,y,z = coordinates
print(y)
print("*" * 20)

numbers = {
    '1' : "one",
    '2' : "two",
    '3' : "three",
    '4' : "four",
    '5' : "five",
    '6' : "sixx",
    '7' : "seven",
    '8' : "eight",
    '9' : "nine",
    '0' : "zero",
}

phone = input("Phone number: ")
output = ""

for digit in phone:
    output += numbers.get(digit, "default") + " "

print(output)

words = output.split(' ')

for word in words:
    print("**" + word)