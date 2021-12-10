

encrypted_message = input()

command = input()

while command != "Decode":
    instructions = command.split("|")
    if instructions[0] == "Move":
        numbers_letters = int(instructions[1])
        encrypted_message = encrypted_message[numbers_letters:] + encrypted_message[0:numbers_letters]
    elif instructions[0] == "Insert":
        index , value = instructions[1:]
        index = int(index)
        encrypted_message = encrypted_message[0:index] + value + encrypted_message[index:]
    elif instructions[0] == "ChangeAll":
        substring, replacement = instructions[1:]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {encrypted_message}")
