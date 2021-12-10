def collect_material(key_materials_dict: dict, junk_materials: dict, material: str, qty: int):
    if material == 'shards' or material == 'fragments' or material == 'motes':
        # Key material found
        key_materials_dict[material] += qty
    else:
        if material not in junk_materials.keys():
            # Material still does not exist in the junk
            junk_materials[material] = qty
        else:
            # Material already exist in the junk and we need to add the qty
            junk_materials[material] += qty


key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
item_obtained = ''

# While item is still not obtained (empty string)
while item_obtained == '':
    current_line = input().split()

    for i in range(0, len(current_line), 2):
        material_qty = int(current_line[i])
        material_name = current_line[i + 1].lower()

        collect_material(key_materials, junk, material_name, material_qty)

        if key_materials['shards'] >= 250:
            # Obtain an item
            item_obtained = 'Shadowmourne'
            key_materials['shards'] -= 250
            break
        elif key_materials['fragments'] >= 250:
            item_obtained = 'Valanyr'
            key_materials['fragments'] -= 250
            break
        elif key_materials['motes'] >= 250:
            item_obtained = 'Dragonwrath'
            key_materials['motes'] -= 250
            break

print(f'{item_obtained} obtained!')
for (key_material_name, key_material_qty) in sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f'{key_material_name}: {key_material_qty}')

for (junk_material_name, junk_material_qty) in sorted(junk.items(), key=lambda kvp: kvp[0]):
    print(f'{junk_material_name}: {junk_material_qty}')