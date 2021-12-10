n = int(input())
registered = {}

for i in range(n):
    command = input().split()
    type_command = command[0]
    if type_command == "register":
        username = command[1]
        plate_number = command[2]
        if username not in registered:
            registered[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    else:
        if type_command == "unregister":
            username = command[1]
            if username not in registered:
                print(f"ERROR: user {username} not found")
            else:
                registered.pop(username)
                print(f"{username} unregistered successfully")


for key, value in registered.items():
    print(f"{key} => {value}")