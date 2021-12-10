
text = input()
color_count = {}
data_dwarfs = {}
colors = {}
while text != "Once upon a time":
    split = text.split(" <:> ")
    dwarf_name = split[0]
    dwarf_hat_color = split[1]
    dwarf_physics = int(split[2])
    dwarf_name = f"({dwarf_hat_color}) {dwarf_name}"
    if dwarf_name not in data_dwarfs:
        data_dwarfs[dwarf_name] = {"physics":dwarf_physics, "colors":dwarf_hat_color}
        if dwarf_hat_color not in color_count:
            color_count[dwarf_hat_color] = 1
        else:
            color_count[dwarf_hat_color] += 1
    else:
        if data_dwarfs[dwarf_name]["physics"] < dwarf_physics:
            data_dwarfs[dwarf_name]["physics"] = dwarf_physics

    text = input()

for n_dwarf, i_dwarf in data_dwarfs.items():
    colors = i_dwarf["colors"]

    i_dwarf["colors"] = color_count[colors]

my_dick = sorted(data_dwarfs.items(),key=lambda kvpt: (-kvpt[1]['physics'], -kvpt[1]["colors"]))

for key, value in my_dick:
    print(f"{key} <-> {value['physics']}")