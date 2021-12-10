






journal = input().split(", ")
command = input().split(" - ")

while command[0] != "Craft!":
    action = command[0]
    item = command[1]
    if action == "Collect":
        if not item in journal:
            journal.append(item)
    elif action == "Drop":
        if item in journal:
            journal.remove(item)
    elif action == "Combine Items":
        item = item.split(":")
        old_one = item[0]
        new_one = item[1]
        for i in range(len(journal)):
            if journal[i] == old_one:
                journal.insert(i + 1, new_one)

    elif action == "Renew":
        if item in journal:
            remeve_item = item
            journal.remove(item)
            journal.append(remeve_item)

    command = input().split(" - ")

print(", ".join(journal))