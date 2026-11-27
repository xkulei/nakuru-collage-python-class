# Python beginner lesson: from first program to a grade report

Based on Bravin Kulei. This handout uses original classroom examples in the same topic order. Suggested class length: 75–90 minutes, including practice.

## Learning goals

By the end, students should be able to run a `.py` file, store values in variables, build strings with f-strings, read input, work with lists, make decisions with `if`, repeat work with `for`, and define and call a function.

## Before class: setup (video 00:21–04:38)

1. Install Python from [python.org](https://www.python.org/downloads/) if it is not already installed. On Windows, make sure the Python launcher is available.
2. Install [Visual Studio Code](https://code.visualstudio.com/) and its **Python** extension.
3. Open a folder in VS Code, create `hello.py`, and type:

```python
print("Hello, class!")
```

4. Save, open **Terminal → New Terminal**, and run `py hello.py` on Windows or `python3 hello.py` on macOS/Linux. Expected output: `Hello, class!`

**Explain:** A `.py` file is a text file containing instructions. Python runs the instructions from top to bottom. `print()` displays a value in the terminal. Quotation marks tell Python that `Hello, class!` is text.

**Ask students:** What happens if the quotes are removed? Let them try it. Python then treats `Hello` as a name and reports an error. Errors are clues about what to fix.

## Suggested flow

| Time | Topic | Video position | Live activity |
| --- | --- | --- | --- |
| 0–10 min | Setup and first program | 00:21–04:38 | Run `hello.py` |
| 10–20 min | Variables and values | 04:39 | Change a price and rerun |
| 20–30 min | Strings and f-strings | 07:36–09:16 | Make a personalized sentence |
| 30–40 min | Input | 09:17 | Ask for a name and age |
| 40–55 min | Lists and conditionals | 11:02–14:36 | Store marks and decide pass/fail |
| 55–65 min | For loops | 14:37 | Print every mark |
| 65–75 min | Functions | 16:14 | Turn a rule into a function |
| 75–90 min | Grade report and exercises | 17:39 | Build and modify the final program |

The 06:26 section is a course promotion; skip it during teaching.

## 1. Variables: named storage (video 04:39)

Run `01_basics.py` one section at a time, or type each snippet live.

```python
item = "Notebook"
price = 150
quantity = 3
total = price * quantity

print(item)
print(total)
```

Output:

```text
Notebook
450
```

**Walk through it:** `item` holds a string (text). `price` and `quantity` hold integers (whole numbers). `=` assigns a value; it does not mean “is equal to” in a question. `*` multiplies. `total` is calculated when that line runs. If you later change `price`, you must calculate `total` again to update it.

```python
price = 200
print(total)          # Still 450
total = price * quantity
print(total)          # Now 600
```

**Try:** Change `quantity` to 5. Predict the output before running. Avoid spaces in variable names; use `unit_price`, not `unit price`.

## 2. Strings and f-strings (video 07:36–09:16)

A string is text inside quotes. An f-string places values into text using `{}`.

```python
student = "Amina"
subject = "Python"
marks = 82

print(student + " studies " + subject)
print(f"{student} scored {marks} in {subject}.")
```

Output:

```text
Amina studies Python
Amina scored 82 in Python.
```

**Explain:** The first line joins strings with `+`. The second is easier to read and can insert a number directly. The `f` must come before the opening quote. `{marks}` looks up the value of the variable; `"marks"` would print the literal word.

**Try:** Add a `course` variable and print `Amina studies Python in the Computing course.`

## 3. User input (video 09:17)

Run `02_input.py` and type answers at the prompts.

```python
name = input("What is your name? ")
age_text = input("How old are you? ")
age = int(age_text)

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1}.")
```

Sample run:

```text
What is your name? Brian
How old are you? 19
Hello, Brian!
Next year you will be 20.
```

**Important:** `input()` always returns text. `int("19")` converts it to an integer so arithmetic works. If a student types `nineteen`, `int()` raises `ValueError`. For this first lesson, ask them to enter digits; validation can be a later topic. `print("19" + "1")` gives `191`, while `print(19 + 1)` gives `20`.

**Try:** Ask for a town and print `Brian lives in Nairobi.` using an f-string.

## 4. Lists: several values in one variable (video 11:02)

```python
scores = [72, 85, 64]

print(scores)
print(scores[0])
scores.append(90)
print(scores)
print(len(scores))
```

Output:

```text
[72, 85, 64]
72
[72, 85, 64, 90]
4
```

**Explain:** A list keeps values in order. Indexes start at **0**, so `scores[0]` is the first value. `append()` adds one value at the end. `len()` counts items. `scores[4]` here would cause `IndexError` because the valid indexes are 0–3.

**Try:** Store three course names in a list, then print the second one.

## 5. Conditionals: choose a path (video 12:36)

```python
score = 64

if score >= 70:
    print("Distinction")
elif score >= 50:
    print("Pass")
else:
    print("Try again")
```

Output: `Pass`

**Walk through it:** Python checks the conditions from top to bottom. Once one is true, it runs that indented block and skips the rest. `>=` means greater than or equal to. The colon starts a block, and indentation shows which statements belong to it. `==` checks equality; `=` assigns a value.

**Try:** Predict the output for 70, 50, and 49. Then change the code and test each prediction.

## 6. For loops: repeat for every item (video 14:37)

```python
scores = [72, 85, 64]

for score in scores:
    print(f"Recorded score: {score}")

print("All scores printed.")
```

Output:

```text
Recorded score: 72
Recorded score: 85
Recorded score: 64
All scores printed.
```

**Explain:** The loop takes each item from `scores` and temporarily calls it `score`. The indented print runs three times. The last print is outside the loop, so it runs once. The singular/plural naming (`score`/`scores`) helps students see the difference.

**Try:** Change the list to four scores. No loop code needs changing.

## 7. Functions: give a block of code a name (video 16:14)

```python
def result_for(score):
    if score >= 50:
        return "Pass"
    return "Try again"


print(result_for(64))
print(result_for(42))
```

Output:

```text
Pass
Try again
```

**Walk through it:** `def` defines the function but does not run its body yet. `score` is a parameter, a local name for the value supplied in a call. `result_for(64)` calls it with 64. `return` gives a result back to the caller. `print` displays something; `return` makes a value available for later code.

**Try:** Extend the function to return `"Distinction"` for 70 or above. Test it with 70, 50, and 49.

## 8. Full program: three-score grade report (video 17:39)

Run `05_grade_report.py`. This original project combines the topics above. Type a name and three numeric scores.

```python
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
```

Sample run:

```text
Student name: Amina
Quiz 1 score: 80
Quiz 2 score: 70
Quiz 3 score: 90

Report for Amina
Score: 80
Score: 70
Score: 90
Average: 80.0
Result: Distinction
```

**Build it in stages:** First collect and print the name. Next collect one score, then change to a loop collecting three. Print the list. Calculate the average. Add the `grade_for` function last. This makes each new idea visible.

**New helpers used here:** `range(1, 4)` produces 1, 2, 3. `float()` allows scores such as `72.5`. `sum(scores)` adds the values. `len(scores)` counts them. `\n` begins a new line. `:.1f` formats a number to one decimal place; `:g` avoids an unnecessary `.0` when printing whole scores.

**Limitation:** The program expects numeric scores. Ask students what should happen if someone enters `abc` or 120; input validation is a good follow-up lesson.

## Student practice

1. **Predict:** What do `print(3 + 2 * 4)` and `print("3" + "2")` show? Run them after predicting.
2. **Modify:** Change the grade report to use **four** quizzes. Which number in `range()` changes?
3. **Modify:** Add a `"Credit"` result for averages from 60 to 69.9. Keep distinction at 70 or above and pass at 50 or above.
4. **Build:** Make a shopping list with three items. Use a loop to print `Remember to buy: <item>` for each one.
5. **Challenge:** Ask for a student's name and score, then print a personalized pass/fail message using a function and an f-string.

### Instructor answer key

1. `11` (multiplication first), then `32` (text joining).
2. Use `range(1, 5)` to produce 1, 2, 3, 4.
3. Add `elif average >= 60: return "Credit"` between distinction and pass.
4. `items = ["milk", "bread", "rice"]`, then `for item in items: print(f"Remember to buy: {item}")` on an indented next line.
5. Define `result_for(score)` as in section 7; get `name` with `input()`, get `score` with `float(input(...))`, then `print(f"{name}: {result_for(score)}")`.

## Common mistakes to demonstrate

| Mistake | What happens | Fix |
| --- | --- | --- |
| `print(Hello)` | Python looks for a variable named `Hello` | Use `print("Hello")` |
| `input(...) + 1` | Cannot add text and an integer | Convert with `int()` or `float()` |
| `scores[1]` for the first item | Prints the second item | Use `scores[0]` |
| Missing colon after `if`, `for`, or `def` | Syntax error | Add `:` |
| Unindented line inside an `if` or loop | Indentation error or wrong behavior | Indent the block consistently |
| `if score = 50:` | Syntax error | Use `==` to compare |

## Exit ticket (last 5 minutes)

Ask students to write, without notes: (1) what `input()` returns, (2) the first index of a list, and (3) the difference between `print` and `return`. Then have them run one modified version of the grade report.
