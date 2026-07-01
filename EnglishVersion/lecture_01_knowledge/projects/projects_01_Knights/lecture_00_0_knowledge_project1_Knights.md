
# 🧠 Knights — Logic Puzzles (CS50 AI)

---

## ⚠️ System Requirement
> <span style="background-color:#fff3b0"><b>The latest version of Python you should use in this course is Python 3.12.</b></span>

---

## 📌 Task
Write a program to solve logic puzzles.

---

# 📚 Background

In 1978, logician **Raymond Smullyan** published *“What is the Name of This Book?”*, a collection of logic puzzles.

A famous class of puzzles in this book is called:

> 🧩 **Knights and Knaves**

---

## Rules
Each character is either:
- 🛡️ Knight → always tells the truth  
- 🗡️ Knave → always lies  

If a knight says something → it is TRUE  
If a knave says something → it is FALSE  

---

## Objective
Given statements, determine:
> 🧠 who is a knight and who is a knave

---

## Example Puzzle

A says:
> “I am both a knight and a knave.”

This is impossible → so:
<span style="background-color:#fff3b0"><b>A must be a knave</b></span>

---

# 🚀 Getting Started

Download:
https://cdn.cs50.net/ai/2023/x/projects/1/knights.zip

---

# 🧠 Understanding

## logic.py
Defines logical connectives like:
- And
- Or
- Not

Example:
`And(Not(A), Or(B, C))`

means:
- A is false
- B or C is true

---

## model_check
Function:
> model_check(knowledge_base, query)

It:
- checks ALL possible models
- returns True if KB entails query
- otherwise False

---

## puzzle.py
Defines symbols:
- AKnight → A is knight
- AKnave → A is knave
(similar for B and C)

Also defines:
- knowledge0
- knowledge1
- knowledge2
- knowledge3

Your task:
👉 fill them in

---

# 📌 Specification

## Puzzle 0
A says:
> “I am both a knight and a knave.”

---

## Puzzle 1
A and B:
- A: “We are both knaves”
- B says nothing

---

## Puzzle 2
A and B:
- A: “We are the same kind”
- B: “We are different kinds”

---

## Puzzle 3
A, B, C:
- A says either:
  - “I am a knight”
  - “I am a knave”
- B says:
  - “A said I am a knave”
  - “C is a knave”
- C says:
  - “A is a knight”

---

# 💡 Hints

- Encode BOTH:
  1. rules of knights/knaves
  2. what characters say

- Do NOT manually solve puzzles

- Goal: let AI (model checking) solve it

---

## Important Idea
> <span style="background-color:#fff3b0"><b>Truth depends on who is speaking</b></span>

