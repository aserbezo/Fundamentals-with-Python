list_of_numbers = input().split()
oposite_numbers  = []
for index in range(len(list_of_numbers)):
    oposite = -int(list_of_numbers[index])
    oposite_numbers.append(oposite)

print(oposite_numbers)