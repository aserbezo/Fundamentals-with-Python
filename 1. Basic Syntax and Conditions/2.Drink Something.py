#  Rules:
# A kid is defined as someone under the age of 14.
# A teen is defined as someone under the age of 18.
# A young adult is defined as someone under the age of 21.
# An adult is defined as someone above the age of 21.
# Note: All the values are inclusive except the last one!

age = int(input())

if age <= 14:
    print("drink toddy")
elif age <= 18:
    print("drink coke")
elif age <= 21:
    print("drink beer")
else:
    print("drink whisky")


