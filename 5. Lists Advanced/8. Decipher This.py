def decripting_digits(message):
    partial_decript = []
    for i in secrets_message:
        final = []
        current = i
        for digit in current:
            if digit.isdigit() == True:
                final.append(digit)
        chracter_string = ("".join(final))
        character_int = int(chracter_string)
        message = chr(character_int)
        replace = current.replace(chracter_string, message)
        partial_decript.append(replace)
    return partial_decript

def dectipting_index(message):
    result = []
    for i in message:
        if len(i) <= 2:
            current = i
            result.append(current)
        else:
            second = i[1]
            last = i[-1]
            current = i[0:1] + last + i[2:-1] + second
            result.append(current)
    return result

secrets_message = input().split()
result = decripting_digits(secrets_message)
decrepted_message = dectipting_index(result)
print(" ".join(decrepted_message))