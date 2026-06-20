# CS50 AI - Project 0: Degrees

# Understanding `main()` Function

## Purpose

The `main()` function is the entry point of the program.

It controls the complete workflow:

1. Load the dataset.
2. Get the source and target actors.
3. Convert names to IMDb IDs.
4. Run BFS to find the shortest connection path.
5. Display the final result.

---

# Overall Program Architecture

```text
User Input
     |
     v
main()
     |
     v
load_data()
     |
     v
Build Graph
(people, movies, names)
     |
     v
person_id_for_name()
     |
     v
Source ID & Target ID
     |
     v
shortest_path()
(BFS Search)
     |
     v
Shortest Path
     |
     v
Print Human-Readable Result
```

---

# Step 1: Handle Command-Line Arguments

```python
if len(sys.argv) > 2:
    sys.exit("Usage: python degrees.py [directory]")

directory = sys.argv[1] if len(sys.argv) == 2 else "large"
```

## Purpose

Determine which dataset should be loaded.

Examples:

```bash
python degrees.py small
```

Load:

```text
small/
```

or:

```bash
python degrees.py
```

Load the default dataset:

```text
large/
```

---

# Step 2: Load CSV Data into Memory

```python
print("Loading data...")
load_data(directory)
print("Data loaded.")
```

## Purpose

Read CSV files and build the graph.

After loading:

```text
people
   |
   |-- movies acted by a person

movies
   |
   |-- actors starring in a movie

names
   |
   |-- mapping name to IMDb IDs
```

The graph becomes:

```text
Actor
  |
Movie
  |
Actor
```

---

# Step 3: Get Source and Target Actors

```python
source = person_id_for_name(input("Name: "))
target = person_id_for_name(input("Name: "))
```

## Purpose

Convert human-readable names into unique IMDb IDs.

Example:

```text
Input:
Kevin Bacon
Tom Cruise
```

Conversion:

```text
Kevin Bacon -> 102
Tom Cruise  -> 129
```

---

# Step 4: Validate User Input

```python
if source is None:
    sys.exit("Person not found.")

if target is None:
    sys.exit("Person not found.")
```

## Purpose

Terminate the program if the actor does not exist.

Example:

```text
Input:
Unknown Actor
```

Output:

```text
Person not found.
```

---

# Step 5: Run BFS Shortest Path Search

```python
path = shortest_path(source, target)
```

## Purpose

Use Breadth-First Search (BFS) to find the minimum number of movie connections between two actors.

BFS explores:

```text
1 movie connection
       |
2 movie connections
       |
3 movie connections
       |
...
```

Therefore:

```text
First path found = Shortest path
```

---

# Step 6: Handle No Connection

```python
if path is None:
    print("Not connected.")
```

## Purpose

No possible path exists between the two actors.

Example:

```text
Actor A      Actor B
   X            X
No shared movie chain
```

---

# Step 7: Calculate Degrees of Separation

```python
degrees = len(path)
```

## Meaning

Each tuple:

```python
(movie_id, person_id)
```

represents one movie connection.

Example:

```python
path = [
    ("104257", "129"),
    ("567890", "456")
]
```

Result:

```text
2 degrees of separation
```

---

# Step 8: Add Source Node to the Path

```python
path = [(None, source)] + path
```

## Why?

The original BFS result does not include the starting actor.

Example:

Before:

```text
[
(Movie 1, Actor B),
(Movie 2, Actor C)
]
```

After:

```text
[
(None, Actor A),
(Movie 1, Actor B),
(Movie 2, Actor C)
]
```

This makes it possible to print the full chain.

---

# Step 9: Convert IDs Back to Human-Readable Information

```python
for i in range(degrees):
    person1 = people[path[i][1]]["name"]
    person2 = people[path[i + 1][1]]["name"]
    movie = movies[path[i + 1][0]]["title"]
```

## Purpose

Translate IDs into real actor and movie names.

Example:

Internal representation:

```text
102 -> 129 through 104257
```

Converted to:

```text
Kevin Bacon and Tom Cruise starred in A Few Good Men
```

---

# Step 10: Display Final Result

```python
print(f"{i + 1}: {person1} and {person2} starred in {movie}")
```

Example output:

```text
1: Kevin Bacon and Tom Cruise starred in A Few Good Men
2: Tom Cruise and Actor X starred in Mission Impossible
```

---

# Software Design Perspective

The program follows a layered architecture:

```text
Presentation Layer
        |
        v
main()
(User interaction and output)
        |
        v
Business Logic Layer
        |
        v
shortest_path()
(BFS graph search)
        |
        v
Data Access Layer
        |
        v
load_data()
(CSV parsing and graph construction)
```

This separation makes the system easier to maintain and extend.

---

# Time Complexity

The `main()` function itself performs only simple operations.

The main computational cost comes from:

```text
shortest_path()
```

which uses BFS.

Complexity:

```text
Time:  O(V + E)

Space: O(V)
```

Where:

- `V` = number of actors (vertices)
- `E` = number of actor-movie relationships (edges)

---

# Key Takeaway

`main()` acts as the controller of the entire Degrees system. It manages user input, loads the actor-movie graph, converts names to IDs, invokes BFS to compute the shortest connection path, and finally translates the internal IDs back into human-readable movie relationships.