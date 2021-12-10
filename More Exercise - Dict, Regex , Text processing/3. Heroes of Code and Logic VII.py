n = int(input())
heroes = {}
for _ in  range(n):
    hero_name, hp, mp = input().split()
    heroes[hero_name] = {"HP": int(hp), "MP": int(mp)}

data = input()

while data != "End":
    split = data.split(" - ")
    if split[0] == "CastSpell":
        hero_name, mp_needed,spell_name = split[1:]
        mp = int(mp_needed)
        if heroes[hero_name]["MP"] >= mp:
            heroes[hero_name]["MP"] -= mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif split[0] == "TakeDamage":
        hero_name, damage, attacker = split[1:]
        damage = int(damage)
        if heroes[hero_name]["HP"] - damage <= 0:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
        else:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
    elif split[0] == "Recharge":
        hero_name, amount = split[1:]
        amount = int(amount)
        if heroes[hero_name]["MP"] + amount > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")

        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif split[0] == "Heal":
        hero_name, amount = split[1:]
        amount = int(amount)
        if heroes[hero_name]["HP"] + amount > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["MP"] = 100
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")


    data = input()

sorted_heroes = sorted(heroes.items(), key= lambda kvpt: (-kvpt[1]["HP"],kvpt[0]))

for name, value in sorted_heroes:
    print(name)
    print(f"  HP: {value['HP']}")
    print(f"  MP: {value['MP']}")
