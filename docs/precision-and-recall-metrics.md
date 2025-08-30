Precision and recall are two key metrics used to evaluate the performance of classification models—especially when you're dealing with **imbalanced datasets** or **critical decision-making** (like fraud detection, medical diagnosis, or spam filtering).

---

### 🎯 Precision: How *accurate* are your positive predictions?

**Definition**:  
Precision measures the proportion of **true positives** out of all predicted positives.

\[
\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
\]

**Interpretation**:  
If your model says “yes,” how often is it correct?

**Example**:  
You build a model to detect birds in images. It flags 10 images as birds, but only 7 actually contain birds.  
→ Precision = 7/10 = 0.7

---

### 🔍 Recall: How *complete* are your positive predictions?

**Definition**:  
Recall measures the proportion of **true positives** out of all actual positives.

\[
\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
\]

**Interpretation**:  
Of all the actual “yes” cases, how many did your model find?

**Example**:  
There are 12 bird images in total. Your model correctly identifies 7 of them.  
→ Recall = 7/12 ≈ 0.58

---

### ⚖️ Trade-off: Precision vs. Recall

- **High precision, low recall**: Model is cautious—only flags when it's very sure, but misses many actual positives.
- **High recall, low precision**: Model is aggressive—flags many positives, but includes lots of false alarms.

---

### 📈 Use Case Tip

- Use **precision** when **false positives** are costly (e.g., marking legit emails as spam).
- Use **recall** when **false negatives** are costly (e.g., missing a cancer diagnosis).

Want to see how this plays out with a confusion matrix or visualize it with a precision-recall curve? I can scaffold that for you.