def get_even_odd_numbers(number):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_numbers += int(digit)
        else:
            sum_of_odd_numbers += int(digit)
    return  sum_of_even_numbers , sum_of_odd_numbers

number_as_string = input()
even_sum, odd_sum = get_even_odd_numbers(number_as_string)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")