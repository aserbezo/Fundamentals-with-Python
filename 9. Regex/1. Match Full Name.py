import re
names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

matches = re.findall(pattern, names)

# for i in names:
#     match = re.match(pattern,i)
#     if match:
#        valid_names.append(match.group())

print(" ".join(matches))