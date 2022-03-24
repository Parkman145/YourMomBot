def extract_commands(command, raise_error = 0):
    start = command.find ("-")
    if start == -1:
        if raise_error == 1:
            raise Exeption("No commands found.")
        else:
            return
    end = command.find (" ", start)
    commands = []
    for i in range(start+1, end-1):
        commands.append(command[i])
    return(commands)