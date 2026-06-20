
# Lecture 1 — Knowledge (CS50 AI)

---

## 📌 Overview

<span style="background-color:#fff3b0"><b>Knowledge in AI (Lecture 1)</b></span>

Humans reason based on existing knowledge and draw conclusions.  
This lecture explores how AI can represent knowledge and use it to infer new information.

---

## 1.  🧠 Knowledge-Based Agents

Knowledge-based agents are systems that reason by operating on **internal representations of knowledge**.

### ❓ Core Question
What does *“reasoning based on knowledge to draw conclusions”* mean?

---

## 🧪 Example (Harry Potter Logic)

Consider the following statements:

1. If it didn’t rain, Harry visited Hagrid today.  
2. Harry visited Hagrid or Dumbledore today, but not both.  
3. Harry visited Dumbledore today.  

From these, we can infer:

- From (3): Harry visited Dumbledore  
- From (2): Therefore, Harry did NOT visit Hagrid  
- From (1): Therefore, it must have rained  

### ✅ Final Conclusion:
<span style="background-color:#fff3b0"><b>It rained today.</b></span>

To come to this conclusion, we used logic, and today’s lecture explores how AI can use logic to reach to new conclusions based on existing information.

---

## 📖 Sentence

A sentence is an assertion about the world in a knowledge representation language.  
AI uses sentences to store knowledge and infer new information.

---

## 2.  🧮 Propositional Logic

Propositional logic consists of statements that are either **true or false**.

### 🔤 Propositional Symbols
Common symbols: P, Q, R

They represent propositions about the world.

---

## 🔗 Logical Connectives

Logical connectives are logical symbols that connect propositional symbols in order to reason in a more complex way about the world.

### NOT (¬)
- Inverts truth value  
- If P: “It is raining” → ¬P: “It is not raining”

Truth tables are used to compare all possible truth assignments to propositions. This tool will help us better understand the truth values of propositions when connected with different logical connectives. For example, below is our first truth table:

Truth table:

| P | ¬P |
|---|---|
| F | T |
| T | F |

---

### AND (∧)

P ∧ Q is true only if BOTH are true.

| P | Q | P ∧ Q |
|---|---|------|
| F | F | F |
| F | T | F |
| T | F | F |
| T | T | T |

---

### OR (∨)

True if at least one is true.

| P | Q | P ∨ Q |
|---|---|------|
| F | F | F |
| F | T | T |
| T | F | T |
| T | T | T |

- Inclusive OR is used in AI
- Exclusive OR (XOR) requires only one true

It is worthwhile to mention that there are two types of Or: an inclusive Or and an exclusive Or. In an exclusive Or, P ∨ Q is false if P ∧ Q is true. That is, an exclusive Or requires only one of its arguments to be true and not both.

An inclusive Or is true if any of P, Q, or P ∧ Q is true. In the case of Or (∨), the intention is an inclusive Or.

A couple of side notes not mentioned in lecture:

```
- Sometimes an example helps understand inclusive versus exclusive Or. Inclusive Or: “in order to eat dessert, you have to clean your room or mow the lawn.” In this case, if you do both chores, you will still get the cookies.

- Exclusive Or: “For dessert, you can have either cookies or ice cream.” In this case, you can’t have both.

- If you are curious, the exclusive Or is often shortened to XOR and a common symbol for it is ⊕).
```
---

### IMPLICATION (→)

P → Q means “if P then Q”

- False only when P is true and Q is false
- Otherwise true (trivially true if P is false)

| P | Q | P → Q |
|---|---|------|
| F | F | T |
| F | T | T |
| T | F | F |
| T | T | T |

---

### BICONDITIONAL (↔)

P ↔ Q means both directions:

P → Q AND Q → P

| P | Q | P ↔ Q |
|---|---|------|
| F | F | T |
| F | T | F |
| T | F | F |
| T | T | T |

---

## 🧠 Model

A model is an assignment of truth values to propositions.

Example:
- P = True (It is raining)
- Q = False (It is Tuesday)

Total models = 2ⁿ (n = number of propositions)

---

## 📚 Knowledge Base (KB)

A knowledge base is a set of sentences known to the AI agent.

Used to make logical inferences.

---

## 📌 Entailment (⊨)

α ⊨ β means:
> In every model where α is true, β is also true.

---

## 🔍 Inference

Inference is the process of deriving new knowledge from old knowledge.

---

## 🧪 Model Checking Algorithm

To check KB ⊨ α:

1. Enumerate all possible models  
2. Check if α is true in all models where KB is true  

---

## 🧾 Code Representation

```python
from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)
```

---

## 🔁 Recursive Model Checking

Algorithm idea:

- Assign truth values recursively
- Try all combinations
- Check KB validity
- Verify query truth

---

## ⚠️ Key Insight

We only consider models where KB is true.

---

## 🎯 Summary

<span style="background-color:#fff3b0"><b>Logic enables AI to derive new conclusions from known facts using formal reasoning systems.</b></span>

---
