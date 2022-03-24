import simple_utils as su
def extract(command):
    result = {}
    if command.startswith("t!") != True:
        result.update({"is_command":"false"})
        return result
    result.update({"command":su.isolate(command, "!", " ")})
    flag_indexes = su.find(command, "-")
    flags = []
    for i in flag_indexes:
        if command[i+2] == " ":
            flags.append(command[i+1])
            continue
        break
    result.update({"flaggs":flags})
    return result
    
