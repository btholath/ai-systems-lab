The **sigmoid function** is a mathematical function often used in machine learning to **convert any real number into a value between 0 and 1**. It’s shaped like a smooth, S-curve and is especially handy when you want to interpret outputs as **probabilities**.

---

### ⚙️ Mathematical Definition

The sigmoid function is defined as:

\[
\sigma(x) = \frac{1}{1 + e^{-x}}
\]

- \( x \) is the input (can be any real number)
- \( e \) is Euler’s number (≈ 2.718)

---

### 📊 Why It’s Useful

- **Binary classification**: Converts raw scores into probabilities (e.g., 0.87 means 87% confidence in class 1)
- **Neural networks**: Acts as an activation function to introduce non-linearity
- **Smooth gradient**: Helps with backpropagation during training

---

### 🧠 Intuition

Think of it like a **squashing function**:
- Large positive inputs → output close to **1**
- Large negative inputs → output close to **0**
- Input of **0** → output is **0.5**

It’s like a soft decision-maker that says: “I’m not 100% sure, but I lean toward this class.”

---

Would you like to see how it behaves visually or how it compares to other activation functions like ReLU or tanh?