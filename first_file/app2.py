message = '''
Hello there

This way I can easily write in pretty format.

Exciting, ain't it?
'''

print(message)
print("I will " + message[1] + message[-4:-2] + " you")

name = "Winona"
surname = "Ryder"

msg = f'{name} [{surname}] is great'
print(msg)
print(len(msg))
print(msg.upper())
print(msg.find('n'))
print(msg.replace('great','stranger'))
print('yder' in msg)


