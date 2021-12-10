def result(result, banned):
    user_sumbishion = {}
    for i in result.values():
        username = i[0]
        language = i[1]
        points = int(i[2])
        if username not in user_sumbishion:
            user_sumbishion[username] = points
        else:
            if username in user_sumbishion and points > user_sumbishion[username]:
                user_sumbishion[username] = points

        if username in banned:
            user_sumbishion.pop(username)

    return user_sumbishion

def submishions_attemt(result):
    language_count = {}
    for i in result.values():
        language = i[1]
        if language not in language_count:
            language_count[language] = 1
        else:
            if language in language_count:
                language_count[language] += 1
    return language_count

submishions = {}
banned_username = []
key_count = 0

command = input()

while command != "exam finished":

    if "banned" in command:
        receivng = command.split("-")
        username = receivng[0]
        banned_username.append(username)
    else:
        key_count +=1
        receivng = command.split("-")
        username = receivng[0]
        language = receivng[1]
        points =  receivng[2]
        submishions[key_count] = username, language, points

    command = input()

final = (result(submishions,banned_username))
final_sumbs = (submishions_attemt(submishions))
print("Results:")
for key ,value in sorted(final.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f"{key} | {value}")

print("Submissions:")
for key ,value in sorted(final_sumbs.items(), key=lambda kvp: kvp[0]):
    print(f"{key} - {value}")

