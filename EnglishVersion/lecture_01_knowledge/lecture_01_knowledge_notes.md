
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

### 🧪 Example (Harry Potter Logic)

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

### 📖 Sentence

A sentence is an assertion about the world in a knowledge representation language.  
AI uses sentences to store knowledge and infer new information.

---

## 2.  🧮 Propositional Logic

Propositional logic consists of statements that are either **true or false**.

### 🔤 Propositional Symbols
Common symbols: P, Q, R

They represent propositions about the world.

---

### 🔗 Logical Connectives

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

Implication (→) represents a structure of “if P then Q.” For example, if P: “It is raining” and Q: “I’m indoors”, then P → Q means “If it is raining, then I’m indoors.” In the case of P implies Q (P → Q), P is called the antecedent and Q is called the consequent.

- False only when P is true and Q is false
- Otherwise true (trivially true if P is false)

| P | Q | P → Q |
|---|---|------|
| F | F | T |
| F | T | T |
| T | F | F |
| T | T | T |

The example:

When the antecedent is true, the whole implication is true in the case that the consequent is true (that makes sense: if it is raining and I’m indoors, then the sentence “if it is raining, then I’m indoors” is true). When the antecedent is true, the implication is false if the consequent is false (if I’m outside while it is raining, then the sentence “If it is raining, then I’m indoors” is false). However, when the antecedent is false, the implication is always true, regardless of the consequent. This can sometimes be a confusing concept. Logically, we can’t learn anything from an implication (P → Q) if the antecedent (P) is false. Looking at our example, if it is not raining, the implication doesn’t say anything about whether I’m indoors or not.

I could be an indoors type and never walk outside, even when it is not raining, or I could be an outdoors type and be outside all the time when it is not raining.

When the antecedent is false, we say that the implication istrivially true.

---

### BICONDITIONAL (↔)

Biconditional (↔) is an implication that goes both directions. You can read it as “if and only if.” P ↔ Q is the same as P → Q and Q → P taken together. For example, if P: “It is raining.” and Q: “I’m indoors,” then P ↔ Q means that “If it is raining, then I’m indoors,” and “if I’m indoors, then it is raining.” This means that we can infer more than we could with a simple implication. If P is false, then Q is also false; if it is not raining, we know that I’m also not indoors.

P ↔ Q means both directions:

P → Q AND Q → P

| P | Q | P ↔ Q |
|---|---|------|
| F | F | T |
| F | T | F |
| T | F | F |
| T | T | T |

---

### 🧠 Model

A model is an assignment of truth values to propositions.

- The model is an assignment of a truth value to every proposition. To reiterate, propositions are statements about the world that can be either true or false. However, knowledge about the world is represented in the truth values of these propositions.


Example:
- P = True (It is raining)
- Q = False (It is Tuesday)

Total models = 2ⁿ (n = number of propositions)

For example, if P: “It is raining.” and Q: “It is Tuesday.”, a model could be the following truth-value assignment: {P = True, Q = False}. This model means that it is raining, but it is not Tuesday.

However, there are more possible models in this situation (for example, {P = True, Q = True}, where it is both raining and a Tuesday). In fact, the number of possible models is 2 to the power of the number of propositions.

In this case, we had 2 propositions, so 2²=4 possible models.

---

### 📚 Knowledge Base (KB)

A knowledge base is a set of sentences known to the AI agent.

Used to make logical inferences.

- The knowledge base is a set of sentences known by a knowledge-based agent. This is knowledge that the AI is provided about the world in the form of propositional logic sentences that can be used to make additional inferences about the world.

---

### 📌 Entailment (⊨)

α ⊨ β means:
> In every model where α is true, β is also true.

- For example, if α: “It is a Tuesday in January” and β: “It is January,” then we know that α ⊨ β. If it is true that it is a Tuesday in January, we also know that it is January. Entailment is different from implication. Implication is a logical connective between two propositions.
- Entailment, on the other hand, is a relation that means that if all the information in α is true, then all the information in β is true.
  
---

## 3. 🔍 Inference

Inference is the process of deriving new sentences from old ones.

In the Harry Potter example earlier, sentences 4 and 5 are derived from sentences 1, 2, and 3.

There are multiple ways to infer new knowledge based on existing knowledge. First, we will consider the Model Checking algorithm.

---

### 🔍 Model Checking Algorithm

To determine whether **KB ⊨ α** (in other words, answering the question: “can we conclude that α is true based on our knowledge base”):

- Enumerate all possible models
- If in every model where KB is true, α is also true
- Then KB entails α

---

### 📌 Example Setup

- P: It is a Tuesday  
- Q: It is raining  
- R: Harry will go for a run  

KB:
> (P ∧ ¬Q) → R   
>Query: R   
>(We want to know whether R is true or false; Does KB ⊨ R?)

>(in words, P and not Q imply R) 
 P (P is true) ¬Q (Q is false)

To answer the query using the Model Checking algorithm, We enumerate all possible models:

| P | Q | R |
|---|---|---|
| F | F | F |
| F | F | T |
| F | T | F |
| F | T | T |
| T | F | F |
| T | F | T |
| T | T | F |
| T | T | T |

Then, we go through every model and check whether it is true given our Knowledge Base.

---

### 🧾 Applying KB constraints

#### Step 1: P is true in KB
So all models where P is false are invalid. Thus, we can say that the KB is false in all models where P is not true.

---

#### Step 2: Q is false in KB
In our KB, we know that Q is false. Thus, we can say that the KB is false in all models where Q is true.

Remaining models:

- P = True
- Q = False
- R = {True, False}

---

#### Step 3: Apply rule (P ∧ ¬Q → R)

- Due to (P ∧ ¬Q) → R being in our KB, we know that in the case where P is true and Q is false, R must be true.

- Only models where R is true satisfy KB.

---

### 📌 Final conclusion

Only one model satisfies KB:
- P = True
- Q = False
- R = True

So:

<span style="background-color:#fff3b0"><b>KB ⊨ R</b></span>

---

### 💻 Code Representation

```python
from logic import *

# Create new classes, each having a name, or a symbol, representing each proposition.
rain = Symbol("rain")  # It is raining.
hagrid = Symbol("hagrid")  # Harry visited Hagrid
dumbledore = Symbol("dumbledore")  # Harry visited Dumbledore

# Save sentences into the KB
knowledge = And(  # Starting from the "And" logical connective, becasue each proposition represents knowledge that we know to be true.

    Implication(Not(rain), hagrid),  # ¬(It is raining) → (Harry visited Hagrid)

    Or(hagrid, dumbledore),  # (Harry visited Hagrid) ∨ (Harry visited Dumbledore).

    Not(And(hagrid, dumbledore)),  # ¬(Harry visited Hagrid ∧ Harry visited Dumbledore) i.e. Harry did not visit both Hagrid and Dumbledore.

    dumbledore  # Harry visited Dumbledore. Note that while previous propositions contained multiple symbols with connectors, this is a proposition consisting of one symbol. This means that we take as a fact that, in this KB, Harry visited Dumbledore.
    )
```

---


To run the Model Checking algorithm, the following information is needed:

- Knowledge Base, which will be used to draw inferences
- A query, or the proposition that we are interested in whether it is entailed by the KB
- Symbols, a list of all the symbols (or atomic propositions) used (in our case, these are rain, hagrid, and dumbledore)
- Model, an assignment of truth and false values to symbols

The model checking algorithm looks as follows:

### 🔁 Model Checking Function

```python
def check_all(knowledge, query, symbols, model):

    # If model has an assignment for each symbol
    # (The logic below might be a little confusing: we start with a list of symbols. The function is recursive, and every time it calls itself it pops one symbol from the symbols list and generates models from it. Thus, when the symbols list is empty, we know that we finished generating models with every possible truth assignment of symbols.)
    if not symbols:

        # If knowledge base is true in model, then query must also be true
        if knowledge.evaluate(model):
            return query.evaluate(model)
        return True
    else:

        # Choose one of the remaining unused symbols
        remaining = symbols.copy()
        p = remaining.pop()

        # Create a model where the symbol is true
        model_true = model.copy()
        model_true[p] = True

        # Create a model where the symbol is false
        model_false = model.copy()
        model_false[p] = False

        # Ensure entailment holds in both models
        return(check_all(knowledge, query, remaining, model_true) and check_all(knowledge, query, remaining, model_false))
```

---

### ⚠️ Key Insight

We only care about models where KB is true.
- Note that we are interested only in the models where the KB is true. If the KB is false, then the conditions that we know to be true are not occurring in these models, making them irrelevant to our case.

an example:

Let P: Harry plays seeker, Q: Oliver plays keeper, R: Gryffindor wins. Our KB specifies that P Q (P ∧ Q) → R. In other words, we know that P is true, i.e. Harry plays seeker, and that Q is true, i.e. Oliver plays keeper, and that if both P and Q are true, then R is true, too, meaning that Gryffindor wins the match. 

Now imagine a model where Harry played beater instead of seeker (thus, Harry did not play seeker, ¬P). Well, in this case, we don’t care whether Gryffindor won (whether R is true or not), because we have the information in our KB that Harry played seeker and not beater. We are only interested in the models where, as in our case, P and Q are true.)

an notes:

Further, the way the check_all function works is recursive. That is, it picks one symbol, creates two models, in one of which the symbol is true and in the other the symbol is false, and then calls itself again, now with two models that differ by the truth assignment of this symbol.

The function will keep doing so until all symbols will have been assigned truth-values in the models, leaving the listsymbols empty. Once it is empty (as identified by the line if not symbols), in each instance of the function (wherein each instance holds a different model), the function checks whether the KB is true given the model. If the KB is true in this model, the function checks whether the query is true, as described earlier.

---

### 🎯 Summary

<span style="background-color:#fff3b0"><b>Inference = reasoning by checking all possible models consistent with knowledge.</b></span>

## 4. 🧠 Knowledge Engineering

Knowledge engineering is the process of figuring out how to represent propositions and logic in AI.

We practice it using the game **Clue**.

---

### 🎮 Clue Game Model

In the game:
- A murder is committed by a **person**
- Using a **tool**
- In a **location**

Cards represent:
- People
- Tools
- Locations

One card from each category is placed in an envelope.

We will use the Model Checking algorithm from before to uncover the mystery.

In our model, we mark as **True** items that we know are related to the murder and **False** otherwise.

### Goal:
Determine **who did it, with what tool, and where**.

---

### 📌 Modeling Assumption

We mark:
- <mark>True</mark> → related to murder
- <mark>False</mark> → not related

---

### 👥 Example Setup

People:
- Mustard
- Plum
- Scarlet

Tools:
- Knife
- Revolver
- Wrench

Locations:
- Ballroom
- Kitchen
- Library

---

### 📐 Knowledge Base Rules

Exactly one from each category is true:

- (Mustard ∨ Plum ∨ Scarlet)
- (Knife ∨ Revolver ∨ Wrench)
- (Ballroom ∨ Kitchen ∨ Library)

---

### 🃏 Observed Cards

Let's start to paly together. Suppose our player gets the cards of Mustard, kitchen, and revolver.:

Player sees:
- Mustard
- Kitchen
- Revolver

So we add:

- ¬Mustard
- ¬Kitchen
- ¬Revolver

---

### 🧪 Guess Constraint

In other situations in the game, one can make a guess, suggesting one combination of person, tool and location. 

Suppose that the guess is that **Scarlet used a wrench to commit the crime in the library**. If this guess is wrong, then the following can be deduced and added to the KB:

If guess is wrong:

Scarlet + Library + Wrench

→ At least one is false:

<span style="background-color:#fff3b0"><b>(¬Scarlet ∨ ¬Library ∨ ¬Wrench)</b></span>

---

### 🧾 Additional Evidence

Now, suppose someone shows us the Plum card. Thus, we can add

If Plum card is shown:

- ¬Plum

Adding just one more piece of knowledge, for example, that it is not the ballroom, can give us more information. First, we update our KB

If not ballroom:

- ¬Ballroom

---

### 🧠 Final Deduction

Using all constraints:

We conclude:

<span style="background-color:#fff3b0"><b>Scarlet committed the murder in the library using the knife.</b></span>

Why:

We can deduce that it’s the library because it has to be either the ballroom, the kitchen, or the library, and the first two were proven to not be the locations. However, when someone guessed Scarlet, library, wrench, the guess was false.

Thus, at least one of the elements in this statement has to be false. Since we know both Scarlet and library to be true, we know that the wrench is the false part here.

Since one of the three instruments has to be true, and it’s not the wrench nor the revolver, we can conclude that it is the knife.

---

### 💻 Python Knowledge Base

Here is how the information would be added to the knowledge base in Python:

```python
# Add the clues to the KB
knowledge = And(

    # Start with the game conditions: one item in each of the three categories has to be true.
    Or(mustard, plum, scarlet),
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench),

    # Add the information from the three initial cards we saw
    Not(mustard),
    Not(kitchen),
    Not(revolver),

    # Add the guess someone made that it is Scarlet, who used a wrench in the library
    Or(Not(scarlet), Not(library), Not(wrench)),

    # Add the cards that we were exposed to
    Not(plum),
    Not(ballroom)
)
```

---

### 🧩 Other Logic Puzzles

### House Assignment Problem

- 4 people
- 4 houses

Encoding is complex:
- Each assignment becomes a proposition
- Requires many OR constraints
- Requires mutual exclusion rules

👉 This motivates **First Order Logic**

---

### 🎯 Mastermind Game

Game idea:
- Guess color order
- Receive feedback (how many correct positions)

In this game, player one arranges colors in a certain order, and then player two has to guess this order.

Each turn, player two makes a guess, and player one gives back a number, indicating how many colors player two got right. Let’s simulate a game with four colors.

Example:
- Guess → "2 correct"
- Swap → "0 correct"
- Final → "4 correct"

---

### ♟️ Play

1. Suppose player two suggests the following ordering:

![alt text](<picture/截屏2026-06-23 15.47.13.png>)

Player one answers “two.” Thus we know that some two of the colors are in the correct position, and the other two are in the wrong place. 

2. Based on this information, player two tries to switch the locations of two colors.

![alt text](<picture/截屏2026-06-23 15.47.49.png>)

Now player one answers “zero.” Thus, player two knows that the switched colors were in the right location initially, which means the untouched two colors were in the wrong location. 

3. Player two switches them.

![alt text](image.png)


Player one says “four” and the game is over.


### 🔢 Logical Encoding

For 4 colors:
- Need (number_of_colors)² propositions
- e.g. red0, red1, red2, red3, blue0… Standing for color and position

The next step is to represent the rules of the game in propositional logic
Rules:
- One color per position
- No repetition

The final step would be adding all the cues that we have to the KB.

Using this knowledge, a Model Checking algorithm can give us the solution to the puzzle.

---

### 🧠 Key Insight

<span style="background-color:#fff3b0"><b>All constraints + observations → can be solved using Model Checking</b></span>

## 4. Inference Rules


