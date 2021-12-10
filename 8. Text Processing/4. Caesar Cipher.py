text = input()

encrypten_text = ""

for ch in text:
    curr_ch_code = ord(ch)

    encrypted_ch = chr(curr_ch_code + 3)

    encrypten_text += encrypted_ch

print(encrypten_text)


# text = input()
# encrypten_list = [chr(ord(ch) + 3) for ch in text]
# print(encrypten_list)