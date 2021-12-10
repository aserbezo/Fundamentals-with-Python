import re

pattern =r"\d+" # chislo edno ili poveche

line = input()

while True:
    if line:
        match = re.findall(pattern,line)
        if match:
            print(" ".join(match), end= " ")

    else:
        break

    line = input()