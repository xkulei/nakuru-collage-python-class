def status_label(code):
    if code == "p":
        return "Present"
    elif code == "a":
        return "Absent"
    return "Unknown"


names = []
attendance = []

for number in range(1, 5):
    name = input(f"Student {number} name: ")
    code = input(f"Attendance for {name} (p/a): ").lower()
    names.append(name)
    attendance.append(code)

present_count = 0
absent_count = 0

print("\n=== ATTENDANCE REGISTER ===")
for index in range(len(names)):
    code = attendance[index]
    print(f"{names[index]}: {status_label(code)}")
    if code == "p":
        present_count = present_count + 1
    elif code == "a":
        absent_count = absent_count + 1

print(f"Present: {present_count}")
print(f"Absent: {absent_count}")
