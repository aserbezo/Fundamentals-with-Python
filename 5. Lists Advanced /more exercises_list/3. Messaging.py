list_numbers = input().split()
word = input()
new_list = []
sum = 0
final = []

for i in range(len(list_numbers)):
    current_number = list_numbers[i]
    for i in current_number:
        sum += int(i)
    new_list.append(sum)
    sum = 0

for j in new_list:
    element = j

    if element > (len(word)):
        index = (element - len(word))
        final.append(word[index])
        word = word[0:index:] + word[index + 1::]

    else:
        index = element
        final.append(word[index])
        word = word[0:index:] + word[index + 1::]

print("".join(final))
