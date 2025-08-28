"""
A factorial is a way of multiplying a number by every whole number smaller than it, down to 1.
It’s written with an exclamation mark like this:
n! (read as “n factorial”)

Example:
Let’s say you want to find 4! (4 factorial):
4! = 4 × 3 × 2 × 1 = 24


So, 4! equals 24.

Why Does It Matter?
Factorials are used when you want to count how many ways things can be arranged or chosen.

Real-Life Example:
Imagine you have 3 different books and you want to know how many ways you can arrange them on a shelf.
- You could put Book A first, then B, then C.
- Or B first, then C, then A.
- And so on...
The total number of ways?
3! = 3 × 2 × 1 = 6 different arrangements.

Where You’ll See It
- Math class: In probability, algebra, and calculus.
- Computer science: In algorithms and recursion.
- Science: In statistics and genetics.
- Business: In modeling combinations or scenarios.



"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def print_factorial(n):
    result = factorial(n)
    print(f"The factorial of {n} is {result}")
    
print_factorial(2)



"""
3. Scenario Simulation & Permutations
If you're simulating product mixes or customer profiles, factorials help calculate:
- Permutations: Total ways to arrange product features or rider combinations.
- Combinations: Selecting subsets of products for portfolio optimization.

"""
from math import factorial

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

print(combinations(5, 2))  # e.g., choosing 2 riders from 5 options