first_string = input()

command = input()

while command != "Done":
    split = command.split()
    new_string = ""
    if split[0] == "TakeOdd":
        for i in range(len(first_string)):

            if i % 2 != 0:
              new_string += first_string[i]
        first_string = first_string.replace(first_string,new_string)
        print(first_string)
    elif split[0] == "Cut":
        index , length = split[1:]
        index = int(index)
        length = int(length)
        first_string = first_string[0:index] + first_string[index + length:]
        print(first_string)

    elif split[0] == "Substitute":
        substring, substitute = split[1:]
        if substring in first_string:
            first_string = first_string.replace(substring, substitute)
            print(first_string)
        else:
            print("Nothing to replace!")

    command = input()



print(f"Your password is: {first_string}")




