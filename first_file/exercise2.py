command = input("> ")

while command.lower() != "abort":
    if command.lower() == "knife":
        print("The target has been butchered with a knife")
    elif command.lower() == "shovel":
        print("The target has been hit gracefully with a shovel")
    elif command.lower() == "help":
        print('''
        knife - target will be assasinated with a knife
        shovel - target will be assasinated with w shovel
        abort - abort mission
        ''')
    else:
        print("Unregistered tool. Choose another one. Type help to see the choices.")

    command = input("> ")
