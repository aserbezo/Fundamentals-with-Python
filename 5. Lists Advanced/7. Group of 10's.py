numbers = [int(number) for number in input().split(", ")]
count = 0
group_of_numbers = 10
while count < len(numbers):
        collected_numbers = []
        for number in numbers:
            if group_of_numbers - 10 < number <= group_of_numbers:
                collected_numbers.append(number)
                count += 1
        print(f"Group of {group_of_numbers}'s: {collected_numbers}")
        group_of_numbers += 10
