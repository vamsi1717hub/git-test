students = {}   # Dictionary to store student names and marks

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    total = 0
    for j in range(3):
        mark = float(input(f"Enter marks for subject {j+1}: "))
        total += mark
    average = total / 3
    students[name] = average

print("\nStudent Averages:")
for name, avg in students.items():
    print(f"{name}: {avg:.2f}")

# Find top student
topper = max(students, key=students.get)
print(f"\nTop student is {topper} with average {students[topper]:.2f}")