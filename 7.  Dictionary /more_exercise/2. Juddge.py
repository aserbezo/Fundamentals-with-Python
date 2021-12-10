def check_individual(my_dict:dict,participant:dict):
    for key, value in my_dict.items():
        for nes_k, nes_v in value.items():
            if nes_k not in participant:
                participant[nes_k] = nes_v
            else:
                participant[nes_k] += nes_v
    return participant

contest  = input()
contest_book = {}
individual_score={}
while contest != "no more time":
    split = contest.split(" -> ")
    username = split[0]
    contest_name = split[1]
    points = int(split[2])
    if contest_name not in contest_book:
        contest_book[contest_name] = {}
        contest_book[contest_name][username] = points
    else:
        if username in contest_book[contest_name]:
            old_points = contest_book[contest_name][username]
            if points > old_points:
                contest_book[contest_name][username] = points
        else:
            contest_book[contest_name][username] = points
    contest = input()




for key , values in contest_book.items():
    print(f"{key}: {len(contest_book[key])} participants")
    count = 1
    for  nes_k , nes_v in sorted(values.items(),key=lambda kvp: (-kvp[1], kvp[0])):
        print(f"{count}. {nes_k} <::> {nes_v}")
        count += 1

print("Individual standings:")
check_individual(contest_book,individual_score)
sec_count = 1
for i, j in sorted(individual_score.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{sec_count}. {i} -> {j}")
    sec_count += 1