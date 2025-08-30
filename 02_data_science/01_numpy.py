import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print("arr =", arr)

print("arr[2] =", arr[2])

print("arr[-1] =",arr[-1])

print("arr[1:4] =",arr[1:4])
print("arr[3:] =",arr[3:])

reshaped = arr.reshape(2,3)
print("reshaped =",reshaped)



matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("matrix =\n", matrix)

vector = np.array([1, 0 , -1])
print("vector =", vector)

result_add = matrix + vector
print("Add: \n", result_add)

result_mul = matrix * 2
print("Multiplication: \n", result_mul)



np.random.seed(42)

random_array = np.random.rand(3, 3)
print("Random Array: \n", random_array)


random_integers = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_integers)

"""
Great question, BIJU. Setting `np.random.seed(42)` in Python is like telling NumPy’s random number generator:  
**“Start from this exact point so I get the same results every time.”**

---

### 🎯 What It Actually Does

`np.random.seed(42)` sets the **seed value** for NumPy’s **pseudo-random number generator**. This ensures that any random numbers you generate—whether it’s for shuffling data, initializing weights, or simulating outcomes—will be **reproducible** across runs.

---

### 🧪 Example

```python
import numpy as np

np.random.seed(42)
print(np.random.rand(3))
```

Output:
```
[0.37454012 0.95071431 0.73199394]
```

Run this code again and again, and you’ll always get the same output. Without the seed, the numbers would change every time.

---

### 🔍 Why It Matters

- ✅ **Reproducibility**: Essential for debugging, testing, and sharing experiments
- 🧪 **Scientific integrity**: Ensures consistent results in simulations and ML experiments
- 🔄 **Controlled randomness**: Useful when tuning models or comparing algorithms

---

### ⚠️ Heads-Up

- Different seed values (e.g., `np.random.seed(7)`) produce different sequences.
- It doesn’t make the numbers truly random—it makes them **predictably random**.

"""