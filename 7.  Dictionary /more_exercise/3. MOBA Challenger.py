def battle_check(first,second,my_dict:dict):
    first_points = 0
    second_points = 0
    if first in my_dict and second in my_dict:
        pass
        for key in my_dict[first]:
            pass
            for key_2 in my_dict[second]:
                pass
            if key == key_2:
                first_points += my_dict[first][key]
                second_points += my_dict[second][key_2]
    if first_points > second_points:
        losser = second
    elif second_points > first_points:
        losser = first
    else:
        return False
    return losser

def check_retrurn_player_total_skill(my_dict:dict, player):
    result = 0

    for skill in my_dict[player].values():
        result += skill

    return result

def sort_players_by_skills(my_dict:dict):
    result = {}
    for player_name in my_dict:
        total_skill_points = check_retrurn_player_total_skill(my_dict, player_name)
        result[player_name] = total_skill_points

    return dict(sorted(result.items(), key=lambda x: (-x[1], x[0])))

def get_posionas_of_player(my_dick:dict, player):
    positions = my_dick[player]
    sorted_positions = dict(sorted(positions.items(), key=lambda x: (-x[1], x[0])))
    return sorted_positions

def print_final_result(my_dick:dict):
    final  = sort_players_by_skills(players_pools)

    for key, value in final.items():
        print(f"{key}: {value} skill")
        sorted_positions = get_posionas_of_player(my_dick, key)

        for position, skill in sorted_positions.items():
            print(f"- {position} <::> {skill}")

players_pools = {}
input_lines = input()

while input_lines != "Season end":
    check = input_lines.split()
    first_check = check[0]
    second_check = check[1]
    if second_check == "vs":
        player1 = first_check
        player2 = check[2]
        if battle_check(player1,player2,players_pools):
             players_pools.pop(battle_check(player1,player2,players_pools))
    else:
        text = input_lines.split(" -> ")
        player = text[0]
        positions = text[1]
        skill = int(text[2])

        if player not in players_pools:
            players_pools[player] = {}
            players_pools[player][positions] = skill
        else:
            if positions not in players_pools:
                players_pools[player][positions] = skill
            else:
                if skill > players_pools[player][positions]:
                    players_pools[player][positions] = skill


    input_lines = input()

print_final_result(players_pools)

# for key, value in sorted(players_pools.items(),key= lambda kvp: -kvp[1]):
#     print(f"{key}: {sum(value.values())} skill")
#     for k,v in sorted(value.items(), key=lambda kvp: (-kvp[1])):
#         print(f"- {k} <::> {v}")