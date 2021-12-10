import sys
def min_number_is(numbers):
    min_number = sys.maxsize
    for i in numbers:
        if int(i) < min_number:
            min_number = int(i)
    return f"The minimum number is {min_number}"
def max_number_is(numbers):
    max_number = -sys.maxsize
    for i in numbers:
        if int(i) > max_number:
            max_number = int(i)
    return  f"The maximum number is {max_number}"
def sum_numbers_is(numbers):
    sum_all = 0
    for i in numbers:
        sum_number = int(i)
        sum_all += sum_number
    return f"The sum number is: {sum_all}"



list_numbers = input().split()

result = min_number_is(list_numbers), max_number_is(list_numbers), sum_numbers_is(list_numbers)
print("\n".join(result))
