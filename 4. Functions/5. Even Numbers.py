numbers = input().split()
numbers_as_digit = []
for number in numbers:
    numbers_as_digit.append(int(number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digit))
print(result)