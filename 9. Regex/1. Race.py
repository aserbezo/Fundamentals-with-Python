import  re

pattern = r"[A-Za-z]+"
pattern2 = r"\d"
check = {}
participants = input().split(", ")

text = input()
while text != "end of race":
    name = ""
    total = 0
    match = re.findall(pattern,text)
    if match:
        for i in match:
            name += i
        if name in participants:
           second_match = re.findall(pattern2,text)
           if second_match:
              for j in second_match:
                  total += int(j)
              if name not in check:
                 check[name] = total
              else:
                  check[name] += total

    text = input()

count = 0
for key , value in sorted(check.items(), key= lambda kvp: -kvp[1]):
    count += 1
    if count == 1:
       print(f"1st place: {key}")
    elif count == 2:
        print(f"2nd place: {key}")
    else:
        if count >= 3:
           print(f"3rd place: {key}")
           break
