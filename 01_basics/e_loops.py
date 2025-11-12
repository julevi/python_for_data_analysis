# LOOPS

# WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1

print("-----------")

# FOR LOOP - list
students = ["Marcio", "Larissa", "Benedito", "Andre"]
for student in students:
    print(student)

print("-----------")

# FOR LOOP - string
word = "Descomplica"
for letter in word:
    print(letter)

print("-----------")

# Collecting input with loop
names = []
count = 1
while count <= 3:
    names.append(input("Enter student name: "))
    count += 1
print("Student list:", names)

print("-----------")

# Nested loop example (student details)
students = []
for i in range(3):
    student = []
    student.append(input("Name: "))
    student.append(input("CPF: "))
    student.append(input("Email: "))
    student.append(input("Registration number: "))

    # Adding 3 grades
    student.append(float(input("Grade 1: ")))
    student.append(float(input("Grade 2: ")))
    student.append(float(input("Grade 3: ")))

    # Calculate average
    average = (student[4] + student[5] + student[6]) / 3
    student.append("Approved" if average >= 6 else "Failed")

    students.append(student)

print("Students details:")
for s in students:
    print(s)
