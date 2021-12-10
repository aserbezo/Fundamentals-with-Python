import  math

number_people = int(input())
capacity_people = int(input())

courses = math.ceil(number_people / capacity_people)
print(courses)