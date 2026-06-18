# CS50 AI - Project 0: Degrees

# Understanding `person_id_for_name()` and `neighbors_for_person()`

These two helper functions provide the bridge between the dataset and the BFS search algorithm.

```text
User Input Name
       |
       v
person_id_for_name()
       |
       v
Actor ID
       |
       v
neighbors_for_person()
       |
       v
Connected Actors (Graph Neighbors)
       |
       v
BFS shortest_path()
```

---

# 1. `person_id_for_name()`

## Purpose

Convert a person's name into a unique IMDb person ID.

Since multiple actors may share the same name, the function also handles ambiguity.

---

## Function Workflow

```text
Input Name
     |
     v
Convert to lowercase
     |
     v
Search names dictionary
     |
     +----------------+
     |                |
     v                v
No match          One or multiple matches
     |                |
Return None       Return ID or ask user to choose
```

---

## Step 1: Search the `names` Dictionary

```python
person_ids = list(names.get(name.lower(), set()))
```

### Why `lower()`?

Makes the search case-insensitive.

Example:

```text
Kevin Bacon
KEVIN BACON
kevin bacon
```

All become:

```text
kevin bacon
```

---

### Why `names.get()`?

Safely searches the dictionary.

Example:

```python
names = {
    "kevin bacon": {"102"}
}
```

Search:

```python
names.get("kevin bacon", set())
```

Returns:

```python
{"102"}
```

If the name does not exist:

```python
set()
```

is returned instead of causing an error.

---

## Step 2: No Match

```python
if len(person_ids) == 0:
    return None
```

Meaning:

```text
No actor found in the database.
```

---

## Step 3: Multiple Matches

```python
elif len(person_ids) > 1:
```

Example:

```text
Chris Evans
```

could refer to multiple people.

The program prints:

```text
ID: 123, Name: Chris Evans, Birth: 1980
ID: 456, Name: Chris Evans, Birth: 1966
```

Then the user selects the correct IMDb ID.

---

## Step 4: Single Match

```python
return person_ids[0]
```

Meaning:

```text
Only one actor has this name.
```

Return the actor's ID directly.

---

# 2. `neighbors_for_person()`

## Purpose

Find all actors who have appeared in the same movie as the given person.

In graph terminology:

```text
Current Actor
       |
       |
      Movies
       |
       |
Connected Actors (Neighbors)
```

---

## Step 1: Get Movies of the Current Actor

```python
movie_ids = people[person_id]["movies"]
```

Example:

```python
people["102"]["movies"]
```

Returns:

```python
{
    "104257",
    "112384"
}
```

Meaning:

```text
This actor appeared in these movies.
```

---

## Step 2: Create an Empty Neighbor Set

```python
neighbors = set()
```

Used to store:

```python
(movie_id, person_id)
```

pairs.

Example:

```python
("104257", "129")
```

Meaning:

```text
Through movie 104257, you can reach actor 129.
```

---

## Step 3: Traverse Each Movie

```python
for movie_id in movie_ids:
```

Check every movie the actor has appeared in.

---

## Step 4: Find All Actors in Each Movie

```python
for person_id in movies[movie_id]["stars"]:
```

Example:

```python
movies["104257"]["stars"]
```

Returns:

```python
{
    "102",
    "129",
    "345"
}
```

Meaning:

```text
All actors who starred in this movie.
```

---

## Step 5: Build Neighbor Relationships

```python
neighbors.add((movie_id, person_id))
```

Final result:

```python
{
    ("104257", "129"),
    ("104257", "345"),
    ("112384", "678")
}
```

This means:

```text
Current Actor
     |
Movie 104257
     |
Actor 129

Current Actor
     |
Movie 104257
     |
Actor 345
```

---

# Relationship With BFS

The `shortest_path()` function uses:

```python
neighbors_for_person(node.state)
```

to expand the current BFS node.

Example:

```text
Current Node: Kevin Bacon
          |
          v
neighbors_for_person()
          |
          v
Tom Cruise
Actor B
Actor C
```

These neighboring actors are added into the BFS queue for future exploration.

---

# Software Architecture

The entire project follows a graph search architecture:

```text
CSV Files
    |
    v
load_data()
    |
    v
Graph Data Structures
(people, movies, names)
    |
    v
person_id_for_name()
    |
    v
Source / Target Actor ID
    |
    v
neighbors_for_person()
    |
    v
Graph Expansion
    |
    v
BFS shortest_path()
    |
    v
Shortest Actor Connection
```

---

# Time Complexity

## `person_id_for_name()`

Average complexity:

```text
O(1)
```

Because dictionary lookup in Python is based on a hash table.

---

## `neighbors_for_person()`

Complexity:

```text
O(M × S)
```

Where:

- `M` = number of movies the actor appeared in
- `S` = average number of stars in each movie

---

# Key Takeaway

`person_id_for_name()` converts a human-readable actor name into a unique IMDb ID, while `neighbors_for_person()` discovers all adjacent actors in the graph. Together, they provide the essential mapping and graph expansion operations required for BFS to find the shortest connection path between two actors.