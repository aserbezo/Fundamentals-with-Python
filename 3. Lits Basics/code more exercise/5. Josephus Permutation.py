list_itself = input().split()
number = int(input())
final = []
count = 0

index = 0

while len(list_itself) > 0:
    count += 1
    if count % number == 0:
        final.append(list_itself.pop(index))
    else:
        index += 1
    if index >= len(list_itself):
        index = 0

final_new = (",".join(final))
print(f"[{final_new}]")
