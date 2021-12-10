list_of_number = input().split()
count_of_number_remove = int(input())
final = []

for index in range(len(list_of_number)):
    list_of_number[index] = int(list_of_number[index])

for i in range(count_of_number_remove):
    min_element = min(list_of_number)

    list_of_number.remove(min_element)
    final = list_of_number

for index in range(len(list_of_number)):
    list_of_number[index] = str(list_of_number[index])

print(", ".join(final))