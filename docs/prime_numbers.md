
"""
Prime Numbers do play a subtle role in the digital infrastructure that supports annuity platforms and financial systems.
Here’s how:

🔐 1. Prime Numbers in Cryptography
Annuity platforms—especially those handling sensitive customer data and transactions—rely on secure encryption protocols like RSA, which are built on the mathematical properties of prime numbers.
• 	RSA encryption uses the difficulty of factoring large prime numbers to secure data.
• 	This protects customer information, payment details, and contract documents in transit and at rest.
So while prime numbers aren’t in the annuity formulas, they’re essential for securing the backend of annuity systems.

🧮 2. Prime Numbers in Hashing & Indexing
Financial databases often use prime-based hashing algorithms to:
• 	Efficiently store and retrieve customer records
• 	Avoid collisions in hash tables
• 	Optimize indexing in large-scale annuity datasets
This improves performance in systems that manage thousands of annuity contracts.

📊 3. Prime-Based Sampling in Analytics
In actuarial modeling or Monte Carlo simulations, prime numbers may be used to:
• 	Generate pseudo-random sequences
• 	Ensure non-repeating sampling across time periods or customer segments
This helps analysts simulate annuity outcomes across diverse demographic groups without bias.

Practical Tip for Your Backend
If you're designing a FastAPI-based annuity platform with supplier indexing or contract hashing:
• 	Choose a prime number for bucket size (e.g., 101, 211, 1009).
• 	Use mod prime hashing for quick lookup tables.
• 	Consider universal hashing if you're storing sensitive or high-volume data.
"""

# 1. Prime Bucket Size Selection
# prime_bucket_selector.py

def get_prime_bucket_size(min_size=100):
    """Returns the smallest prime number >= min_size from a predefined list."""
    prime_candidates = [101, 211, 307, 401, 503, 601, 701, 809, 907, 1009]
    for prime in prime_candidates:
        if prime >= min_size:
            return prime
    raise ValueError("No suitable prime found in list.")

# Example usage
bucket_size = get_prime_bucket_size(200)
print(f"Selected prime bucket size: {bucket_size}")


#2. Mod Prime Hashing for Lookup Tables
# mod_prime_hasher.py

class ModPrimeHasher:
    def __init__(self, bucket_size=101):
        self.bucket_size = bucket_size

    def hash_key(self, key: str) -> int:
        """Simple mod-prime hash using sum of ASCII values."""
        ascii_sum = sum(ord(char) for char in key)
        return ascii_sum % self.bucket_size

# Example usage
hasher = ModPrimeHasher(bucket_size=211)
supplier_id = "LOCKET_SUPPLIER_001"
bucket_index = hasher.hash_key(supplier_id)
print(f"Bucket index for '{supplier_id}': {bucket_index}")


#3. Universal Hashing for Sensitive Data
# universal_hasher.py
import random

class UniversalHasher:
    def __init__(self, prime=1009, bucket_count=101):
        self.p = prime
        self.m = bucket_count
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash_key(self, key: str) -> int:
        """Universal hash function for strings."""
        key_int = sum((i + 1) * ord(char) for i, char in enumerate(key))
        return ((self.a * key_int + self.b) % self.p) % self.m

# Example usage
hasher = UniversalHasher()
contract_id = "ANNUITY_CONTRACT_2025_ABC"
secure_index = hasher.hash_key(contract_id)
print(f"Secure index for '{contract_id}': {secure_index}")



#3. Universal Hashing for Sensitive Data
# universal_hasher.py
# universal_hasher.py
import random

class UniversalHasher:
    def __init__(self, prime=1009, bucket_count=101):
        self.p = prime
        self.m = bucket_count
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash_contract(self, contract_id: str, premium: float) -> int:
        """Universal hash using contract ID and premium value."""
        key_str = f"{contract_id}_{int(premium * 100)}"
        key_int = sum((i + 1) * ord(char) for i, char in enumerate(key_str))
        return ((self.a * key_int + self.b) % self.p) % self.m

# Example usage with annuity contract
hasher = UniversalHasher()
contract_id = "ANN2025_LOCKET_PREM"
premium_value = 1299.75  # USD
secure_index = hasher.hash_contract(contract_id, premium_value)
print(f"Secure index for contract '{contract_id}' with premium ${premium_value}: {secure_index}")

hese scripts are designed to support:
- Supplier indexing for inventory and sourcing
- Contract hashing for secure lookup and storage
- Bucket sizing for scalable data partitioning


---

## 🧠 1. **Choosing a Prime Bucket Size**
### 🔧 Real-World Use:
When you're storing annuity contracts or supplier records in a hash table or lookup structure, you need to divide them into "buckets" for fast access. Choosing a **prime number** as the bucket count helps avoid patterns that cause data to clump together, which slows down retrieval.

### 🗣️ Layman Explanation:
> "Imagine you’re organizing 1,000 annuity files into folders. If you use a number like 100, some folders get overloaded while others stay empty. But if you use a prime number like 101, the files spread out more evenly—so it’s faster to find what you need."

---

## ⚡ 2. **Mod Prime Hashing for Lookup Tables**
### 🔧 Real-World Use:
You want to quickly find supplier or contract data based on a unique name or ID. Mod prime hashing turns that name into a number that points to a specific bucket. It’s simple, fast, and works well when paired with a prime-sized table.

### 🗣️ Layman Explanation:
> "Think of a supplier name like 'LuxuryLockets' as a key. We turn that key into a number using math, then drop it into a specific drawer. Because we use a prime number of drawers, the keys don’t pile up in one place—they’re spread out, so we can grab the right one instantly."

---

## 🔐 3. **Universal Hashing for Sensitive or High-Volume Data**
### 🔧 Real-World Use:
When you’re handling thousands of annuity contracts or sensitive financial data, you need a hashing method that’s **secure and collision-resistant**. Universal hashing uses randomization and prime math to ensure that even similar-looking inputs land in different buckets.

### 🗣️ Layman Explanation:
> "If two annuity contracts look almost the same, we don’t want them ending up in the same folder. Universal hashing adds a layer of randomness—like shuffling the deck—so each contract gets its own space. It’s like giving every file a secret code that’s hard to guess and keeps things secure."

---

## 🧩 Why This Matters for Your Platform

- ⚙️ **Speed**: Hashing makes data retrieval lightning-fast—critical for real-time dashboards or supplier matching.
- 🔒 **Security**: Universal hashing protects sensitive contract data from predictable patterns.
- 📈 **Scalability**: Prime-based bucket sizing ensures your system stays efficient as you grow from 100 to 10,000 contracts.

---

If you’re pitching this to a business partner or investor, you could say:

> “We use smart mathematical techniques—like prime-based hashing—to make our annuity platform faster, safer, and more scalable. It’s like organizing a warehouse with precision so we never waste time searching, and we always keep customer data secure.”

