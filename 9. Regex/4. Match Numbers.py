import  re


pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(0), end= " ")




 #   \www.[A - Z][a - z | -] + (.)[a - z] + (.)[a - z] +\b

 # \www.[A-Z | a-z]+[|. | -][a-z]+[|. |-][a-z]+[|. |-][a-z]+

 # w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+