def decript_message(text,key):
    decript_message = ""
    index = 0
    for i in range(len(text)):
        if index >= len(key):
            index = 0
        letter = ord(text[i]) - int(key[index])
        decript_message += chr(letter)
        index += 1

    return decript_message

def treasure_find(text):
    gold_begin = 0
    gold_end = 0
    cordinates_begin = 0
    cordinates_end = 0
    treasure = ""
    cordinates = ""
    check = []
    result = []
    for i in range(len(text)):
        if text[i] == "&":
            if text[i] not in check:
                check.append(text[i])
                gold_begin = i
            else:
                gold_end = i
        elif text[i] == "<":
            cordinates_begin = i
        elif text[i] == ">":
            cordinates_end = i
    treasure = text[gold_begin + 1:gold_end]
    cordinates = text[cordinates_begin + 1:cordinates_end]
    result.append(treasure)
    result.append(cordinates)
    return result
key = input().split()

stings = input()
meseges = []
while stings != "find":
    decript = decript_message(stings,key)
    meseges.append(treasure_find(decript))



    stings = input()

for i in meseges:
   print(f"Found {i[0]} at {i[1]}")