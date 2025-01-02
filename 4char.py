# Generate all 62^4=14,776,336 4 character strings using upper, lower, and numbers.
import itertools

# Define the character set
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Generate all combinations
combinations = [''.join(p) for p in itertools.product(chars, repeat=4)]

# Write to a file (optional, since the list is too large for memory in some cases)
with open("all_4_char.txt", "w") as file:
    file.write("\n".join(combinations))
