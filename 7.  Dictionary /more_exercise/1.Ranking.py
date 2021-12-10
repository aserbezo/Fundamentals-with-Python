def check_contest_and_password(contest:dict,course:str,password:str):
    if course in contest.keys():
       if contest[course] == password:
           return True
    return False


def check_winner(my_dict:dict):
    participant = {}
    for key, value in my_dict.items():
        for nes_k, nes_v in value.items():
            if nes_k not in participant:
                participant[nes_k] = nes_v
            else:
                participant[nes_k] += nes_v

    winner = (max(participant.keys()))
    points = (max(participant.values()))
    return print(f"Best candidate is {winner} with total {points} points.")

def final_print(my_dict:dict):
    participant = {}
    for key, value in my_dict.items():
        for n_k, n_v in value.items():
            if n_k not in participant:
                participant[n_k] = {}
                participant[n_k][key] = n_v
            else:
                participant[n_k][key] = n_v

    for key, value in sorted(participant.items(), key=lambda kvp: (kvp[0], kvp[1])):
        print(key)
        for nes_key, nes_val in sorted(value.items(), key=lambda kvp: (-kvp[1], kvp[0])):
            print(f"#  {nes_key} -> {nes_val}")

contest = input()
contest_dict = {}
contest_book = {}
while contest != "end of contests":
    split = contest.split(":")
    course = split[0]
    password = split[1]
    if course not in contest_dict:
        contest_dict[course] = password
    contest = input()

submissions = input()

while submissions != "end of submissions":
    splits = submissions.split('=>')
    courser = splits[0]
    passwords = splits[1]
    users = splits[2]
    points = int(splits[3])

    if check_contest_and_password(contest_dict,courser,passwords) == True:
        if courser not in contest_book:
            contest_book[courser] = {}
            contest_book[courser][users] = points
        else:
            if users in contest_book[courser]:
                old_points = contest_book[courser][users]
                if points > old_points:
                    contest_book[courser][users] = points
            else:
                contest_book[courser][users] = points


    submissions = input()
check_winner(contest_book)
print("Ranking:")
final_print(contest_book)

