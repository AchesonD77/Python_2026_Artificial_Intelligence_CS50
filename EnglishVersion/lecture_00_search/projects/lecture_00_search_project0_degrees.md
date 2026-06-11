
# CS50 AI — Degrees Project

---

## 📌 Overview

<span style="background-color: #fff3b0">**The latest version of Python required is Python 3.12**</span>

Write a program that determines how many **degrees of separation** apart two actors are.

Example run:

```bash
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

---

## 🎬 Background

According to the *Six Degrees of Kevin Bacon* game, anyone in Hollywood can be connected to Kevin Bacon within six steps.



In this problem, we find the **shortest path between two actors** by connecting them through movies.

For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.

We can frame this as a search problem: our states are people. Our actions are movies, which take us from one actor to another (it’s true that a movie could take us to multiple different actors, but that’s okay for this problem).

Our initial state and goal state are defined by the two people we’re trying to connect. By using breadth-first search, we can find the shortest path from one actor to another.

We use **BFS (Breadth-First Search)** because it guarantees the shortest path in an unweighted graph.

---

## 🚀 Getting Started

Here i already uploaded on this page: [degrees.zip](degrees.zip)

you can also Download the distribution code from official website:

```text
https://cdn.cs50.net/ai/2023/x/projects/0/degrees.zip
```

Unzip it to begin.

---

## 📂 Understanding the Data

The distribution code contains two sets of CSV data files: one set in the large directory and one set in the small directory. Each contains files with the same names, and the same structure, but small is a much smaller dataset for ease of testing and experimentation.

Two datasets exist:

- `large/` dataset
- `small/` dataset (for testing)

Each dataset consists of three CSV files. A CSV file, if unfamiliar, is just a way of organizing data in a text-based format: each row corresponds to one data entry, with commas in the row separating the values for that entry.

Each contains CSV files (we open up the small dataset) [small](small):

### people.csv
- id
- name
- birth

### movies.csv
- id
- title
- year

### stars.csv (This file establishes a relationship between the people in people.csv and the movies in movies.csv. Each row is a pair of a person_id value and movie_id value. )
- person_id
- movie_id

---

## 🧠 Program Structure (degrees.py) [degrees.py](degrees.py)

Data structures used:

they are dictionaries:
- `names`: map name → set of person IDs
- `people`: map person_id → another ditc: {name, birth, movies}
- `movies`: map movie_id → another dict: {title, year, stars}

### Loading Data
Function: `load_data(directory)`

Loads CSV data into memory.

### Main Function Flow
- Prompt user for two names
- Convert names → IDs using `person_id_for_name`
- Call `shortest_path(source, target)`
- Print result path

```text
The shortest_path function, however, is left unimplemented. That’s where you come in!
```
---

## ⚙️ Specification

Implement:

```python
shortest_path(source, target)
```

### Requirements:

- Return list of `(movie_id, person_id)` pairs
- Each pair represents a step in the connection
- If multiple shortest paths exist → return any one
- If no path exists → return `None`

You may use:

```python
neighbors_for_person(person_id)
```

---

## 💡 Key Constraint

<span style="background-color: #fff3b0">Do NOT modify anything except `shortest_path`</span>

---

## 🧪 Hints

- Goal test can be done when node is:
  - popped from frontier OR
  - added to frontier
- Provided utilities:
  - `Node`
  - `StackFrontier`
  - `QueueFrontier`

---

## 🧪 Testing

Run correctness tests:

```bash
check50 ai50/projects/2024/x/degrees
```

Style check:

```bash
style50 degrees.py
```

---

## 📤 Submission

### Method 1: submit50

```bash
submit50 ai50/projects/2024/x/degrees
```

### Method 2: GitHub

```text
https://github.com/me50/USERNAME.git
branch: ai50/projects/2024/x/degrees
```

---

## ⚠️ Important Warning

<span style="background-color: #ffcccc">Do NOT include `large` or `small` directories when submitting</span>

---

## 🙏 Acknowledgements

Data provided by **IMDb**

---
