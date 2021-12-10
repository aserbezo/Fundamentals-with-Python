def sorting_number(list_numbers):
    return sorted(list_numbers) # reverse = True

sequence_numbers = input().split()
filetered_numbers = []
for number in sequence_numbers:
    filetered_numbers.append(int(number))
sorted_numbers = sorting_number(filetered_numbers)
print(sorted_numbers)