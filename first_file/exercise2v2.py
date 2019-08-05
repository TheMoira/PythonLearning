command = ""
executed = ''
is_chosen = False

while True:

    if not is_chosen:
        command = input("> ").lower()

    if command == "knife":
        if executed == 'k':
            print("The target has already been knifed. Would you like me to hit him with a shovel?")
            if input("(Y)es or (N)o: ").upper() == "Y":
                command = "shovel"
                is_chosen = True
        else:
            print("The target has been butchered with a knife")
            executed = 'k'
            is_chosen = False
    elif command == "shovel":
        if executed == 's':
            print("The target has already been shoveled. Would you like me to knife him?")
            if input("(Y)es or (N)o: ").upper() == "Y":
                command = "knife"
                is_chosen = True
        else:
            print("The target has been hit gracefully with a shovel")
            executed = 's'
            is_chosen = False
    elif command == "help":
        print('''
knife - target will be assasinated with a knife
shovel - target will be assasinated with w shovel
abort - abort mission
        ''')
        is_chosen = False
    elif command == "abort":
        break
    else:
        print("Unregistered tool. Choose another one. Type help to see the choices.")
        is_chosen = False

