

courses = {}


command = input()

while command != "end":
    receiving = command.split(" : ")
    course_name = receiving[0]
    student_name = receiving[1]

    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student_name)
    else:
        courses[course_name].append(student_name)

    command = input()

for key, value in sorted(courses.items(), key=lambda kvp: - len(kvp[1])):
    print(f"{key}: {len(courses[key])}")
    for i in sorted(value):
        print(f"-- {i}")


