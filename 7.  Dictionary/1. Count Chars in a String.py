text = input()

my_dict = {}

for i in text:
    if i == " ":
        continue
    else:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

for key,value in my_dict.items():
    print(f"{key} -> {value}")