# CS50 AI - Project 0: Degrees

# shortest_path() Deep Dive

## Objective

Implement **Breadth-First Search (BFS)** to find the shortest connection path between two actors.

Example:

```text
Kevin Bacon
    ↓ A Few Good Men
Tom Cruise
    ↓ Mission Impossible
Actor X
```

Output:

```python
[
    ("104257", "129"),
    ("567890", "456")
]
```

Each tuple:

```python
(movie_id, person_id)
```

means:

> Reach `person_id` through `movie_id`.

---

# High-Level Architecture

The search process follows:

```text
Source Actor
      │
      ▼
Queue Frontier
      │
      ▼
Expand Neighbors
      │
      ▼
Target Actor
```

This is a classic:

```text
Graph Search
+
Breadth-First Search (BFS)
```

---

# Graph Model

Actors and movies form a graph.

```text
Actor
  │
Movie
  │
Actor
```

Example:

```text
Kevin Bacon
      │
A Few Good Men
      │
Tom Cruise
```

---

# Step 1: Create Start Node

```python
start = Node(
    state=source,
    parent=None,
    action=None
)
```

## Purpose

Create the root node of the search tree.

---

### Node Structure

```python
Node(
    state,
    parent,
    action
)
```

| Field  | Meaning                           |
| ------ | --------------------------------- |
| state  | Current actor id                  |
| parent | Previous node                     |
| action | Movie used to reach current actor |

---

Example:

```python
Node(
    state="129",
    parent=node1,
    action="104257"
)
```

means:

```text
Reached Tom Cruise

through movie:
A Few Good Men (104257)

from:
Kevin Bacon (129)
```

---

# Step 2: Initialize BFS Queue

```python
frontier = QueueFrontier()
frontier.add(start)
```

---

## Why QueueFrontier?

BFS requires:

```text
FIFO
First In First Out
```

Visualization:

```text
Queue

Front ───── Back

[A]
```

Expand:

```text
[A]
 ↓

[B][C][D]
```

Process order:

```text
B → C → D
```

This guarantees:

```text
Shortest Path First
```

---

# Step 3: Initialize Explored Set

```python
explored = set()
```

Purpose:

```text
Avoid revisiting nodes
```

Without it:

```text
A → B → A → B → A
```

Infinite loop.

---

Example:

```python
explored = {
    "102",
    "129",
    "456"
}
```

---

# Step 4: BFS Main Loop

```python
while True:
```

Continue searching until:

```text
Target found
OR
No path exists
```

---

# Step 5: Check Frontier Empty

```python
if frontier.empty():
    return None
```

Meaning:

```text
No nodes left to explore
```

Graph example:

```text
Source

     X

Target
```

No connection.

Return:

```python
None
```

---

# Step 6: Remove Node From Queue

```python
node = frontier.remove()
```

BFS always removes:

```text
Oldest node
```

Visualization:

```text
Queue

[A][B][C]

remove()

[B][C]
```

---

# Step 7: Goal Test

```python
if node.state == target:
```

Check:

```text
Have we reached target actor?
```

If yes:

```python
return path
```

---

# Step 8: Path Reconstruction

This is the most important part.

```python
path = []

while node.parent is not None:
    path.append(
        (node.action, node.state)
    )
    node = node.parent
```

---

## Example Search Tree

```text
Kevin Bacon
      │
Movie 1
      │
Tom Cruise
      │
Movie 2
      │
Brad Pitt
```

Parent chain:

```text
Brad Pitt
     ↑
Tom Cruise
     ↑
Kevin Bacon
```

---

### Backtracking

First iteration:

```python
(Movie2, Brad Pitt)
```

Second iteration:

```python
(Movie1, Tom Cruise)
```

Result:

```python
[
    (Movie2, Brad Pitt),
    (Movie1, Tom Cruise)
]
```

Wrong order.

---

### Reverse Path

```python
path.reverse()
```

Result:

```python
[
    (Movie1, Tom Cruise),
    (Movie2, Brad Pitt)
]
```

Correct path:

```text
Kevin Bacon
→ Tom Cruise
→ Brad Pitt
```

---

# Step 9: Mark Current Node Explored

```python
explored.add(node.state)
```

Purpose:

```text
Never visit this actor again
```

---

# Step 10: Expand Neighbors

```python
for movie_id, person_id in neighbors_for_person(node.state):
```

Example:

```python
neighbors_for_person("102")
```

returns:

```python
{
    ("104257", "129"),
    ("104257", "345"),
    ("104257", "678")
}
```

Meaning:

```text
Kevin Bacon acted with:

Tom Cruise
Actor 345
Actor 678
```

---

# Step 11: Avoid Duplicate Visits

```python
if (
    not frontier.contains_state(person_id)
    and person_id not in explored
):
```

Requirements:

```text
Not already in queue
AND
Not already explored
```

Without this check:

```text
Same actor added repeatedly
```

causing:

```text
Huge memory usage
Slow search
Infinite loops
```

---

# Step 12: Create Child Node

```python
child = Node(
    state=person_id,
    parent=node,
    action=movie_id
)
```

Example:

```python
Node(
    state="129",
    parent=KevinNode,
    action="104257"
)
```

Meaning:

```text
Reached Tom Cruise

from Kevin Bacon

through A Few Good Men
```

---

# Step 13: Add Child To Queue

```python
frontier.add(child)
```

Queue becomes:

```text
[B]
 ↓

[B][C][D]
```

Ready for future exploration.

---

# Why BFS Guarantees Shortest Path

BFS explores:

```text
Distance 1
Distance 2
Distance 3
...
```

Therefore:

```text
First time target is found
=
Shortest path
```

Unlike DFS:

```text
DFS may go very deep
before finding target
```

and may return a longer path.

---

# Time Complexity

Let:

```text
V = number of actors
E = number of actor-movie connections
```

Complexity:

```text
Time:  O(V + E)

Space: O(V)
```

This is optimal for an unweighted graph shortest-path problem.

---

# Key Takeaway

The `shortest_path()` function models actors and movies as a graph and uses **Breadth-First Search (BFS)** with a queue, explored set, and parent pointers to guarantee finding the shortest connection path between two actors.
