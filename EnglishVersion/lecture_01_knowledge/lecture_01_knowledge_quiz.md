
# Quiz 1 — Logic (English)

---

## 🧠 Overview
Quizzes are optional but encouraged. They help test conceptual understanding before programming projects.

---

# Question 1 — Logical Entailment

Consider:

1. If Hermione is in the library, then Harry is in the library.  
2. Hermione is in the library.  
3. Ron is in the library AND Ron is NOT in the library.  
4. Harry is in the library.  
5. Harry is not in the library OR Hermione is in the library.  
6. Ron is in the library OR Hermione is in the library.

---

## ❓ Which entailment is true?

- Sentence 6 entails Sentence 2  
- Sentence 1 entails Sentence 4  
- Sentence 6 entails Sentence 3  
- Sentence 2 entails Sentence 5  
- Sentence 1 entails Sentence 2  
- Sentence 5 entails Sentence 6  

---

## ✅ Answer
<span style="background-color:#fff3b0"><b>Sentence 2 entails Sentence 5</b></span>

---

## why?
✅️ Sentence 2 entails Sentence 5
- Sentence 2 states that Hermione is in the library, so the statement "Harry is not in the library OR Hermione is in the library" (Sentence 5) must also be true because an OR statement is true if at least one of its conditions is true.

❌ Sentence 6 entails Sentence 2
- False, because "Ron or Hermione" being true does not guarantee that Hermione is true.

❌ Sentence 1 entails Sentence 4

- False, because an implication alone ("If Hermione, then Harry") does not prove Harry is actually in the library.

❌ Sentence 6 entails Sentence 3

- False, because an OR statement cannot imply a contradiction ("Ron and not Ron").

❌ Sentence 1 entails Sentence 2

- False, because knowing "If Hermione, then Harry" does not prove Hermione is in the library.

❌ Sentence 5 entails Sentence 6

- False, because "Harry not in the library OR Hermione in the library" provides no information about Ron.


---


# Question 2 — XOR Logic

“Exclusive Or” (represented using the symbol ⊕)

A ⊕ B means: **A or B, but not both**

![alt text](<picture/截屏2026-07-01 21.44.14.png>)

---

## ❓ Which is equivalent?

Correct form:

<span style="background-color:#fff3b0"><b>(A ∨ B) ∧ ¬(A ∧ B)</b></span>

---
## why？
✅️ (A ∨ B) ∧ ¬(A ∧ B)
- Exclusive OR (XOR) means that exactly one of A or B is true. Therefore, the statement must satisfy two conditions: at least one is true (A∨B), and they cannot both be true ¬(A∧B). Combining these conditions gives (A∨B)∧¬(A∧B), which is logically equivalent to A⊕B.

❌ (A∧B)∨¬(A∨B)

- This is true only when both are true or both are false (logical equivalence/XNOR), not XOR.

❌ (A∨B)∧(A∧B)

- This simplifies to A∧B, meaning both A and B must be true.

❌ (A∨B)∧¬(A∨B)

- A statement and its negation cannot both be true, so this expression is always false.

---



# Question 3 — Propositional Logic

Let:
- R = It is raining
- C = It is cloudy
- S = It is sunny

---

## ❓ Translate:

“If it is raining, then it is cloudy and not sunny”

---

## ✅ Answer

<span style="background-color:#fff3b0"><b>R → (C ∧ ¬S)</b></span>

---

# Question 4 — First Order Logic

![alt text](<picture/截屏2026-07-01 21.49.58.png>)

Predicate definitions:
- Student(x): x is a student  
- Course(x): x is a course  
- Enrolled(x, y): x enrolled in y  

---

## ❓ Translate:

“There is a course that Harry and Hermione are both enrolled in”

---

## ✅ Answer

<span style="background-color:#fff3b0"><b>∃x Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)</b></span>

---
## why?
✅ The sentence says that there exists at least one course that both Harry and Hermione are enrolled in. Therefore, we use the existential quantifier (∃x) to represent "there exists a course," require x to be a course (Course(x)), and use AND (∧) to state that both Harry and Hermione are enrolled in the same course x.

Why the Other Options Are Wrong?

❌ ∀x. Course(x)∧Enrolled(Harry,x)∧Enrolled(Hermione,x)

This means Harry and Hermione are enrolled in every course, not just one course.

❌ ∃x. Enrolled(Harry,x)∧∃y. Enrolled(Hermione,y)

This only says Harry and Hermione are each enrolled in some course, but the courses could be different.

❌ ∀x. Enrolled(Harry,x)∧∀y. Enrolled(Hermione,y)

This means Harry is enrolled in every course and Hermione is enrolled in every course, which is much stronger than the original statement.

❌ ∃x. Enrolled(Harry,x)∨Enrolled(Hermione,x)

This means at least one of them is enrolled in some course, not that both are enrolled in the same course.

❌ ∀x. Enrolled(Harry,x)∨Enrolled(Hermione,x)

This means that for every course, at least one of them is enrolled, which is not what the sentence states.

---

# 🧠 Summary
Logic questions test:
- entailment reasoning
- boolean equivalences
- implication translation
- first-order logic quantifiers
