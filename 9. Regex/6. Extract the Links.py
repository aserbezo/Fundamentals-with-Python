import  re



pattern = r"((www)\.([A-Za-z0-9]+(\-[A-Z-a-z0-9]+)*(\.[a-z]+)+))"
text = input()
valid_urls = []

while text:
    matches = re.finditer(pattern,text)
    for match in matches:
        valid_urls.append(match.group(1))

    text = input()

for valid in valid_urls:
    print(valid)



# * ot nula do poveche puti moje da ima no moje i da e nula