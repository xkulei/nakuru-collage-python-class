item = "Notebook"
price = 150
quantity = 3
total = price * quantity

print(item)
print(total)

price = 200
print(total)  # The earlier calculation is still 450.
total = price * quantity
print(total)

student = "Amina"
subject = "Python"
marks = 82
print(student + " studies " + subject)
print(f"{student} scored {marks} in {subject}.")
