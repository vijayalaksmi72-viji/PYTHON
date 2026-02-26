score = 0

print("WELCOME TO PYTHON MCQ QUIZ")
print("---------------------------")

q1 = q2 = q3 = q4 = q5 = ""
q6 = q7 = q8 = q9 = q10 = ""

print("\n1. Python is a _____ language")
print("a) Low level")
print("b) High level")
print("c) Machine")
print("d) Assembly")
ans = input("Enter answer: ")
if ans == 'b':
    score += 1
    q1 = "Q1 ✓ Correct"
else:
    q1 = "Q1 ✗ Wrong (Correct: b)"


print("\n2. Which symbol is used for comments in Python?")
print("a) //")
print("b) /* */")
print("c) #")
print("d) %")
ans = input("Enter answer: ")
if ans == 'c':
    score += 1
    q2 = "Q2 ✓ Correct"
else:
    q2 = "Q2 ✗ Wrong (Correct: c)"


print("\n3. What is the correct extension of Python file?")
print("a) .pt")
print("b) .pyt")
print("c) .py")
print("d) .python")
ans = input("Enter answer: ")
if ans == 'c':
    score += 1
    q3 = "Q3 ✓ Correct"
else:
    q3 = "Q3 ✗ Wrong (Correct: c)"

print("\n4. Which keyword is used to define a function?")
print("a) fun")
print("b) def")
print("c) function")
print("d) define")
ans = input("Enter answer: ")
if ans == 'b':
    score += 1
    q4 = "Q4 ✓ Correct"
else:
    q4 = "Q4 ✗ Wrong (Correct: b)"

print("\n5. Which data type is used to store text?")
print("a) int")
print("b) float")
print("c) str")
print("d) bool")
ans = input("Enter answer: ")
if ans == 'c':
    score += 1
    q5 = "Q5 ✓ Correct"
else:
    q5 = "Q5 ✗ Wrong (Correct: c)"


print("\n6. Which operator is used for exponentiation in Python?")
print("a) ^")
print("b) **")
print("c) %")
print("d) //")
ans = input("Enter answer: ")
if ans == '**':
    score += 1
    q6 = "Q6 ✓ Correct"
else:
    q6 = "Q6 ✗ Wrong (Correct: **)"

print("\n7. Which of these is a Python tuple?")
print("a) [1, 2, 3]")
print("b) (1, 2, 3)")
print("c) {1, 2, 3}")
print("d) <1, 2, 3>")
ans = input("Enter answer: ")
if ans == 'b':
    score += 1
    q7 = "Q7 ✓ Correct"
else:
    q7 = "Q7 ✗ Wrong (Correct: b)"


print("\n8. What is the output of print(2 * 3)?")
print("a) 5")
print("b) 6")
print("c) 23")
print("d) Error")
ans = input("Enter answer: ")
if ans == 'b':
    score += 1
    q8 = "Q8 ✓ Correct"
else:
    q8 = "Q8 ✗ Wrong (Correct: b)"


print("\n9. Which keyword is used for loops in Python?")
print("a) loop")
print("b) for")
print("c) iterate")
print("d) repeat")
ans = input("Enter answer: ")
if ans == 'b':
    score += 1
    q9 = "Q9 ✓ Correct"
else:
    q9 = "Q9 ✗ Wrong (Correct: b)"


print("\n10. What does len() function do?")
print("a) Counts items")
print("b) Adds items")
print("c) Deletes items")
print("d) None")
ans = input("Enter answer: ")
if ans == 'a':
    score += 1
    q10 = "Q10 ✓ Correct"
else:
    q10 = "Q10 ✗ Wrong (Correct: a)"


print("\n---------------------------")
print("Quiz Completed!")
print("Your Score:", score, "/ 10")

print("\n--- ANSWER SUMMARY ---")
print(q1)
print(q2)
print(q3)
print(q4)
print(q5)
print(q6)
print(q7)
print(q8)
print(q9)
print(q10)
print("---------------------------")
