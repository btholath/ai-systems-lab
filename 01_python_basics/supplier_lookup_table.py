"""
Here’s a practical Python script that demonstrates Mod Prime Hashing for Lookup Tables using annuity supplier data. This simulates how you might store and retrieve supplier records efficiently in a backend system—like your FastAPI-based annuity platform.
"""
# supplier_lookup_table.py

class ModPrimeHasher:
    def __init__(self, bucket_size=211):
        self.bucket_size = bucket_size
        self.lookup_table = [[] for _ in range(bucket_size)]

    def _hash(self, supplier_name: str) -> int:
        """Hash supplier name using sum of ASCII values mod prime."""
        ascii_sum = sum(ord(char) for char in supplier_name)
        return ascii_sum % self.bucket_size

    def insert_supplier(self, supplier_name: str, supplier_data: dict):
        """Insert supplier into hashed lookup table."""
        index = self._hash(supplier_name)
        self.lookup_table[index].append((supplier_name, supplier_data))
        print(f"Inserted '{supplier_name}' at index {index}")

    def find_supplier(self, supplier_name: str) -> dict:
        """Retrieve supplier data by name."""
        index = self._hash(supplier_name)
        for name, data in self.lookup_table[index]:
            if name == supplier_name:
                return data
        return None

# Example usage
if __name__ == "__main__":
    hasher = ModPrimeHasher(bucket_size=211)

    # Sample annuity suppliers
    suppliers = {
        "AnnuitySource_LuxuryLockets": {"region": "US", "rating": "A+", "products": 12},
        "SecureAnnuity_HandmadeVault": {"region": "EU", "rating": "A", "products": 8},
        "BudgetAnnuity_ChainCraft": {"region": "Asia", "rating": "B+", "products": 15},
    }

    # Insert suppliers
    for name, data in suppliers.items():
        hasher.insert_supplier(name, data)

    # Lookup example
    search_name = "SecureAnnuity_HandmadeVault"
    result = hasher.find_supplier(search_name)
    if result:
        print(f"\nFound supplier '{search_name}': {result}")
    else:
        print(f"\nSupplier '{search_name}' not found.")

"""
What This Script Shows
• 	Efficient indexing: Supplier names are hashed into a fixed-size table using a prime modulus.
• 	Collision handling: Multiple suppliers can land in the same bucket, handled via chaining ().
• 	Fast lookup: You can retrieve supplier data in near-constant time.

We turn each supplier’s name into a number using math, then store their info in a specific drawer. 
Because we use a prime number of drawers, the names spread out evenly. 
That way, when we need to find a supplier, we know exactly where to look—no searching through the whole cabinet.
"""        