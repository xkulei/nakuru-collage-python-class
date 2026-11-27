# Four beginner Python projects

These projects follow the [first lesson](../python_beginner_lesson.md). Each project has a `starter.py` for students and a `solution.py` for the instructor. Students need only Python 3; no extra packages or internet access are required.

## How to run

Open a terminal in this folder. On Windows, run `py 01_profile_card/starter.py` (replace the path with the project you are teaching). On macOS or Linux, use `python3` in place of `py`. Keep the `solution.py` files out of the student handout until the activity is over.

| Project | Suggested time | Main concepts | Difficulty |
| --- | --- | --- | --- |
| 1. Profile card | 15–20 min | `input`, variables, `int`, f-strings | First solo project |
| 2. Canteen bill | 25–30 min | Numbers, arithmetic, `if`, functions | Guided pairs |
| 3. Mini quiz | 30–40 min | Lists, `for`, `if`, function returns | Pairs |
| 4. Attendance register | 30–40 min | Lists, loops, conditionals, functions | Independent or homework |

## Teaching pattern for each project

1. Show the sample run and ask students to describe the inputs, processing, and outputs.
2. Let them write the first few lines before showing more guidance.
3. Run the program after each small step. Ask students to predict outputs first.
4. Use the challenge only after the core version works.
5. Finish with a two-minute explanation from a student: “What does this variable hold?” or “Why does this loop run this many times?”

---

## Project 1: Student profile card

**Situation:** The program creates a short introduction for a new student.

**Requirements**

- Ask for the student's name, course, and age.
- Convert age to a number, then calculate next year's age.
- Print a tidy card using f-strings.

**Sample run**

```text
Name: Amina
Course: Computing
Age: 18

=== STUDENT PROFILE ===
Name: Amina
Course: Computing
Age next year: 19
```

**Build order:** Ask for name and print it. Add course. Add age as text, then convert it with `int()`. Finally calculate and format the card.

**Questions to ask:** What type does `input()` return? Why do we need `int()` before adding 1? What is the difference between `age = 18` and `age == 18`?

**Challenge:** Add a town and a sentence such as `Amina studies Computing and lives in Nairobi.`

---

## Project 2: Canteen bill

**Situation:** A campus canteen sells several units of one item. Bills of 500 or more receive a 10% discount.

**Requirements**

- Ask for the item name, unit price, and quantity.
- Calculate `subtotal = unit_price * quantity`.
- Write `discount_for(subtotal)` to return 10% of the subtotal when it is at least 500; otherwise return 0.
- Print subtotal, discount, and amount due to two decimal places.

**Sample run**

```text
Item: Lunch
Unit price: 200
Quantity: 3

=== CANTEEN BILL ===
Item: Lunch
Subtotal: 600.00
Discount: 60.00
Amount due: 540.00
```

**Test another case:** 2 items at 200 each should give a subtotal of 400, discount of 0, and amount due of 400.

**Build order:** Calculate the subtotal before writing the function. Test the function with `discount_for(600)` and `discount_for(400)`. Then connect it to the input and print the bill.

**Questions to ask:** Why does `discount_for` use `return`? Why does the code check `>= 500` rather than `> 500`? What does `:.2f` do?

**Challenge:** Add a 5% discount for bills from 300 up to but below 500.

---

## Project 3: Three-question mini quiz

**Situation:** Students answer three multiple-choice Python questions. The program awards one point for each correct answer.

**Requirements**

- Store three questions in a list and their correct answer letters in a second list.
- Use a `for` loop to ask every question.
- Compare the answer to the matching correct letter. Give 1 for correct and 0 for incorrect.
- Print the score out of 3 and a pass message for scores of 2 or 3.

**Sample run**

```text
1. Which function displays text? (a) input (b) print (c) len: b
Correct!
2. What is the first list index? (a) 0 (b) 1 (c) -1: a
Correct!
3. Which keyword defines a function? (a) for (b) if (c) def: b
Incorrect. The answer is c.

Score: 2/3
Result: Pass
```

**Build order:** First print each question with a loop. Then ask for answers. Then add a helper function that checks one answer and returns a point. Finally total the points and print the result.

**Questions to ask:** Why are there two lists? Why must their items stay in the same order? How many times does the loop run? What happens when the answer is uppercase `B`? The solution uses `.lower()` to accept it.

**Challenge:** Add a fourth question and correct answer. The loop should automatically handle it; change the score display to use `len(questions)` rather than a fixed number.

---

## Project 4: Attendance register

**Situation:** Record whether four students are present or absent, then print a class summary.

**Requirements**

- Ask for four student names.
- For each student, ask for `p` (present) or `a` (absent).
- Store names and attendance codes in lists.
- Use a loop to print every student's status and count how many are present.
- Print the number present and absent.

**Sample run**

```text
Student 1 name: Amina
Attendance for Amina (p/a): p
Student 2 name: Brian
Attendance for Brian (p/a): a
Student 3 name: Chao
Attendance for Chao (p/a): p
Student 4 name: Diana
Attendance for Diana (p/a): p

=== ATTENDANCE REGISTER ===
Amina: Present
Brian: Absent
Chao: Present
Diana: Present
Present: 3
Absent: 1
```

**Build order:** Collect just names and print them. Add attendance codes. Write a `status_label(code)` function to turn `p` or `a` into a word. Then calculate totals.

**Questions to ask:** Why do `names[0]` and `attendance[0]` belong together? Why is `present_count` initialized to 0? What happens if someone types an unexpected code?

**Challenge:** Prevent unexpected codes from being counted as absent. For now, print `Unknown` for any code other than `p` or `a`; input validation with repeated prompts can be a later lesson.

## Quick assessment checklist

For each project, check that the student can explain what each input becomes, identify one variable's value during execution, predict a condition's outcome, and make one small change without copying the solution.
