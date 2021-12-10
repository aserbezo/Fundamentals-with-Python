n = int(input())
stdents ={}
for i in range(n):

    student_name = input()
    grade = float(input())
    if student_name not in stdents:
        stdents[student_name] = grade
    else:
        if student_name in stdents:
            stdents[student_name] = (stdents[student_name] + grade)  / 2


for key ,value in sorted(stdents.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
