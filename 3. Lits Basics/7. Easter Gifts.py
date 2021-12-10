receive_gift_names = input().split()
command= input()

final_list = []

while command != "No Money":
    command = command.split()
    new_command = command[0]
    if new_command == "OutOfStock":
        for i in range(len(receive_gift_names)):
            if  command[1] in receive_gift_names[i]:
                receive_gift_names[i] = "None"
    elif new_command == "Required":
        for i in range(len(receive_gift_names)):
            if i == int(command[2]):
                receive_gift_names[i] = command[1]
    elif new_command == "JustInCase":
        for i in range(len(receive_gift_names)):
            receive_gift_names[-1] = command[1]
    command = input()


for i in receive_gift_names:
   if "None" in receive_gift_names:
       receive_gift_names.remove("None")

print(" ".join(receive_gift_names))




