text = input()
result_text = ""
bomp_power = 0
i = 0

while i < len(text):
    curr_ch = text[i]
    if curr_ch != ">":
        result_text += curr_ch
    else:
        result_text += ">"
        bomp_power += int(text[i + 1])
        while bomp_power > 0:
            i += 1


            if i >= len(text):
                break

            curr_ch = text[i]

            if curr_ch == ">":
                result_text += ">"
                bomp_power += int(text[i + 1])
            else:
                bomp_power -= 1
    i += 1

print(result_text)