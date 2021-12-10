
command = input()
spell_book ={}
while command != "End":
    split = command.split()
    if split[0] == "Enroll":
        hero_name = split[1]
        if hero_name not in spell_book:
            spell_book[hero_name] = ""
        else:
            print(f"{hero_name} is already enrolled.")
    elif split[0] == "Learn":
        hero_name_1, spell_name = split[1:]
        if hero_name_1 in spell_book:
            if spell_name not in spell_book.values():
               spell_book[hero_name_1] = spell_name
            else:
                print(f"{hero_name_1} has already learnt {spell_book[hero_name]}.")
        else:
            print(f"{hero_name_1} doesn't exist.")

    elif split[0] == "Unlearn":
        hero_name_2, spell_name_1 = split[1:]
        if hero_name_2 in spell_book:
            if spell_name_1 in spell_book.values():
               del spell_book[hero_name_2]
               spell_book[hero_name_2] = ""
            else:
                print(f"{hero_name_2} doesn't know {spell_name_1}.")

        else:
             print(f"{hero_name_2} doesn't exist.")

    command = input()


print("Heroes:")

sorted_dict = sorted(spell_book.items(),key= lambda kvpt: (-len(kvpt[1]),kvpt[0]))

for key , value in sorted_dict:
    print(f"== {key}: {value}")