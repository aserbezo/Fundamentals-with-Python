fire_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
final = []



print("Cells:")

for i in fire_cells:
    new_split = i.split(" = ")
    type_fire = new_split[0]
    range = int(new_split[1])
    if water < range:
        continue
    if type_fire == "High":
        if 81 <= range <= 125:
            final.append(range)
            water -= range
    elif type_fire == "Medium":
        if 51 <= range <= 80:
            final.append(range)
            water -= range
    elif type_fire == "Low":
        if 1 <= range <= 50:
            final.append(range)
            water -= range

for i in final:
    effort += i
    energy = effort * 0.25
    print(f" - {i}")


print(f"Effort: {energy:.2f}")
print(f"Total Fire: {effort}")