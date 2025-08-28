"""

• Rider listing helps organize optional features for customer selection.
• Product description analysis supports NLP, indexing, and compliance checks.
• File modularity enables integration into supplier vetting or inventory pipelines.
"""
import os

# --- File Analysis: Count Lines and Words ---
def count_words_and_lines(filename):
    """Count the number of lines and words in an annuity product file."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"📄 File: {filename}")
            print(f"Number of lines: {line_count}")
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")

# --- Write Annuity Riders to File ---
def write_items_to_file(filename, items):
    """Write a list of annuity riders or features to a file."""
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")

# --- Read and Display File Contents ---
def read_items_from_file(filename):
    """Read and display annuity riders or features from a file."""
    try:
        with open(filename, "r") as file:
            items = file.readlines()
            print(f"📦 Items in '{filename}':")
            for item in items:
                print(f"- {item.strip()}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found!")

# --- Read Entire File Content Safely ---
def read_full_file(filename):
    """Read full content of an annuity product file."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"\n📘 Full content of '{filename}':\n{content}")
    except FileNotFoundError:
        print("❌ File Not Found!")

# --- Sample Data ---
annuity_riders = [
    "Return of Premium",
    "Guaranteed Lifetime Withdrawal Benefit",
    "Death Benefit Rider",
    "Inflation Protection",
    "Long-Term Care Rider"
]

# --- File Names ---
rider_file = "annuity_riders.txt"
product_file = "annuity_product_description.txt"

# --- Execution ---
write_items_to_file(rider_file, annuity_riders)
read_items_from_file(rider_file)
count_words_and_lines(rider_file)

# Simulate a product description file
product_description = """\
This annuity product offers a guaranteed lifetime income stream.
Optional riders include Return of Premium and Long-Term Care benefits.
Ideal for retirement planning with inflation protection built-in.
"""

# Write and analyze product description
with open(product_file, "w") as f:
    f.write(product_description)

count_words_and_lines(product_file)
read_full_file(product_file)