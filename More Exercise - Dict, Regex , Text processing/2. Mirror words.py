import re

pattern = r"(?P<surr>(@|#))(?P<word_1>[A-Za-z]{3,})(?P=surr)(?P=surr)(?P<word_2>[A-Za-z]{3,})(?P=surr)"

#r"(@|#)[A-za-z]{2,}\1\1[A-Za-z]{3,}\1"


text = input()
mirror_words = []
count = 0
result = re.finditer(pattern,text)
for match in result:
    current_word = match.groupdict() # raboti pri naimenovani grupi
    if current_word["word_1"] == current_word["word_2"][::-1]:
        mirror_words.append(current_word["word_1"])
    count += 1

if count == 0:
    print("No word pairs found!")

else:
    print(f"{count} words pairs found!")

if not mirror_words:
    print("No mirror words!")

else:
    print(f", ".join([f"{word}<=> {word[::-1]}"for word in mirror_words]))

