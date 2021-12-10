phonebook = {}
number_check = " "


while True:
    command = input().split("-")
    name = command[0]
    if name.isnumeric():
        number_check = name
        break

    number = str(command[1])

    if name not in phonebook:
      phonebook[name] = number


num = int(number_check)

for i in range(num):
    name_check = input()
    if name_check in phonebook.keys():
        print(f"{name_check} -> {phonebook[name_check]}")
    else:
       print(f"Contact {name_check} does not exist.")