list_character = input().split(", ")
values = []
character_dict = {}
for value in list_character:
    values.append(ord(value))

print(dict(zip(list_character,values)))
