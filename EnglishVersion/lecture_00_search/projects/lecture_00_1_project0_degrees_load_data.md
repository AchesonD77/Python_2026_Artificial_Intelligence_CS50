### Project Goal
Find the **shortest connection path** between two actors using their shared movie appearances.

Example:
```text
Kevin Bacon
    ↓ A Few Good Men
Tom Cruise
    ↓ Mission Impossible
Actor X
```

The project models actors and movies as a **Graph** and uses **Breadth-First Search (BFS)** to find the shortest path.

---

### Data Files

The dataset contains three CSV files:

## people.csv

Stores actor information.

```csv
id,name,birth
102,Kevin Bacon,1958
129,Tom Cruise,1962
```

Loaded into:

```python
people = {
    "102": {
        "name": "Kevin Bacon",
        "birth": "1958",
        "movies": set()
    }
}
```

---

## movies.csv

Stores movie information.

```csv
id,title,year
104257,A Few Good Men,1992
```

Loaded into:

```python
movies = {
    "104257": {
        "title": "A Few Good Men",
        "year": "1992",
        "stars": set()
    }
}
```

---

## stars.csv

Stores actor-movie relationships.

```csv
person_id,movie_id
102,104257
129,104257
```

Meaning:

```text
Kevin Bacon ── A Few Good Men ── Tom Cruise
```

---

### Core Data Structures

#### names

Maps actor names to IDs.

```python
names = {
    "kevin bacon": {"102"}
}
```

Purpose:

- Fast actor lookup
- Handle duplicate names

---

#### people

Maps actor IDs to actor information.

```python
people = {
    "102": {
        "name": "Kevin Bacon",
        "birth": "1958",
        "movies": {"104257"}
    }
}
```

---

#### movies

Maps movie IDs to movie information.

```python
movies = {
    "104257": {
        "title": "A Few Good Men",
        "year": "1992",
        "stars": {"102", "129"}
    }
}
```

---

# 💻 For the code

## Understanding `load_data()`

## Define function:

```python
def load_data(directory):

  # This function loads all CSV files into memory and builds relationships between people and movies.
```
Example: load_data("small") will read files:

small/people.csv

small/movies.csv

small/stars.csv

## Step 1: Load People
```python
with open(f"{directory}/people.csv", encoding="utf-8") as f:
# Open the people.csv file

  reader = csv.DictReader(f) # Convert each row into a dictionary.
  # Instead of: ["102", "Kevin Bacon", "1958"]
  # we get:
  # {
  #  "id": "102",
  #  "name": "Kevin Bacon",
  #  "birth": "1958"
  #  }

  # Each iteration processes one person.
  for row in reader:
    # Building the people Dictionary
    people[row["id"]] = {
        "name": row["name"],
        "birth": row["birth"],
        "movies": set()
    }
    # 3. Building the names Dictionary
    if row["name"].lower() not in names:
    """
    Purpose
    Check whether this name already exists.
    Example:
    "Kevin Bacon".lower()
    becomes
    "kevin bacon"
    Using lowercase avoids:
    Kevin Bacon
    KEVIN BACON
    kevin bacon
    being treated as different names.
    """
    #First Time Seeing This Name
      names[row["name"].lower()] = {row["id"]}
      """
      Result:
        names = {
          "kevin bacon": {"102"}
        }
      """
    # Duplicate Name
    else:
      names[row["name"].lower()].add(row["id"])
      """
      Example:
      Chris Evans
      Chris Evans
      could become:
      {
          "chris evans": {
              "100",
              "200"
          }
      }
      because multiple people may share the same name.
      """
```

result: 

```text
people = {
    "102": {
        "name": "Kevin Bacon",
        "birth": "1958",
        "movies": set()
    }
}

Why use set()?
Initially:set()
means:{}
(No movies loaded yet.)
Later:
{
    "104257",
    "112384"
}

Meaning:
Kevin Bacon starred in:
104257
112384

```
Creates a record for each actor.

---

## Step 2: Load Movies

```python
movies[row["id"]] = {
    "title": row["title"],
    "year": row["year"],
    "stars": set()
}
```

Creates a record for each movie.
```text
Why stars?
Later we want:
movies["104257"]["stars"]
to give:
{
    "102",
    "129"
}
Meaning:
Kevin Bacon
Tom Cruise
starred in that movie.

```

---

## Step 3: Load stars Relationships

```python
# Building the Connections
people[row["person_id"]]["movies"].add(row["movie_id"])
```

Adds movie information to an actor.

Example:

```python
people["102"]["movies"]
```

Output:

```python
{"104257"}
```

Result: 
```text
Before
people["102"] = {
    "name":"Kevin Bacon",
    "movies":set()
}
After
people["102"] = {
    "name":"Kevin Bacon",
    "movies":{
        "104257"
    }
}

Meaning:

Kevin Bacon starred in A Few Good Men.
```

---

Reverse Connection

```python
movies[row["movie_id"]]["stars"].add(row["person_id"])
```

Adds actor information to a movie.

Example:

```python
movies["104257"]["stars"]
```

Output:

```python
{"102", "129"}
```
Result:

```text
Before
movies["104257"] = {
    "title":"A Few Good Men",
    "stars":set()
}
After
movies["104257"] = {
    "title":"A Few Good Men",
    "stars":{
        "102"
    }
}

Meaning:

A Few Good Men stars Kevin Bacon.
```
---

## Why Use Sets?

```python
set()
```

Advantages:

- No duplicate entries
- Fast lookup: O(1)

Example:

```python
{
    "104257",
    "112384"
}
```

---

## Why Build Both Directions?

```text
Because later BFS needs:

Person → Movies
people["102"]["movies"]

returns:

{
    "104257"
}
Movie → Stars
movies["104257"]["stars"]

returns:

{
    "102",
    "129"
}

Then BFS can do:

Kevin Bacon
    ↓
A Few Good Men
    ↓
Tom Cruise

and discover neighboring actors.
```

## try / except KeyError
```text
try:

people[row["person_id"]]
and
movies[row["movie_id"]]
```

If a bad ID appears:

999999,104257

but

people["999999"]

doesn't exist,

Python raises:

KeyError

The code handles it:

except KeyError:
    pass

Meaning:

Ignore this bad record and continue.

## Graph Representation

The dataset forms a graph:

```text
Actor
   ↓
Movie
   ↓
Actor
```

Example:

```text
Kevin Bacon
     |
A Few Good Men
     |
Tom Cruise
```

---

## neighbors_for_person()

Returns all neighboring actors connected through movies.

```python
neighbors_for_person("102")
```

Possible result:

```python
{
    ("104257", "102"),
    ("104257", "129")
}
```

Meaning:

```text
Through movie 104257:

Kevin Bacon
Tom Cruise
```

---

## Why BFS?

Project requirement:

```text
Find the shortest path
```

BFS explores:

```text
Distance 1
Distance 2
Distance 3
...
```

Therefore:

```text
First solution found = Shortest solution
```

---

## BFS Search Flow

```text
Source Actor
      ↓
Queue Frontier
      ↓
Expand Neighbors
      ↓
Target Actor
```

Uses:

```python
QueueFrontier()
```

because BFS requires:

```text
FIFO (First In First Out)
```

---

## Final Memory Structure

After loading:

```text
Kevin Bacon (102)
Tom Cruise (129)

Movie:
A Few Good Men (104257)
```

Memory becomes:

```python
people = {
    "102": {
        "name": "Kevin Bacon",
        "movies": {"104257"}
    },
    "129": {
        "name": "Tom Cruise",
        "movies": {"104257"}
    }
}
```

```python
movies = {
    "104257": {
        "title": "A Few Good Men",
        "stars": {"102", "129"}
    }
}
```

```python
names = {
    "kevin bacon":{"102"},
    "tom cruise":{"129"}
}
```

---

## Key Takeaway

`load_data()` builds a **bidirectional graph**:

```text
Person → Movies
Movie  → Stars
```

This allows BFS to efficiently discover connections between actors and find the shortest path.

load_data() reads the CSV files and builds a bidirectional graph where each person knows the movies they appeared in, and each movie knows the actors who appeared in it, enabling BFS to find the shortest connection between two actors.

---
