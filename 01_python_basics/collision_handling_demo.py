"""
Let’s walk through a hands-on Python example that shows how collision handling via chaining works when multiple annuity suppliers hash to the same bucket.
This simulates a real-world scenario where different supplier names—due to similar character patterns—end up in the same hash index. We’ll use a small prime bucket size to force collisions and demonstrate how chaining (storing multiple entries in a list at the same index) resolves it.


"""
# collision_handling_demo.py

class ModPrimeHasher:
    def __init__(self, bucket_size=7):  # Small prime to force collisions
        self.bucket_size = bucket_size
        self.lookup_table = [[] for _ in range(bucket_size)]

    def _hash(self, supplier_name: str) -> int:
        """Hash supplier name using sum of ASCII values mod prime."""
        ascii_sum = sum(ord(char) for char in supplier_name)
        return ascii_sum % self.bucket_size

    def insert_supplier(self, supplier_name: str, supplier_data: dict):
        """Insert supplier into hashed lookup table with chaining."""
        index = self._hash(supplier_name)
        self.lookup_table[index].append((supplier_name, supplier_data))
        print(f"Inserted '{supplier_name}' at index {index}")

    def show_table(self):
        """Display the full lookup table with collisions."""
        print("\n📦 Lookup Table with Chaining:")
        for i, bucket in enumerate(self.lookup_table):
            print(f"Bucket {i}: {bucket}")

# Example usage
if __name__ == "__main__":
    hasher = ModPrimeHasher(bucket_size=7)

    # Suppliers intentionally designed to collide
    suppliers = {
        "Annuity_Luxury": {"region": "US", "rating": "A"},
        "Annuity_Luxor": {"region": "EU", "rating": "A-"},
        "Annuity_Luxe": {"region": "Asia", "rating": "B+"},
        "Secure_Annuity": {"region": "US", "rating": "A+"},
        "Budget_Annuity": {"region": "EU", "rating": "B"},
    }

    for name, data in suppliers.items():
        hasher.insert_supplier(name, data)

    hasher.show_table()

"""
 What This Demonstrates
- Forced collisions: Using a small prime bucket size (7) increases the chance that multiple supplier names hash to the same index.
- Chaining: Instead of overwriting data, each bucket holds a list of (name, data) pairs.
- Retrieval remains efficient: Even with collisions, you can still find the correct supplier by scanning the short list in that bucket.

Think of each bucket like a drawer. If two suppliers happen to get the same drawer number, we don’t throw one away—we just stack them inside. So even if multiple suppliers land in the same drawer, we can still find each one quickly by checking the labels.
"""    