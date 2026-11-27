def grade_for(average):
    if average >= 70:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Try again"


name = input("Student name: ")
scores = []

for quiz_number in range(1, 4):
    score = float(input(f"Quiz {quiz_number} score: "))
    scores.append(score)

average = sum(scores) / len(scores)

print(f"\nReport for {name}")
for score in scores:
    print(f"Score: {score:g}")
print(f"Average: {average:.1f}")
print(f"Result: {grade_for(average)}")
