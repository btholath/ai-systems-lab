"""
Python example that simulates product mix scenarios using factorials, permutations, and combinations. 
This is especially useful when you're optimizing product portfolios or modeling customer rider selections.

"""
from math import factorial

# --- Permutations: Order matters ---
def permutations(n, r):
    return factorial(n) // factorial(n - r)

# --- Combinations: Order doesn't matter ---
def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# --- Example Scenario ---
# Suppose you have 5 product features (or riders)
# You want to simulate:
# - How many ways to arrange 3 of them (permutations)
# - How many ways to choose 3 of them (combinations)

features = ['Luxury', 'Budget', 'Handmade', 'Eco-Friendly', 'Customizable']
n = len(features)
r = 3

print(f"Total permutations (arrangements of {r} from {n}): {permutations(n, r)}")
print(f"Total combinations (selections of {r} from {n}): {combinations(n, r)}")

# --- Optional: Generate actual combinations using itertools ---
from itertools import permutations as permute, combinations as combine

print("\nSample permutations:")
for p in list(permute(features, r))[:5]:  # Show only first 5
    print(p)

print("\nSample combinations:")
for c in list(combine(features, r))[:5]:  # Show only first 5
    print(c)

"""
Why Factorials Matter in Scenario Simulation
• 	Factorial (): Total ways to arrange  items.
• 	Permutations (): Ways to arrange  items from  options (order matters).
• 	Combinations (): Ways to choose  items from  options (order doesn’t matter).

Use Cases in Your Context
• 	Supplier Mix Simulation: How many unique bundles can be offered from vetted suppliers.
• 	Customer Profile Modeling: Predict rider combinations customers might select.
• 	Inventory Planning: Estimate SKU diversity based on feature permutations.
• 	A/B Testing: Simulate test groups with different product combinations.
This helps in making data-driven decisions for product offerings and customer engagement strategies.
"""    