from stats import get_num_words
from stats import sorting
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

count = get_num_words()
print(f"Found {count} total words")

list_dict = sorting()
for char in list_dict:
    print(f"{char["char"]}: {char["num"]}")
