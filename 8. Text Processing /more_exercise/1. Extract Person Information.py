def extact_infomration(info):
    index_name_begin = 0
    index_name_end = 0
    age_index_begin = 0
    age_index_end = 0
    name = ""
    age = ""
    for i in range(len(info)):
        if info[i] == "@":
            index_name_begin = i
        elif info[i] == "|":
            index_name_end = i
        elif info[i] == "#":
            age_index_begin = i
        elif info[i] == "*":
            age_index_end = i
    name = info[index_name_begin + 1:index_name_end]
    age = info[age_index_begin + 1:age_index_end]
    return  print(f"{name} is {age} years old.")

n = int(input())

for i in range(n):
    person_information = input()
    extact_infomration(person_information)

