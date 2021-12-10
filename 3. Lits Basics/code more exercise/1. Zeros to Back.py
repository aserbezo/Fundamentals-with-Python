list_integers = input().split(",")

for i in range(len(list_integers)):
    list_integers[i] = int(list_integers[i])

for i in range(len(list_integers)):
    if 0  in list_integers:
        list_integers.remove(0)
        list_integers.append(0)
print(list_integers)