number_of_rooms = int(input())
free_chairs = 0
for i in range(1,number_of_rooms + 1):
    each_room = input().split()
    chairs = each_room[0]
    visitors = int(each_room[1])
    if (len(chairs)) < visitors:
        print(f"{visitors - len(chairs)} more chairs needed in room {i}")
        free_chairs -= visitors - len(chairs)
    elif (len(chairs)) > visitors:
        free_chairs += len(chairs) - visitors

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")



