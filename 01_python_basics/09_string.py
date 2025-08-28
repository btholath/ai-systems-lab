def is_palindrome(text):
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

input_text = input("Enter a string: ")
if is_palindrome(input_text):
    print(f'"{input_text}" is a palindrome.')
else:
    print(f'"{input_text}" is not a palindrome.')


import re

def clean_text(text):
    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    # Remove extra spaces
    text = " ".join(text.split())
    # Convert to lowercase
    return text.lower()

input_text = "   Hello, World.!!! Welcome to Python, Programming....    "
cleaned_text = clean_text(input_text)
print("Cleaned Text: ", cleaned_text)


import re


# split()

sentence = "Python is fun"
words = sentence.split()
#print(words)

# join()
new_sentence = "|".join(words)
#print(new_sentence)


text = "I love Java"
updated_text = text.replace("Java", "Python")
#print(updated_text)

messy = "     Hello, World     "
print(messy)
cleaned_text = messy.strip()
print(cleaned_text)

import re

text = "Contact me at 123-456-7890"
digits = re.findall(r"\d+", text)
print(digits)

updated_text = re.sub(r"\d", "X", text)
print(updated_text)


import re

# --- Text Utilities ---
def is_palindrome(text):
    """Check if a string is a palindrome (ignoring punctuation and case)."""
    text = "".join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

def clean_text(text):
    """Clean text by removing punctuation, extra spaces, and converting to lowercase."""
    text = re.sub(r"[^\w\s]", "", text)
    text = " ".join(text.split())
    return text.lower()

def extract_digits(text):
    """Extract all digit sequences from a string."""
    return re.findall(r"\d+", text)

def mask_digits(text):
    """Replace all digits in a string with 'X'."""
    return re.sub(r"\d", "X", text)

# --- String Manipulation ---
def split_and_join(sentence, delimiter="|"):
    """Split a sentence into words and rejoin with a delimiter."""
    words = sentence.split()
    return delimiter.join(words)

def replace_text(text, old, new):
    """Replace a substring with another."""
    return text.replace(old, new)

def strip_whitespace(text):
    """Remove leading and trailing whitespace."""
    return text.strip()

# --- Annuity Line of Business Example ---
def simulate_annuity_text_processing():
    """Simulate text processing for annuity product descriptions."""
    raw_description = "   Premium-based annuity, with riders like Return of Premium, Guaranteed Income!!!   "
    print("Original Description:", raw_description)

    cleaned = clean_text(raw_description)
    print("Cleaned Description:", cleaned)

    if is_palindrome(cleaned):
        print("Note: Description is a palindrome (rare but interesting).")
    else:
        print("Description is not a palindrome.")

    digits = extract_digits(raw_description)
    print("Extracted Digits:", digits)

    masked = mask_digits(raw_description)
    print("Masked Description:", masked)

    joined = split_and_join(cleaned, delimiter=" | ")
    print("Joined Description:", joined)

    replaced = replace_text(cleaned, "guaranteed income", "lifetime payout")
    print("Updated Description:", replaced)

# --- Main Execution ---
def main():
    # General Palindrome Check
    user_input = input("Enter a string to check for palindrome: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

    # Run Annuity Simulation
    print("\n--- Annuity Text Processing Simulation ---")
    simulate_annuity_text_processing()

if __name__ == "__main__":
    main()