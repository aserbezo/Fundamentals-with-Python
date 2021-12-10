firs_numbers = input().split()
second_number = input().split()
third_number = input().split()

winner_is = False
winner = ""
# rows
if firs_numbers[0] == firs_numbers[1] == firs_numbers[2] != "0":
        winner_is = True
        winner = firs_numbers[0]
elif second_number[0] == second_number[1] == second_number[1] != "0":
        winner_is = True
        winner = second_number[1]
elif third_number[0] == third_number[1] == third_number[2] != "0":
        winner_is = True
        winner  = third_number[2]
# collums
if firs_numbers[0] == second_number[0] == third_number[0] != "0":
    winner_is = True
    winner = firs_numbers[0]
elif firs_numbers[1] == second_number[1] == third_number[1] != "0":
    winner_is = True
    winner = firs_numbers[1]
elif firs_numbers[2] == second_number[2] == third_number[2] != "0":
    winner_is = True
    winner = firs_numbers[2]

# diagnolas
if firs_numbers[0] == second_number[1] == third_number[2] != "0":
    winner_is = True
    winner = firs_numbers[0]
elif firs_numbers[2] == second_number[1] == third_number[0] != "0":
    winner_is = True
    winner = firs_numbers[2]


if not winner_is:
    print("Draw!")

else:
    if winner == "1":
        print("First player won")
    elif winner == "2":
        print("Second player won")

