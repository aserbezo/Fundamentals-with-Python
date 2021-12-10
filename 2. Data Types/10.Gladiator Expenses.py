lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())


# Every second lost game, his helmet is broken
# Every third lost game, his sword is broken
# When both his sword and helmet are broken in the same lost fight, his shield also breaks
# Every second time his shield brakes, his armor also needs to be repaired.


# •	As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus."
trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
trashed_armour = 0
for i in range(1 , lost_fights + 1):

    if i % 2 == 0:
        trashed_helmet+= 1
    if i % 3 == 0:
        trashed_sword += 1
    if i % 6 == 0:
        trashed_shield += 1
        if trashed_shield % 2 == 0:
            trashed_armour += 1

expenses_helmet = trashed_helmet * helmet_price
expenses_shield = trashed_shield * shield_price
expenses_sword = trashed_sword * sword_price
expenses_armour = trashed_armour * armour_price
total = expenses_helmet + expenses_armour + expenses_sword + expenses_shield
print(f"Gladiator expenses: {total:.2f} aureus")





