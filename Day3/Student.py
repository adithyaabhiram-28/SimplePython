students = []

for i in range(5):
    roll_no = input(f"Enter roll number for student {i+1}: ")
    name = input(f"Enter name for student {i+1}: ")
    marks = int(input(f"Enter marks for student {i+1}: "))
    students.append((roll_no, name, marks))

highest = max(students, key=lambda x: x[2])
print(f"\nStudent with highest marks: {highest[1]} (Marks: {highest[2]})")

print("\nStudents who scored more than 75 marks:")
for student in students:
    if student[2] > 75:
        print(f"{student[1]} (Roll No: {student[0]}, Marks: {student[2]})")