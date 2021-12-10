
def sum_numbers(first, second):
    return first + second
def subtract(sum ,number):
    return  sum - number

def add_and_subtract(first , second , third):
    sum_first_two_num = sum_numbers(first_number, second_number)
    result = subtract(sum_first_two_num, third_number)
    return  result

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number,second_number,third_number))