import re

first_check = r"([star])"
pattern =  r"((?<=@)[A-Za-z]+)[^@!>\-]*((?<=:)\d+)[^@:>\-]*((?<=!)[AD](?=!))[^@:]*((?<=->)\d+)"


n = int(input())
attacker = []
destroy = []
for i in range(n):
    text = input()
    decrypted_text = ""
    key_match = re.findall(first_check,text, re.IGNORECASE)
    key = len(key_match)
    for j in text:
        decrypted_text += chr(ord(j) - key)

    match = re.findall(pattern,decrypted_text)
    if match:
        name = match[0][0]
        population = match[0][1]
        attack_type = match[0][2]
        soldier_count = match[0][3]
        if attack_type == "A":
            attacker.insert(0, name)
        elif attack_type == "D":
            destroy.insert(0, name)



print(f"Attacked planets: {len(attacker)}")
for name in attacker:
	print(f"-> {name}")
print(f"Destroyed planets: {len(destroy)}")
for name in destroy:
	print(f"-> {name}")