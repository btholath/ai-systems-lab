"""
## What Is a Vector?

A **vector** is a mathematical object that has **two key properties**:

- **Magnitude**: How big or strong it is (like the length of an arrow).
- **Direction**: Where it’s pointing (like north, south, or diagonally).

You can think of a vector as an **arrow** drawn on a graph:
- The **tail** is where it starts.
- The **head** is where it points.
- The **length** of the arrow shows its magnitude.
- The **angle** shows its direction.

---

## In Numbers: Vectors as Lists
In programming and data science, we often represent vectors as **lists of numbers**. For example:

```python
v = [3, 4]
```

This is a 2D vector:
- It moves 3 units in the x-direction.
- It moves 4 units in the y-direction.

Its magnitude is calculated using the Pythagorean theorem:

\[
\text{Magnitude} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
\]


## Why Vectors Matter

Vectors are everywhere in machine learning, physics, and engineering:

| Field            | Example of Vectors                     |
|------------------|----------------------------------------|
| Machine Learning | Feature vectors (inputs to models)     |
| Physics          | Velocity, force, acceleration          |
| Graphics         | Position and movement of objects       |
| Economics        | Portfolio weights or demand vectors    |

"""

import numpy as np

# Define a vector
v = np.array([3, 4])

# Compute its magnitude
magnitude = np.linalg.norm(v)
print("Magnitude:", magnitude)
