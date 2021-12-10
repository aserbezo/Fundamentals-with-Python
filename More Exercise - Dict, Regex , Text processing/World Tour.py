first_string = input()

command = input()

while command != "Travel":
    split = command.split(":" )
    if split[0] == "Add Stop":
        index , string = split[1:]
        index = int(index)
        if index < len(first_string):
            first_string = first_string[0:index] + string + first_string[index:]
            print(first_string)
        else:
            print(first_string)
    elif split[0] == "Remove Stop":
        start_index ,end_index = split[1:]
        start_index = int(start_index)
        end_index = int(end_index)
        if start_index < len(first_string) and end_index < len(first_string):
           first_string = first_string[0:start_index] + first_string[end_index + 1:]
           print(first_string)
        else:
            print(first_string)
    elif split[0] == "Switch":
        old_string , new_string = split[1:]
        if old_string in first_string:
            first_string = first_string.replace(old_string,new_string)
            print(first_string)
        else:
            print(first_string)
    command = input()

print(f"Ready for world tour! Planned stops: {first_string}")

