single_strig_inegers = input().split(", ")
count_beggar = int(input())
list_of_sum = []
sum_list_digits = []
couter_while = 0
temp_sum = 0
for i in range(len(single_strig_inegers)):
    sum_list_digits.append(int(single_strig_inegers[i]))

while couter_while < count_beggar:
    for element in range(couter_while, len(sum_list_digits), count_beggar):
        print(sum_list_digits[element])
        #temp_sum += sum_list_digits[element]
    #list_of_sum.append(temp_sum)
    #temp_sum = 0
    couter_while += 1

print(list_of_sum)