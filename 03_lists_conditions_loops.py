scores = [72, 85, 64]

print(scores)
print(scores[0])
scores.append(90)
print(scores)
print(len(scores))

score = 64
if score >= 70:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Try again")

for score in scores:
    print(f"Recorded score: {score}")

print("All scores printed.")
