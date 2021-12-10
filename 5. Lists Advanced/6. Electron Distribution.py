number_electrons = int(input())
final_list = []
count = 0

while 0 < number_electrons :
    count+=1
    shell_positions = 2 * count **2

    if number_electrons >= shell_positions:   # проверка дали има място за максималния капацитет
        final_list.append(shell_positions)
        number_electrons -= shell_positions
    else:                # ако няма попълваме колкото е останало
        final_list.append(number_electrons)
        number_electrons = 0

print(final_list)