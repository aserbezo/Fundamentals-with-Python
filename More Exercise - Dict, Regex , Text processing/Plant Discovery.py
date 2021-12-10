
n = int(input())

plant_dict = {}

for _ in range(n):
    info_plants = input().split("<->")
    plant = info_plants[0]
    rarity = int(info_plants[1])
    if plant not in plant_dict:
        plant_dict[plant] = {"rarity": rarity, "rating": []}
    else:
         plant_dict[plant]["rarity"] += rarity


commands = input()

while commands != "Exhibition":
    command, command_params = commands.split(": ")
    if command == "Rate":
        plant_name, rating = command_params.split(" - ")
        rating = int(rating)
        if plant_name not in plant_dict:
            print("error")
        else:
            plant_dict[plant_name]["rating"].append(rating)
    elif command == "Update":
        plant_name, new_rarity = command_params.split(" - ")
        new_rarity = int(new_rarity)
        if plant_name not in plant_dict:
            print("error")
        else:
            plant_dict[plant_name]["rarity"] = new_rarity
    elif command == "Reset":
        plant_name = command_params
        if plant_name not in plant_dict:
            print("error")
        else:
            plant_dict[plant_name]["rating"].clear()
    else:
         print("error")
    commands = input()


for plant_name, value in plant_dict.items():
    if value['rating']:
        avg = sum(value['rating']) / len(value['rating'])
    else:
        avg = 0
    plant_dict[plant_name]['avg'] = avg

sorted_plants = sorted(plant_dict.items(), key=lambda tkvp: (tkvp[1]['rarity'], tkvp[1]['avg']), reverse=True)

print("Plants for the exhibition:")
for plant_name, values in sorted_plants:
    print(f"- {plant_name}; Rarity: {values['rarity']}; Rating: {values['avg']:.2f}")
