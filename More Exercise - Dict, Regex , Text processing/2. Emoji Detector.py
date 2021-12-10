import re

text = input()

numbers = [int(el) for el in re.findall(r"\d",text)]

cool_threshold= 1
for num in numbers:
    cool_threshold *= num
print(f"Cool threshold: {cool_threshold}")
pattern = r"(::|\*\*)[A-Z][a-z]{2,}\1" # {2,} opredelqme kolko texst
result = re.finditer(pattern, text)
cool_emojis = []
emojis_count = 0
for match in result:
    emoji = match.group()
    emoji_without_surround = emoji.replace(emoji[0],"")
    emoji_coolness = sum([ord(el) for el in emoji_without_surround])
    if emoji_coolness >= cool_threshold:
        cool_emojis.append(emoji)

    emojis_count += 1

print(f"{emojis_count} emojis found in the text. The cool ones are:")
for i in cool_emojis:
   print(i)
