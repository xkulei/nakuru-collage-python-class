questions = [
    "Which function displays text? (a) input (b) print (c) len",
    "What is the first list index? (a) 0 (b) 1 (c) -1",
    "Which keyword defines a function? (a) for (b) if (c) def",
]
correct_answers = ["b", "a", "c"]


def point_for(answer, correct_answer):
    if answer.lower() == correct_answer:
        return 1
    return 0


score = 0

for index in range(len(questions)):
    answer = input(f"{index + 1}. {questions[index]}: ")
    point = point_for(answer, correct_answers[index])
    score = score + point

    if point == 1:
        print("Correct!")
    else:
        print(f"Incorrect. The answer is {correct_answers[index]}.")

print(f"\nScore: {score}/{len(questions)}")
if score >= 2:
    print("Result: Pass")
else:
    print("Result: Try again")
