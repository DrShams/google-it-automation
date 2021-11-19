def first_and_last(message):
    if len(message)> 0: 
        if message[0] == message[-1]:
            return True
        else:
            return False
    else:
        return True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
