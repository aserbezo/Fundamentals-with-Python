sums_list = input().split(", ")
number_beggars = int(input())
final_list = []
counter_of_index = 0
temp_sum = 0

sum_list_as_digits = []

for index in range(len(sums_list)):
        sum_list_as_digits.append(int(sums_list[index]))

while counter_of_index < number_beggars:
       for element in range(counter_of_index, len(sum_list_as_digits), number_beggars):
           temp_sum += sum_list_as_digits[element]
       final_list.append(temp_sum)
       temp_sum = 0
       counter_of_index += 1
print(final_list)